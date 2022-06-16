# Generated by Django 4.0.4 on 2022-06-16 13:41

from django.db import migrations

from dora.services.enums import ServiceStatus


def migrate_statuses(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    for service in Service.objects.all():
        if service.is_model:
            service.status = None
        elif service.is_suggestion:
            service.status = ServiceStatus.SUGGESTION
        elif service.is_draft:
            service.status = ServiceStatus.DRAFT
        else:
            service.status = ServiceStatus.PUBLISHED
        service.save(update_fields=["status"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0054_service_status_and_more"),
    ]

    operations = [
        migrations.RunPython(migrate_statuses, reverse_code=migrations.RunPython.noop),
    ]
