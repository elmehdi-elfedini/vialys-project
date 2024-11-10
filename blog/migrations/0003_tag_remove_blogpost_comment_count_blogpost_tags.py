# Generated by Django 4.2.16 on 2024-10-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_blogpost_comment_count_blogpost_published_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="comment_count",
        ),
        migrations.AddField(
            model_name="blogpost",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="blog_posts", to="blog.tag"
            ),
        ),
    ]
