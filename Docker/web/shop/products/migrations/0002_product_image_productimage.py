# Generated by Django 5.0.1 on 2024-03-23 05:36

import core.helpers
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="core_helpers.upload_handle",
                verbose_name="圖片",
            ),
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="商品圖片說明")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=core.helpers.upload_handle,
                        verbose_name="圖片",
                    ),
                ),
                ("order", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_image_set",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "商品圖片",
                "verbose_name_plural": "商品圖片",
                "ordering": ["order"],
            },
        ),
    ]
