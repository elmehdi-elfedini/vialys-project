# Generated by Django 5.1.1 on 2024-11-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0010_alter_brand_name_alter_category_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="emballage",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
