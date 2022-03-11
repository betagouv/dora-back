# Generated by Django 3.2.12 on 2022-03-08 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0045_migrate_enums"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="beneficiaries_access_modes",
        ),
        migrations.RemoveField(
            model_name="service",
            name="category",
        ),
        migrations.RemoveField(
            model_name="service",
            name="coach_orientation_modes",
        ),
        migrations.RemoveField(
            model_name="service",
            name="kinds",
        ),
        migrations.RemoveField(
            model_name="service",
            name="location_kinds",
        ),
        migrations.RemoveField(
            model_name="service",
            name="subcategories",
        ),
        migrations.RenameModel(
            old_name="BeneficiaryAccessMode2",
            new_name="BeneficiaryAccessMode",
        ),
        migrations.RenameModel(
            old_name="CoachOrientationMode2",
            new_name="CoachOrientationMode",
        ),
        migrations.RenameModel(
            old_name="LocationKind2",
            new_name="LocationKind",
        ),
        migrations.RenameModel(
            old_name="ServiceCategories2",
            new_name="ServiceCategory",
        ),
        migrations.RenameModel(
            old_name="ServiceKind2",
            new_name="ServiceKind",
        ),
        migrations.RenameModel(
            old_name="ServiceSubCategories2",
            new_name="ServiceSubCategory",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="beneficiaries_access_modes2",
            new_name="beneficiaries_access_modes",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="categories2",
            new_name="categories",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="coach_orientation_modes2",
            new_name="coach_orientation_modes",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="kinds2",
            new_name="kinds",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="location_kinds2",
            new_name="location_kinds",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="subcategories2",
            new_name="subcategories",
        ),
    ]
