# Generated by Django 4.2.7 on 2023-12-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0005_alter_order_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="charge",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]