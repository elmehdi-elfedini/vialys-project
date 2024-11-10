# Generated by Django 4.2.16 on 2024-11-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0015_alter_teammember_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teammember",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="phone1",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="priority",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="role",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
