import csv
import logging
from itertools import groupby
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import transaction
from tqdm import tqdm

from dora.sirene.models import Establishment
from dora.structures import utils
from dora.structures.models import Structure, StructureSource, StructureTypology
from dora.users.models import User

logging.basicConfig()
logger = logging.getLogger()


class Command(BaseCommand):
    """Commande d'import des données SIAE d'ITOU depuis format csv

    Les données ITOU siae sont:
    * soit des données de structures taggées comment étant créées par un utilisateur.
    Leurs sirets sont valides et ces structures sont des structures mères.
    * soit des données de structures qui doivent être considérées comme des antennes.
    Structure mères et antennes partagent le même asp_id.
    """

    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument("--log-level", default="INFO", type=str)
        parser.add_argument("input_path", type=Path)

    def handle(self, *args, **options):
        logger.setLevel(options["log_level"])
        itou_siae_input_path = options["input_path"]

        with itou_siae_input_path.open(newline="") as f:
            data = [row for row in csv.DictReader(f)]

        logger.info(f"{len(data)} lignes en entrée")

        antennes = [d for d in data if d["source"] == "USER_CREATED"]
        structures = [d for d in data if d not in antennes]

        structures_by_siret = {
            k: list(g) for k, g in groupby(structures, lambda d: d["siret"])
        }
        antennes_by_asp_id = {
            k: list(g) for k, g in groupby(antennes, lambda d: d["asp_id"])
        }

        logger.info(f"{len(structures)} structures mères en entrée")
        logger.info(f"{len(antennes)} antennes en entrée")

        with transaction.atomic():
            bot_user = User.objects.get_dora_bot()
            structure_source, _ = StructureSource.objects.get_or_create(
                value="ITOU", defaults={"label": "Import ITOU"}
            )

            for siret, data in tqdm(
                structures_by_siret.items(), disable=logger.level < logging.INFO
            ):
                if len(data) > 1:
                    # 2 structures mères partagent le même siret
                    logger.debug(f"{siret} commun à 2 structures mères. Ignoré")
                    continue

                datum = data[0]
                establishment = Establishment.objects.filter(siret=siret).first()
                if establishment is None:
                    logger.debug(f"{siret} probablement fermé. Ignoré")
                    # structure probablement fermée
                    continue

                structure = Structure.objects.filter(siret=establishment.siret).first()
                if structure is not None:
                    logger.debug(f"{siret} déjà référencé. Ignoré")
                    # structure déjà référencée
                    continue

                # nouvelle structure
                structure = Structure.objects.create_from_establishment(establishment)
                structure.source = structure_source
                structure.creator = bot_user
                structure.last_editor = bot_user
                structure.name = datum["name"]
                structure.email = datum["email"]
                structure.phone = utils.normalize_phone_number(datum["phone"])
                structure.url = datum["website"]
                structure.short_desc, structure.full_desc = utils.normalize_description(
                    datum["description"], limit=Structure.short_desc.field.max_length
                )
                if datum["coords"] != "":
                    structure.longitude, structure.latitude = utils.normalize_coords(
                        datum["coords"]
                    )
                else:
                    structure.longitude, structure.latitude = (
                        establishment.longitude,
                        establishment.latitude,
                    )
                structure.creation_date = datum["created_at"]
                structure.modification_date = datum["updated_at"]
                structure.typology = StructureTypology.objects.get(value=datum["kind"])
                structure.save()

                logger.debug(f"{siret} nouvellement référencé")

                # antennes associées
                if "asp_id" in datum and datum["asp_id"] in antennes_by_asp_id:
                    for antenne_datum in antennes_by_asp_id[datum["asp_id"]]:
                        antenne = Structure.objects.create_from_parent_structure(
                            parent=structure,
                            name=antenne_datum["name"],
                            source=structure.source,
                            creator=structure.creator,
                            last_editor=structure.last_editor,
                            address1=antenne_datum["address_line_1"],
                            address2=antenne_datum["address_line_2"],
                            postal_code=antenne_datum["post_code"],
                            city=antenne_datum["city"],
                            email=antenne_datum["email"],
                            phone=utils.normalize_phone_number(antenne_datum["phone"]),
                            url=antenne_datum["website"],
                            typology=StructureTypology.objects.get(value=datum["kind"]),
                            creation_date=antenne_datum["created_at"],
                            modification_date=antenne_datum["updated_at"],
                        )

                        if antenne_datum["description"] != "":
                            (
                                antenne.short_desc,
                                antenne.full_desc,
                            ) = utils.normalize_description(
                                datum["description"],
                                limit=Structure.short_desc.field.max_length,
                            )

                        if antenne_datum["coords"] != "":
                            (
                                antenne.longitude,
                                antenne.latitude,
                            ) = utils.normalize_coords(antenne_datum["coords"])

                        antenne.save()

                        logger.debug(
                            f"{antenne_datum['siret']} nouvellement référencé comme "
                            f"antenne de {siret}"
                        )
