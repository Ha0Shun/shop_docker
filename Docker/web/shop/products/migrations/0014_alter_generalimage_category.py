# Generated by Django 5.0.1 on 2024-11-17 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0013_alter_generalimage_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generalimage",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="Image_set",
                to="products.productcategory",
                verbose_name="品牌分類",
            ),
        ),
    ]
