# Generated by Django 5.0.1 on 2024-06-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_productoption"),
    ]

    operations = [
        migrations.AddField(
            model_name="relationalproduct",
            name="size",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="尺寸"
            ),
        ),
    ]
