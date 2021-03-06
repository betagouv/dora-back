# Generated by Django 3.2.5 on 2021-07-26 15:09

import uuid

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("structures", "0003_auto_20210726_1508"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AccessCondition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name="ConcernedPublic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name="Credential",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name="Requirement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=140, verbose_name="Nom de l???offre"),
                ),
                (
                    "short_desc",
                    models.TextField(blank=True, max_length=280, verbose_name="R??sum??"),
                ),
                (
                    "full_desc",
                    models.TextField(
                        blank=True, verbose_name="Descriptif complet de l???offre"
                    ),
                ),
                (
                    "kinds",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("MA", "Aide materielle"),
                                ("FI", "Aide financi??re"),
                                ("SU", "Accompagnement"),
                            ],
                            max_length=2,
                        ),
                        blank=True,
                        db_index=True,
                        default=list,
                        size=None,
                        verbose_name="Type de service",
                    ),
                ),
                (
                    "categories",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("MO", "Mobilit??"),
                                ("HO", "Logement"),
                                ("CC", "Garde d???enfant"),
                            ],
                            max_length=2,
                        ),
                        blank=True,
                        db_index=True,
                        default=list,
                        size=None,
                        verbose_name="Cat??gorie principale",
                    ),
                ),
                (
                    "subcategories",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("MFH", "Aide aux frais de d??placements"),
                                ("MCR", "R??paration de voitures ?? prix r??duit"),
                            ],
                            max_length=3,
                        ),
                        blank=True,
                        default=list,
                        size=None,
                        verbose_name="Sous-cat??gorie",
                    ),
                ),
                (
                    "is_common_law",
                    models.BooleanField(
                        default=False,
                        verbose_name="Il s???agit d'un service de Droit commun\xa0?",
                    ),
                ),
                (
                    "is_cumulative",
                    models.BooleanField(
                        default=True, verbose_name="Solution cumulable"
                    ),
                ),
                (
                    "has_fee",
                    models.BooleanField(
                        default=False,
                        verbose_name="Frais ?? charge pour le b??n??ficiaire",
                    ),
                ),
                (
                    "fee_details",
                    models.CharField(
                        blank=True, max_length=140, verbose_name="D??tail des frais"
                    ),
                ),
                (
                    "beneficiaries_access_modes",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("OS", "Se pr??senter"),
                                ("PH", "T??l??phoner"),
                                ("EM", "Envoyer un mail"),
                                ("OT", "Autre"),
                            ],
                            max_length=2,
                        ),
                        blank=True,
                        default=list,
                        size=None,
                        verbose_name="Comment mobiliser la solution en tant que b??n??ficiaire",
                    ),
                ),
                (
                    "beneficiaries_access_modes_other",
                    models.CharField(blank=True, max_length=280, verbose_name="Autre"),
                ),
                (
                    "coach_orientation_modes",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("PH", "T??l??phoner"),
                                ("EM", "Envoyer un mail"),
                                (
                                    "EP",
                                    "Envoyer un mail avec une fiche de prescription",
                                ),
                                ("OT", "Autre"),
                            ],
                            max_length=2,
                        ),
                        blank=True,
                        default=list,
                        size=None,
                        verbose_name="Comment orienter un b??n??ficiaire en tant qu???accompagnateur",
                    ),
                ),
                (
                    "coach_orientation_modes_other",
                    models.CharField(blank=True, max_length=280, verbose_name="Autre"),
                ),
                (
                    "forms",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FileField(upload_to=""),
                        blank=True,
                        default=list,
                        size=None,
                        verbose_name="Partagez les documents ?? compl??ter",
                    ),
                ),
                (
                    "online_forms",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=280),
                        blank=True,
                        default=list,
                        size=None,
                        verbose_name="Formulaires en ligne ?? compl??ter",
                    ),
                ),
                (
                    "contact_name",
                    models.CharField(
                        blank=True,
                        max_length=140,
                        verbose_name="Nom du contact r??f??rent",
                    ),
                ),
                (
                    "contact_phone",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Num??ro de t??l??phone"
                    ),
                ),
                (
                    "contact_email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="Courriel"
                    ),
                ),
                ("contact_url", models.URLField(blank=True, verbose_name="Site web")),
                (
                    "is_contact_info_public",
                    models.BooleanField(
                        default=False, verbose_name="Rendre mes informations publiques"
                    ),
                ),
                (
                    "location_kind",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[("OS", "En pr??sentiel"), ("RE", "?? distance")],
                            max_length=2,
                        ),
                        blank=True,
                        default=list,
                        size=None,
                        verbose_name="Lieu de d??roulement",
                    ),
                ),
                (
                    "remote_url",
                    models.URLField(blank=True, verbose_name="Lien visioconf??rence"),
                ),
                (
                    "address1",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Adresse"
                    ),
                ),
                (
                    "address2",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Compl??ments d???adresse"
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True, max_length=5, verbose_name="Code postal"
                    ),
                ),
                (
                    "city_code",
                    models.CharField(
                        blank=True, max_length=5, verbose_name="Code INSEE"
                    ),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=200, verbose_name="Ville"),
                ),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                (
                    "is_time_limited",
                    models.BooleanField(
                        default=False,
                        verbose_name="Votre offre est limit??e dans le temps ?",
                    ),
                ),
                (
                    "start_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date de d??but"
                    ),
                ),
                (
                    "end_date",
                    models.DateField(blank=True, null=True, verbose_name="Date de fin"),
                ),
                (
                    "recurrence",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("DD", "Tous les jours"),
                            ("WW", "Toutes les semaines"),
                            ("MM", "Tous les mois"),
                            ("OT", "Autre"),
                        ],
                        max_length=2,
                        verbose_name="R??currences",
                    ),
                ),
                (
                    "recurrence_other",
                    models.CharField(blank=True, max_length=140, verbose_name="Autre"),
                ),
                (
                    "suspension_count",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="?? partir d???un nombre d???inscriptions",
                    ),
                ),
                (
                    "suspension_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="?? partir d???une date"
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("modification_date", models.DateTimeField(auto_now=True)),
                (
                    "access_conditions",
                    models.ManyToManyField(
                        blank=True,
                        to="services.AccessCondition",
                        verbose_name="Crit??res d???admission",
                    ),
                ),
                (
                    "concerned_public",
                    models.ManyToManyField(
                        blank=True,
                        to="services.ConcernedPublic",
                        verbose_name="Publics concern??s",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "credentials",
                    models.ManyToManyField(
                        blank=True,
                        to="services.Credential",
                        verbose_name="Quels sont les justificatifs ?? fournir ?",
                    ),
                ),
                (
                    "last_editor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "requirements",
                    models.ManyToManyField(
                        blank=True,
                        to="services.Requirement",
                        verbose_name="Quels sont les pr??-requis ou comp??tences ?",
                    ),
                ),
                (
                    "structure",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="structures.structure",
                        verbose_name="",
                    ),
                ),
            ],
        ),
    ]
