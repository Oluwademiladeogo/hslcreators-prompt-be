# Generated by Django 4.2.7 on 2023-12-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0005_alter_printer_id_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="printer",
            name="average_rating",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=3, null=True
            ),
        ),
    ]
