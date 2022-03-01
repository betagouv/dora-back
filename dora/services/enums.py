from django.db import models


class ServiceCategories(models.TextChoices):
    CREATION = "CR", "Création d’activité"
    DIGITAL = "DI", "Numérique"
    EQUIPMENTS = "EQ", "Equipement et alimentation"
    FAMILY = "FA", "Famille"
    FFL = "FL", "Apprendre le Français"
    FINANCIAL = "FI", "Difficultés financières"
    GLOBAL = "GL", "Acco. global individualisé"
    HANDICAP = "HA", "Handicap"
    HEALTH = "HE", "Santé"
    HOUSING = "HO", "Logement – Hébergement"
    ILLITERACY = "IL", "Illettrisme"
    JOBS = "JO", "Emploi"
    MOBILITY = "MO", "Mobilité"
    REMOBILISATION = "RE", "Remobilisation"
    RIGHTS = "RI", "Accès aux droits & citoyenneté"


# Subcategories are prefixed by their category
class ServiceSubCategories(models.TextChoices):

    CR_ELABORATE = "CR-EL", "Élaborer son projet"
    CR_IDEA = "CR-ID", "De l’idée au projet"
    CR_START = "CR-ST", "Démarrer son activité"

    DI_ADMIN = "DI-AD", "Réaliser une démarche en ligne"
    DI_BASICS = "DI-BA", "Prendre en main un équipement informatique"
    DI_CHILD = "DI-CH", "Accompagner son enfant"
    DI_COM = "DI-CO", "Échanger avec ses proches"
    DI_CONTENT = "DI-CN", "Créer et gérer ses contenus numériques"
    DI_EMAIL = "DI-EM", "Envoyer, recevoir, gérer ses courriels"
    DI_JOB = "DI-JO", "Trouver un emploi ou une formation"
    DI_NAVIGATE = "DI-NA", "Naviguer sur internet"
    DI_PHONE = "DI-PH", "Utiliser son smartphone"
    DI_WORDPROC = "DI-WP", "Apprendre les bases du traitement de texte"
    DI_WORDS = "DI-WD", "Connaitre l’environnement et le vocabulaire numérique"

    EQ_APPLIANCE = "EQ_APPLIANCE", "Electroménager"
    EQ_CLOTH = "EQ_CLOTH", "Habillement"
    EQ_COMP = "EQ_COMP", "Accès à du matériel informatique"
    EQ_FOOD = "EQ_FOOD", "Alimentation"
    EQ_PHONE = "EQ_PHONE", "Accès à un téléphone et un abonnement"

    FA_CHILD = "FA_CHILD", "Garde d'enfants"
    FA_NOFAM = "FA_NOFAM", "Jeunes sans soutien familial"
    FA_PARENT = "FA_PARENT", "Information et accompagnement des parents"
    FA_SUPPORT = "FA_SUPPORT", "Soutien aux familles"
    FA_VIOLENCE = "FA_VIOLENCE", "Violences intrafamiliales"

    FI_ACCOUNT = "FI_ACCOUNT", "Création et utilisation d’un compte bancaire"
    FI_BUDGET = "FI_BUDGET", "Apprendre à gérer son budget"
    FI_DEBT = "FI_DEBT", "Prévention du surendettement"
    FI_HELP = "FI_HELP", "Accompagnement aux personnes en difficultés financières"

    FL_COM = "FL-CO", "Communiquer dans la vie de tous les jours"
    FL_FORMATION = "FL-FO", "Suivre une formation"
    FL_INSERTION = "FL-IN", "Accompagnement vers l’insertion professionnelle"

    HA_ACC = "HA_ACC", "Accompagnement par une structure spécialisée"
    HA_DESK = "HA_DESK", "Adaptation au poste de travail"
    HA_HOUSING = "HA_HOUSING", "Adapter son logement"
    HA_RECOG = "HA_RECOG", "Faire reconnaitre un handicap"
    HA_RIGHTS = "HA_RIGHTS", "Connaissance des droits des travailleurs"
    HA_WORK = "HA_WORK", "Favoriser le retour et le maintien dans l’emploi"

    HE_ADDICT = "HE_ADDICT", "Faire face à une situation d’addiction"
    HE_CURE = "HE_CURE", "Se soigner et prévenir la maladie"
    HE_EXPENSE = "HE_EXPENSE", "Obtenir la prise en charge de frais médicaux"
    HE_PSY = "HE_PSY", "Bien être psychologique"

    HO_ACCESS = "HO-AC", "Être accompagné(e) pour se loger"
    HO_ADAPT = "HO_AD", "Besoin d’adapter mon logement"
    HO_KEEP = "HO-KE", "Problème avec son logement"
    HO_MOVE = "HO_MO", "Déménagement"
    HO_SHORT = "HO-SH", "Mal logé/sans logis"
    HO_WORK = "HO_WK", "Reprendre un emploi ou une formation"

    IL_AUTONOMY = "IL_AUTONOMY", "Être autonome dans la vie de tous les jours"
    IL_CLEA = "IL_CLEA", "Valider une certification Cléa"
    IL_DEFECT = "IL_DEFECT", "Surmonter un trouble de l’apprentissage"
    IL_DETECT = "IL_DETECT", "Repérer des situations d’illettrisme"
    IL_DIGITAL = "IL_DIGITAL", "Savoir utiliser les outils numériques"
    IL_DRIVING = "IL_DRIVING", "Passer le permis de conduire"
    IL_INFO = "IL_INFO", "Être informé(e) sur l’acquisition des compétences de base"
    IL_JOB = "IL_JOB", "Trouver un emploi ou une formation"
    IL_SCHOOL = "IL_SCHOOL", "Accompagner la scolarité d’un enfant"
    IL_VOCAB = "IL_VOCAB", "Améliorer un niveau de vocabulaire"

    JO_CHOOSE = "JO_CHOOSE", "Choisir un métier"
    JO_FIND = "JO_FIND", "Trouver un emploi"
    JO_PREPARE = "JO_PREPARE", "Préparer sa candidature"

    MO_2WHEELS = "MO_2W", "Apprendre à utiliser un deux roues"
    MO_BLOCKS = "MO_BLK", "Identifier ses freins, et définir ses besoins en mobilité"
    MO_HELP = "MO_HLP", "Être accompagné(e) dans son parcours mobilité"
    MO_LICENSE = (
        "MO-LI",
        "Préparer son permis de conduire, se réentraîner à la conduite",
    )
    MO_MAINTENANCE = "MO-MA", "Entretenir ou réparer son véhicule"
    MO_MOBILITY = "MO-MO", "Se déplacer sans permis et/ou sans véhicule personnel"
    MO_VEHICLE = "MO-VE", "Louer ou acheter un véhicule"
    MO_WORK = "MO-WK", "Reprendre un emploi ou une formation"

    RE_EVAL = "RE_EVAL", "Identifier ses compétences et aptitudes"
    RE_SOCIAL = "RE_SOCIAL", "Lien social"
    RE_TRUST = "RE_TRUST", "Restaurer sa confiance, son image de soi"
    RE_WELLBEING = "RE_WELLBEING", "Bien être"

    RI_ADM_ACC = "RI_ADM_ACC", "Accompagnement dans les démarches administratives"
    RI_ASYLUM = "RI_ASYLUM", "Demandeurs d’asile et naturalisation"
    RI_JUD_ACC = "RI_JUD_ACC", "Accompagnement juridique"
    RI_KNOW = "RI_KNOW", "Connaitre ses droits"


class ServiceKind(models.TextChoices):
    FINANCIAL = "FI", "Aide financière"
    FORMATION = "FO", "Formation"
    INFORMATION = "IN", "Information"
    MATERIAL = "MA", "Aide materielle"
    RECEPTION = "RE", "Accueil"
    SUPPORT = "SU", "Accompagnement"
    WORKSHOP = "WK", "Atelier"


class BeneficiaryAccessMode(models.TextChoices):
    EMAIL = "EM", "Envoyer un mail"
    ONSITE = "OS", "Se présenter"
    OTHER = "OT", "Autre (préciser)"
    PHONE = "PH", "Téléphoner"


class CoachOrientationMode(models.TextChoices):
    EMAIL = "EM", "Envoyer un mail"
    EMAIL_PRESCRIPTION = "EP", "Envoyer un mail avec une fiche de prescription"
    FORM = "FO", "Envoyer le formulaire d’adhésion"
    OTHER = "OT", "Autre (préciser)"
    PHONE = "PH", "Téléphoner"


class LocationKind(models.TextChoices):
    ONSITE = "OS", "En présentiel"
    REMOTE = "RE", "À distance"
