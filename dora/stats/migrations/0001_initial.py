# Generated by Django 3.2.12 on 2022-03-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeploymentState",
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
                ("department_code", models.CharField(blank=True, max_length=3)),
                ("department_name", models.CharField(max_length=230)),
                (
                    "state",
                    models.IntegerField(
                        choices=[
                            (0, "Aucun contact"),
                            (1, "En cours d'échanges"),
                            (2, "Premières saisies de services"),
                            (3, "Déploiement en cours"),
                            (4, "Finalisation du déploiement"),
                        ],
                        default=0,
                        verbose_name="État de déploiement",
                    ),
                ),
            ],
            options={
                "verbose_name": "État de déploiement",
                "verbose_name_plural": "État de déploiement",
            },
        ),
    ]
