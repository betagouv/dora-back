# Generated by Django 3.2.12 on 2022-03-01 18:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0041_newcategories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="beneficiaries_access_modes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("EM", "Envoyer un mail"),
                        ("OS", "Se présenter"),
                        ("OT", "Autre (préciser)"),
                        ("PH", "Téléphoner"),
                    ],
                    max_length=2,
                ),
                blank=True,
                default=list,
                size=None,
                verbose_name="Comment mobiliser la solution en tant que bénéficiaire",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("CR", "Création d’activité"),
                    ("DI", "Numérique"),
                    ("EQ", "Equipement et alimentation"),
                    ("FA", "Famille"),
                    ("FL", "Apprendre le Français"),
                    ("FI", "Difficultés financières"),
                    ("GL", "Acco. global individualisé"),
                    ("HA", "Handicap"),
                    ("HE", "Santé"),
                    ("HO", "Logement – Hébergement"),
                    ("IL", "Illettrisme"),
                    ("JO", "Emploi"),
                    ("MO", "Mobilité"),
                    ("RE", "Remobilisation"),
                    ("RI", "Accès aux droits & citoyenneté"),
                ],
                db_index=True,
                max_length=2,
                verbose_name="Catégorie principale",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="coach_orientation_modes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("EM", "Envoyer un mail"),
                        ("EP", "Envoyer un mail avec une fiche de prescription"),
                        ("FO", "Envoyer le formulaire d’adhésion"),
                        ("OT", "Autre (préciser)"),
                        ("PH", "Téléphoner"),
                    ],
                    max_length=2,
                ),
                blank=True,
                default=list,
                size=None,
                verbose_name="Comment orienter un bénéficiaire en tant qu’accompagnateur",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="kinds",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("FI", "Aide financière"),
                        ("FO", "Formation"),
                        ("IN", "Information"),
                        ("MA", "Aide materielle"),
                        ("RE", "Accueil"),
                        ("SU", "Accompagnement"),
                        ("WK", "Atelier"),
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
        migrations.AlterField(
            model_name="service",
            name="subcategories",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("CR-EL", "Élaborer son projet"),
                        ("CR-ID", "De l’idée au projet"),
                        ("CR-ST", "Démarrer son activité"),
                        ("DI-AD", "Réaliser une démarche en ligne"),
                        ("DI-BA", "Prendre en main un équipement informatique"),
                        ("DI-CH", "Accompagner son enfant"),
                        ("DI-CO", "Échanger avec ses proches"),
                        ("DI-CN", "Créer et gérer ses contenus numériques"),
                        ("DI-EM", "Envoyer, recevoir, gérer ses courriels"),
                        ("DI-JO", "Trouver un emploi ou une formation"),
                        ("DI-NA", "Naviguer sur internet"),
                        ("DI-PH", "Utiliser son smartphone"),
                        ("DI-WP", "Apprendre les bases du traitement de texte"),
                        (
                            "DI-WD",
                            "Connaitre l’environnement et le vocabulaire numérique",
                        ),
                        ("EQ_APPLIANCE", "Electroménager"),
                        ("EQ_CLOTH", "Habillement"),
                        ("EQ_COMP", "Accès à du matériel informatique"),
                        ("EQ_FOOD", "Alimentation"),
                        ("EQ_PHONE", "Accès à un téléphone et un abonnement"),
                        ("FA_CHILD", "Garde d'enfants"),
                        ("FA_NOFAM", "Jeunes sans soutien familial"),
                        ("FA_PARENT", "Information et accompagnement des parents"),
                        ("FA_SUPPORT", "Soutien aux familles"),
                        ("FA_VIOLENCE", "Violences intrafamiliales"),
                        ("FI_ACCOUNT", "Création et utilisation d’un compte bancaire"),
                        ("FI_BUDGET", "Apprendre à gérer son budget"),
                        ("FI_DEBT", "Prévention du surendettement"),
                        (
                            "FI_HELP",
                            "Accompagnement aux personnes en difficultés financières",
                        ),
                        ("FL-CO", "Communiquer dans la vie de tous les jours"),
                        ("FL-FO", "Suivre une formation"),
                        ("FL-IN", "Accompagnement vers l’insertion professionnelle"),
                        ("HA_ACC", "Accompagnement par une structure spécialisée"),
                        ("HA_DESK", "Adaptation au poste de travail"),
                        ("HA_HOUSING", "Adapter son logement"),
                        ("HA_RECOG", "Faire reconnaitre un handicap"),
                        ("HA_RIGHTS", "Connaissance des droits des travailleurs"),
                        ("HA_WORK", "Favoriser le retour et le maintien dans l’emploi"),
                        ("HE_ADDICT", "Faire face à une situation d’addiction"),
                        ("HE_CURE", "Se soigner et prévenir la maladie"),
                        ("HE_EXPENSE", "Obtenir la prise en charge de frais médicaux"),
                        ("HE_PSY", "Bien être psychologique"),
                        ("HO-AC", "Être accompagné(e) pour se loger"),
                        ("HO_AD", "Besoin d’adapter mon logement"),
                        ("HO-KE", "Problème avec son logement"),
                        ("HO_MO", "Déménagement"),
                        ("HO-SH", "Mal logé/sans logis"),
                        ("HO_WK", "Reprendre un emploi ou une formation"),
                        ("IL_AUTONOMY", "Être autonome dans la vie de tous les jours"),
                        ("IL_CLEA", "Valider une certification Cléa"),
                        ("IL_DEFECT", "Surmonter un trouble de l’apprentissage"),
                        ("IL_DETECT", "Repérer des situations d’illettrisme"),
                        ("IL_DIGITAL", "Savoir utiliser les outils numériques"),
                        ("IL_DRIVING", "Passer le permis de conduire"),
                        (
                            "IL_INFO",
                            "Être informé(e) sur l’acquisition des compétences de base",
                        ),
                        ("IL_JOB", "Trouver un emploi ou une formation"),
                        ("IL_SCHOOL", "Accompagner la scolarité d’un enfant"),
                        ("IL_VOCAB", "Améliorer un niveau de vocabulaire"),
                        ("JO_CHOOSE", "Choisir un métier"),
                        ("JO_FIND", "Trouver un emploi"),
                        ("JO_PREPARE", "Préparer sa candidature"),
                        ("MO_2W", "Apprendre à utiliser un deux roues"),
                        (
                            "MO_BLK",
                            "Identifier ses freins, et définir ses besoins en mobilité",
                        ),
                        ("MO_HLP", "Être accompagné(e) dans son parcours mobilité"),
                        (
                            "MO-LI",
                            "Préparer son permis de conduire, se réentraîner à la conduite",
                        ),
                        ("MO-MA", "Entretenir ou réparer son véhicule"),
                        (
                            "MO-MO",
                            "Se déplacer sans permis et/ou sans véhicule personnel",
                        ),
                        ("MO-VE", "Louer ou acheter un véhicule"),
                        ("MO-WK", "Reprendre un emploi ou une formation"),
                        ("RE_EVAL", "Identifier ses compétences et aptitudes"),
                        ("RE_SOCIAL", "Lien social"),
                        ("RE_TRUST", "Restaurer sa confiance, son image de soi"),
                        ("RE_WELLBEING", "Bien être"),
                        (
                            "RI_ADM_ACC",
                            "Accompagnement dans les démarches administratives",
                        ),
                        ("RI_ASYLUM", "Demandeurs d’asile et naturalisation"),
                        ("RI_JUD_ACC", "Accompagnement juridique"),
                        ("RI_KNOW", "Connaitre ses droits"),
                    ],
                    max_length=100,
                ),
                blank=True,
                default=list,
                size=None,
                verbose_name="Sous-catégorie",
            ),
        ),
    ]