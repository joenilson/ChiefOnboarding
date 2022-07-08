# Generated by Django 3.2.13 on 2022-07-04 18:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sequences", "0038_alter_condition_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pendingadmintask",
            name="assigned_to",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assigned_user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Pick user",
            ),
        ),
    ]
