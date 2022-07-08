# Generated by Django 3.2.13 on 2022-06-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sequences", "0037_auto_20220520_0129"),
    ]

    operations = [
        migrations.AlterField(
            model_name="condition",
            name="days",
            field=models.IntegerField(
                default=1,
                verbose_name="Amount of days before/after new hire has started",
            ),
        ),
    ]
