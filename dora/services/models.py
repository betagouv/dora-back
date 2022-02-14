import uuid

from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import CharField
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from dora.admin_express.models import AdminDivisionType
from dora.structures.models import Structure, StructureMember


def make_unique_slug(instance, parent_slug, value, length=20):
    model = instance.__class__
    base_slug = parent_slug + "-" + slugify(value)[:length]
    unique_slug = base_slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = (
            base_slug + "-" + get_random_string(4, "abcdefghijklmnopqrstuvwxyz")
        )
    return unique_slug


class ServiceCategories(models.TextChoices):
    MOBILITY = ("MO", "Mobilité")
    HOUSING = ("HO", "Logement – Hébergement")
    CHILD_CARE = ("CC", "Garde d’enfant")
    FFL = "FL", "Apprendre le Français"
    ILLITERACY = "IL", "Illettrisme"
    CREATION = "CR", "Création d’activité"
    DIGITAL = "DI", "Numérique"
    FINANCIAL = "FI", "Difficultés financières"
    GLOBAL = "GL", "Acco. global individualisé"


# Subcategories are prefixed by their category
class ServiceSubCategories(models.TextChoices):

    MO_MOBILITY = ("MO-MO", "Se déplacer sans permis et/ou sans véhicule personnel")
    MO_WORK = ("MO-WK", "Reprendre un emploi ou une formation")
    MO_LICENSE = (
        "MO-LI",
        "Préparer son permis de conduire, se réentraîner à la conduite",
    )
    MO_VEHICLE = ("MO-VE", "Louer ou acheter un véhicule")
    MO_MAINTENANCE = ("MO-MA", "Entretenir ou réparer son véhicule")

    MO_2WHEELS = "MO_2W", "Apprendre à utiliser un deux roues"
    MO_BLOCKS = "MO_BLK", "Identifier ses freins, et définir ses besoins en mobilité"
    MO_HELP = "MO_HLP", "Être accompagné(e) dans son parcours mobilité"

    HO_ADAPT = "HO_AD", "Besoin d’adapter mon logement"
    HO_KEEP = ("HO-KE", "Problème avec son logement")
    HO_SHORT = ("HO-SH", "Mal logé/sans logis")
    HO_MOVE = "HO_MO", "Déménagement"
    HO_ACCESS = ("HO-AC", "Être accompagné(e) pour se loger")
    HO_WORK = "HO_WK", "Reprendre un emploi ou une formation"

    CC_INFO = ("CC-IN", "Information et accompagnement des parents")
    CC_TEMP = ("CC-TM", "Garde ponctuelle")
    CC_LONG = ("CC-LG", "Garde pérenne")
    CC_EXTRACURRICULAR = ("CC-EX", "Garde périscolaire")

    FL_COM = "FL-CO", "Communiquer dans la vie de tous les jours"
    FL_INSERTION = "FL-IN", "Accompagnement vers l’insertion professionnelle"
    FL_FORMATION = "FL-FO", "Suivre une formation"

    IL_COM = "IL-CO", "Communiquer dans la vie de tous les jours"
    IL_INSERTION = "IL-IN", "Accompagnement vers l’insertion professionnelle"
    IL_FORMATION = "IL-FO", "Suivre une formation"
    IL_ADMIN = "IL-AD", "Être informé sur les  démarches administratives"

    CR_IDEA = "CR-ID", "De l’idée au projet"
    CR_ELABORATE = "CR-EL", "Élaborer son projet"
    CR_START = "CR-ST", "Démarrer son activité"

    DI_BASICS = "DI-BA", "Prendre en main un équipement informatique"
    DI_NAVIGATE = "DI-NA", "Naviguer sur internet"
    DI_EMAIL = "DI-EM", "Envoyer, recevoir, gérer ses courriels"
    DI_PHONE = "DI-PH", "Utiliser son smartphone"
    DI_CONTENT = "DI-CN", "Créer et gérer ses contenus numériques"
    DI_WORDS = "DI-WD", "Connaitre l’environnement et le vocabulaire numérique"
    DI_WORDPROC = "DI-WP", "Apprendre les bases du traitement de texte"
    DI_COM = "DI-CO", "Échanger avec ses proches"
    DI_JOB = "DI-JO", "Trouver un emploi ou une formation"
    DI_CHILD = "DI-CH", "Accompagner son enfant"
    DI_ADMIN = "DI-AD", "Réaliser une démarche en ligne"


class ServiceKind(models.TextChoices):
    SUPPORT = ("SU", "Accompagnement")
    RECEPTION = "RE", "Accueil"
    FINANCIAL = ("FI", "Aide financière")
    MATERIAL = ("MA", "Aide materielle")
    WORKSHOP = "WK", "Atelier"
    FORMATION = "FO", "Formation"
    INFORMATION = "IN", "Information"


class BeneficiaryAccessMode(models.TextChoices):
    ONSITE = ("OS", "Se présenter")
    PHONE = ("PH", "Téléphoner")
    EMAIL = ("EM", "Envoyer un mail")
    OTHER = ("OT", "Autre (préciser)")


class CoachOrientationMode(models.TextChoices):
    PHONE = ("PH", "Téléphoner")
    EMAIL = ("EM", "Envoyer un mail")
    FORM = ("FO", "Envoyer le formulaire d’adhésion")
    EMAIL_PRESCRIPTION = ("EP", "Envoyer un mail avec une fiche de prescription")
    OTHER = ("OT", "Autre (préciser)")


class LocationKind(models.TextChoices):
    ONSITE = ("OS", "En présentiel")
    REMOTE = ("RE", "À distance")


class CustomizableChoice(models.Model):
    name = models.CharField(max_length=140)
    structure = models.ForeignKey(
        Structure,
        on_delete=models.CASCADE,
        db_index=True,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=["name", "structure"],
                name="%(app_label)s_unique_%(class)s_by_structure",
            )
        ]

    def __str__(self):
        return self.name


class AccessCondition(CustomizableChoice):
    class Meta(CustomizableChoice.Meta):
        verbose_name = "Critère d’admission"
        verbose_name_plural = "Critères d’admission"


class ConcernedPublic(CustomizableChoice):
    class Meta(CustomizableChoice.Meta):
        verbose_name = "Public concerné"
        verbose_name_plural = "Publics concernés"


class Requirement(CustomizableChoice):
    class Meta(CustomizableChoice.Meta):
        verbose_name = "Pré-requis ou compétence"
        verbose_name_plural = "Pré-requis ou compétences"


class Credential(CustomizableChoice):
    class Meta(CustomizableChoice.Meta):
        verbose_name = "Justificatif à fournir"
        verbose_name_plural = "Justificatifs à fournir"


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)

    ##############
    # Presentation
    name = models.CharField(verbose_name="Nom de l’offre", max_length=140)
    short_desc = models.TextField(verbose_name="Résumé", max_length=280, blank=True)
    full_desc = models.TextField(
        verbose_name="Descriptif complet de l’offre", blank=True
    )

    ##########
    # Typology
    kinds = ArrayField(
        models.CharField(max_length=2, choices=ServiceKind.choices),
        verbose_name="Type de service",
        db_index=True,
        blank=True,
        default=list,
    )
    category = models.CharField(
        max_length=2,
        choices=ServiceCategories.choices,
        verbose_name="Catégorie principale",
        db_index=True,
        blank=True,
    )

    subcategories = ArrayField(
        models.CharField(max_length=6, choices=ServiceSubCategories.choices),
        verbose_name="Sous-catégorie",
        blank=True,
        default=list,
    )

    ############
    # Conditions

    access_conditions = models.ManyToManyField(
        AccessCondition, verbose_name="Critères d’admission", blank=True
    )
    concerned_public = models.ManyToManyField(
        ConcernedPublic, verbose_name="Publics concernés", blank=True
    )
    is_cumulative = models.BooleanField(verbose_name="Solution cumulable", default=True)
    has_fee = models.BooleanField(
        verbose_name="Frais à charge pour le bénéficiaire", default=False
    )
    fee_details = models.TextField(verbose_name="Détail des frais", blank=True)

    ############
    # Modalities

    beneficiaries_access_modes = ArrayField(
        models.CharField(max_length=2, choices=BeneficiaryAccessMode.choices),
        verbose_name="Comment mobiliser la solution en tant que bénéficiaire",
        blank=True,
        default=list,
    )
    beneficiaries_access_modes_other = CharField(
        verbose_name="Autre", max_length=280, blank=True
    )
    coach_orientation_modes = ArrayField(
        models.CharField(max_length=2, choices=CoachOrientationMode.choices),
        verbose_name="Comment orienter un bénéficiaire en tant qu’accompagnateur",
        blank=True,
        default=list,
    )
    coach_orientation_modes_other = CharField(
        verbose_name="Autre", max_length=280, blank=True
    )
    requirements = models.ManyToManyField(
        Requirement,
        verbose_name="Quels sont les pré-requis ou compétences ?",
        blank=True,
    )
    credentials = models.ManyToManyField(
        Credential, verbose_name="Quels sont les justificatifs à fournir ?", blank=True
    )

    forms = ArrayField(
        models.CharField(max_length=1024),
        verbose_name="Partagez les documents à compléter",
        blank=True,
        default=list,
    )
    online_form = models.URLField(
        verbose_name="Formulaire en ligne à compléter",
        blank=True,
    )

    ########################
    # Practical informations

    # Contact

    contact_name = models.CharField(
        max_length=140, verbose_name="Nom du contact référent", blank=True
    )
    contact_phone = models.CharField(
        verbose_name="Numéro de téléphone", max_length=10, blank=True
    )
    contact_email = models.EmailField(verbose_name="Courriel", blank=True)
    is_contact_info_public = models.BooleanField(
        verbose_name="Rendre mes informations publiques",
        default=False,
    )

    # Location

    location_kinds = ArrayField(
        models.CharField(max_length=2, choices=LocationKind.choices),
        verbose_name="Lieu de déroulement",
        blank=True,
        default=list,
    )

    remote_url = models.URLField(verbose_name="Lien visioconférence", blank=True)
    address1 = models.CharField(verbose_name="Adresse", max_length=255, blank=True)
    address2 = models.CharField(
        verbose_name="Compléments d’adresse", max_length=255, blank=True
    )
    postal_code = models.CharField(verbose_name="Code postal", max_length=5, blank=True)
    city_code = models.CharField(verbose_name="Code INSEE", max_length=5, blank=True)
    city = models.CharField(verbose_name="Ville", max_length=200, blank=True)
    geom = models.PointField(
        srid=4326, geography=True, spatial_index=True, null=True, blank=True
    )

    diffusion_zone_type = models.CharField(
        max_length=10,
        choices=AdminDivisionType.choices,
        verbose_name="Zone de diffusion",
        db_index=True,
        blank=True,
    )
    diffusion_zone_details = models.CharField(max_length=9, db_index=True, blank=True)
    qpv_or_zrr = models.BooleanField(default=False)

    # Duration
    recurrence = models.CharField(verbose_name="Autre", max_length=140, blank=True)

    suspension_date = models.DateField(
        verbose_name="À partir d’une date", null=True, blank=True, db_index=True
    )

    ##########
    # Metadata

    structure = models.ForeignKey(
        Structure,
        verbose_name="Structure",
        on_delete=models.CASCADE,
        db_index=True,
        related_name="services",
    )
    is_draft = models.BooleanField(default=True)
    is_suggestion = models.BooleanField(default=False)

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField(blank=True, null=True)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    last_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="+",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        instance._original = dict(zip(field_names, values))
        return instance

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = make_unique_slug(self, self.structure.slug, self.name)
        if not self._state.adding:
            original_is_draft = self._original["is_draft"]
            if original_is_draft is True and self.is_draft is False:
                self.publication_date = timezone.now()

        return super().save(*args, **kwargs)

    def can_write(self, user):
        return (
            user.is_staff
            or StructureMember.objects.filter(
                structure_id=self.structure_id, user_id=user.id
            ).exists()
        )


class ServiceModificationHistoryItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    fields = ArrayField(
        models.CharField(
            max_length=50,
        ),
    )

    class Meta:
        ordering = ["-date"]
