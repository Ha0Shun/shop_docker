# Generated by Django 5.0.1 on 2024-05-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0006_delete_relationalproduct"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="product_counts",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="product_names",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("未付款", "未付款"),
                    ("付款失敗", "付款失敗"),
                    ("付款成功", "付款成功"),
                    ("取消", "取消"),
                ],
                default="未付款",
                max_length=100,
                verbose_name="訂單狀態",
            ),
        ),
    ]
