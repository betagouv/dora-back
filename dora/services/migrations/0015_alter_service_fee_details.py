# Generated by Django 3.2.5 on 2021-08-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0014_alter_service_beneficiaries_access_modes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="fee_details",
            field=models.TextField(blank=True, verbose_name="Détail des frais"),
        ),
    ]