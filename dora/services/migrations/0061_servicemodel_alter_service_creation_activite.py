# Generated by Django 4.0.4 on 2022-06-27 22:02

from django.db import migrations

from dora.services.migration_utils import (
    delete_subcategory,
    replace_subcategory,
    update_subcategory_label,
    update_subcategory_slug,
)

"""
-- Avant: 15 => Après : 15
SELECT COUNT(*) from services_servicecategory;

-- Avant : 4 (3+ 1 autre) => Après: 3 (2+1 autre)
SELECT * FROM services_servicesubcategory WHERE "value" LIKE 'creation-activite--%';

-- Avant : 3 => Après: 0
SELECT COUNT(*) FROM services_servicesubcategory WHERE "value" IN ('creation-activite--de-lidee-au-projet','creation-activite--demarrer-activite', 'creation-activite--elaborer-projet');
-- Avant : 1 & 1 & 1 => Après: 0 & 0 & 0
SELECT COUNT(*) FROM services_servicesubcategory WHERE "label" LIKE 'De l’idée au projet';
SELECT COUNT(*) FROM services_servicesubcategory WHERE "label" LIKE 'Démarrer son activité';
SELECT COUNT(*) FROM services_servicesubcategory WHERE "label" LIKE 'Élaborer son projet';


-- Avant : 0 => Après : 1
SELECT COUNT(*) FROM services_servicesubcategory WHERE "label" LIKE 'Définir son projet de création d’entreprise';
SELECT COUNT(*) FROM services_servicesubcategory WHERE "label" LIKE 'Structurer son projet de création d’entreprise';

-- Avant 0 => après 2
SELECT COUNT(*) FROM services_servicesubcategory WHERE "value" IN ('creation-activite--structurer-son-projet-de-creation-dentreprise','creation-activite--definir-son-projet-de-creation-dentreprise');


-- Avant 32 => Après 0
SELECT COUNT(*) FROM services_service_subcategories WHERE servicesubcategory_id = (SELECT id FROM services_servicesubcategory WHERE "value" = 'creation-activite--de-lidee-au-projet');
-- Avant 0 => Après 32
SELECT COUNT(*) FROM services_service_subcategories WHERE servicesubcategory_id = (SELECT id FROM services_servicesubcategory WHERE "value" = 'creation-activite--definir-son-projet-de-creation-dentreprise');
SELECT * FROM services_servicesubcategory WHERE "value" = 'creation-activite--definir-son-projet-de-creation-dentreprise';


-- Avant 49 => Après 0
SELECT COUNT(DISTINCT(service_id)) FROM services_service_subcategories WHERE servicesubcategory_id IN (SELECT id FROM services_servicesubcategory WHERE "value" = 'creation-activite--demarrer-activite' OR value = 'creation-activite--elaborer-projet');

-- Avant 0 => après 49
SELECT COUNT(*) FROM services_service_subcategories WHERE servicesubcategory_id = (SELECT id FROM services_servicesubcategory WHERE "value" = 'creation-activite--structurer-son-projet-de-creation-dentreprise');
"""


def migrate_services_options(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    ServiceSubCategory = apps.get_model("services", "ServiceSubCategory")

    # 1 - Création d’activité :
    """
    1:
    - Renommer slug "creation-activite--demarrer-activite" en "creation-activite--structurer-son-projet-de-creation-dentreprise"
    - Renommer label de "creation-activite--structurer-son-projet-de-creation-dentreprise" en "Structurer son projet de création d’entreprise"
    - Remplacer toutes les références à "creation-activite--elaborer-projet" vers "creation-activite--structurer-son-projet-de-creation-dentreprise"
    - Supprimer "creation-activite--elaborer-projet"
    """
    creation_activite_slug = "creation-activite"
    update_subcategory_slug(
        ServiceSubCategory,
        old_slug=f"{creation_activite_slug}--demarrer-activite",
        new_slug=f"{creation_activite_slug}--structurer-son-projet-de-creation-dentreprise",
    )
    update_subcategory_label(
        ServiceSubCategory,
        slug=f"{creation_activite_slug}--structurer-son-projet-de-creation-dentreprise",
        new_label="Structurer son projet de création d’entreprise",
    )
    replace_subcategory(
        ServiceSubCategory,
        Service,
        from_slug=f"{creation_activite_slug}--elaborer-projet",
        to_slug=f"{creation_activite_slug}--structurer-son-projet-de-creation-dentreprise",
    )
    delete_subcategory(
        ServiceSubCategory, slug=f"{creation_activite_slug}--elaborer-projet"
    )

    """
        2:
        - Renommer value "creation-activite--de-lidee-au-projet" en "creation-activite--definir-son-projet-de-creation-dentreprise"
        - Renommer label "creation-activite--definir-son-projet-de-creation-dentreprise" en "Définir son projet de création d’entreprise"
    """
    update_subcategory_slug(
        ServiceSubCategory,
        old_slug=f"{creation_activite_slug}--de-lidee-au-projet",
        new_slug=f"{creation_activite_slug}--definir-son-projet-de-creation-dentreprise",
    )
    update_subcategory_label(
        ServiceSubCategory,
        slug=f"{creation_activite_slug}--definir-son-projet-de-creation-dentreprise",
        new_label="Définir son projet de création d’entreprise",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0060_Cleanup"),
    ]

    operations = [
        migrations.RunPython(
            migrate_services_options, reverse_code=migrations.RunPython.noop
        ),
    ]
