# Generated by Django 3.0 on 2020-03-16 22:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gazette",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("crawled_at", models.DateTimeField()),
                ("crawled_from", models.URLField()),
                ("notes", models.TextField(blank=True, null=True)),
                ("date", models.DateField(null=True)),
                (
                    "power",
                    models.CharField(
                        choices=[
                            ("executivo", "Poder Executivo"),
                            ("legislativo", "Poder Legislativo"),
                        ],
                        max_length=25,
                    ),
                ),
                ("year_and_edition", models.CharField(max_length=100)),
                ("is_legacy", models.BooleanField(default=False)),
                ("file_url", models.URLField(blank=True, null=True)),
                ("file_content", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="citycouncilagenda",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="citycouncilagenda",
            name="crawled_at",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="citycouncilagenda",
            name="crawled_from",
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="GazetteEvent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("crawled_at", models.DateTimeField()),
                ("crawled_from", models.URLField()),
                ("notes", models.TextField(blank=True, null=True)),
                ("title", models.CharField(blank=True, max_length=300, null=True)),
                (
                    "secretariat",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("summary", models.TextField(blank=True, null=True)),
                (
                    "published_on",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "gazette",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datasets.Gazette",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]