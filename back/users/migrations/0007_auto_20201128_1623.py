# Generated by Django 3.1.2 on 2020-11-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_preboardinguser_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preboardinguser",
            name="order",
            field=models.IntegerField(default=0),
        ),
    ]
