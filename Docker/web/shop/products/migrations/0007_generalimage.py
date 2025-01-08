# Generated by Django 5.0.1 on 2024-11-15 19:35

import core.helpers
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_remove_relationalproduct_size"),
    ]

    operations = [
        migrations.CreateModel(
            name="GeneralImage",
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
                ("name", models.CharField(max_length=50, verbose_name="圖片名稱")),
                (
                    "image",
                    models.ImageField(
                        upload_to=core.helpers.upload_handle, verbose_name="圖片"
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("carousel", "輪播圖片"),
                            ("banner", "橫幅圖片"),
                            ("thumbnail", "縮略圖"),
                            ("other", "其他"),
                        ],
                        default="other",
                        max_length=20,
                        verbose_name="圖片分類",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="圖片描述"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="建立日期"),
                ),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="修改日期")),
                ("is_active", models.BooleanField(default=True, verbose_name="是否啟用")),
            ],
            options={
                "verbose_name": "通用圖片",
                "verbose_name_plural": "通用圖片",
                "ordering": ["-created"],
            },
        ),
    ]