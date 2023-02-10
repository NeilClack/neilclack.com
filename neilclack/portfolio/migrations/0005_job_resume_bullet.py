# Generated by Django 4.1.6 on 2023-02-10 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0004_alter_project_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("company", models.CharField(max_length=120)),
                ("title", models.CharField(max_length=120)),
                ("start", models.DateField()),
                ("end", models.DateField(blank=True, null=True)),
                ("current", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Resume",
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
                ("name", models.CharField(max_length=120)),
                ("title", models.CharField(max_length=120)),
                ("download", models.FileField(upload_to="resume")),
            ],
        ),
        migrations.CreateModel(
            name="Bullet",
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
                ("bullet", models.TextField()),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="portfolio.job"
                    ),
                ),
            ],
        ),
    ]
