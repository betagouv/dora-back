# Generated by Django 4.0.6 on 2022-07-14 11:08

from django.db import migrations


def cleanup_concerned_public(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    ConcernedPublic = apps.get_model("services", "ConcernedPublic")

    try:
        value_to_keep = ConcernedPublic.objects.get(
            name="Bénéficiaire de l'Allocation Spécifique de Solidarité (ASS)"
        )
        value_to_remove = ConcernedPublic.objects.get(
            name="Bénéficiaires de l'Allocation de Solidarité Spécifique"
        )

        services_with_only_value_to_remove = Service.objects.filter(
            concerned_public=value_to_remove
        ).exclude(concerned_public=value_to_keep)
        for service in services_with_only_value_to_remove:
            service.concerned_public.add(value_to_keep)
        value_to_remove.delete()
    except ConcernedPublic.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0059_service_last_draft_notification_date"),
    ]

    operations = [
        migrations.RunPython(
            cleanup_concerned_public, reverse_code=migrations.RunPython.noop
        )
    ]