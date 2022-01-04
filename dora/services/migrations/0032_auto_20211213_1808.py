# Generated by Django 3.2.10 on 2021-12-13 17:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0031_alter_service_suspension_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("MO", "Mobilité"),
                    ("HO", "Logement – Hébergement"),
                    ("CC", "Garde d’enfant"),
                    ("FL", "Apprendre le Français"),
                    ("IL", "Illettrisme"),
                    ("CR", "Création d’activité"),
                    ("DI", "Numérique"),
                    ("FI", "Difficultés financières"),
                    ("GL", "Accompagnement global individualisé"),
                ],
                db_index=True,
                max_length=2,
                verbose_name="Catégorie principale",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="kinds",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("MA", "Aide materielle"),
                        ("FI", "Aide financière"),
                        ("SU", "Accompagnement"),
                        ("FO", "Formation"),
                        ("IN", "Information"),
                        ("RE", "Accueil"),
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
                        (
                            "MO-MO",
                            "Se déplacer sans permis et/ou sans véhicule personnel",
                        ),
                        ("MO-WK", "Reprendre un emploi ou une formation"),
                        (
                            "MO-LI",
                            "Préparer son permis de conduire, se réentraîner à la conduite",
                        ),
                        ("MO-VE", "Louer ou acheter un véhicule"),
                        ("MO-MA", "Entretenir ou réparer son véhicule"),
                        ("MO_2W", "Apprendre à utiliser un deux roues"),
                        (
                            "MO_BLK",
                            "Identifier ses freins, et définir ses besoins en mobilité",
                        ),
                        ("MO_HLP", "Être accompagné(e) dans son parcours mobilité"),
                        ("HO_AD", "Besoin d’adapter mon logement"),
                        ("HO-KE", "Problème avec son logement"),
                        ("HO-SH", "Mal logé/sans logis"),
                        ("HO_MO", "Déménagement"),
                        ("HO-AC", "Être accompagné(e) pour se loger"),
                        ("HO_WK", "Reprendre un emploi ou une formation"),
                        ("CC-IN", "Information et accompagnement des parents"),
                        ("CC-TM", "Garde ponctuelle"),
                        ("CC-LG", "Garde pérenne"),
                        ("CC-EX", "Garde périscolaire"),
                        ("FL-CO", "Communiquer dans la vie de tous les jours"),
                        ("FL-IN", "Accompagnement vers l’insertion professionnelle"),
                        ("FL-FO", "Suivre une formation"),
                        ("IL-CO", "Communiquer dans la vie de tous les jours"),
                        ("IL-IN", "Accompagnement vers l’insertion professionnelle"),
                        ("IL-FO", "Suivre une formation"),
                        ("IL-AD", "Être informé sur les  démarches administratives"),
                        ("CR-ID", "De l’idée au projet"),
                        ("CR-EL", "Élaborer son projet"),
                        ("CR-ST", "Démarrer son activité"),
                        ("DI-BA", "Prendre en main un équipement informatique"),
                        ("DI-NA", "Naviguer sur internet"),
                        ("DI-EM", "Envoyer, recevoir, gérer ses courriels"),
                        ("DI-PH", "Utiliser son smartphone"),
                        ("DI-CN", "Créer et gérer ses contenus numériques"),
                        (
                            "DI-WD",
                            "Connaitre l’environnement et le vocabulaire numérique",
                        ),
                        ("DI-WP", "Apprendre les bases du traitement de texte"),
                        ("DI-CO", "Échanger avec ses proches"),
                        ("DI-JO", "Trouver un emploi ou une formation"),
                        ("DI-CH", "Accompagner son enfant"),
                        ("DI-AD", "Réaliser une démarche en ligne"),
                    ],
                    max_length=6,
                ),
                blank=True,
                default=list,
                size=None,
                verbose_name="Sous-catégorie",
            ),
        ),
    ]