# Generated by Django 4.2.2 on 2023-06-22 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ref_Video",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=20)),
                ("singer", models.CharField(default=None, max_length=10)),
                (
                    "video_file",
                    models.FileField(
                        default=datetime.datetime.now, upload_to="ref_video/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Video",
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
                (
                    "video_file",
                    models.FileField(
                        default=datetime.datetime.now, upload_to="challenge_upload/"
                    ),
                ),
                ("ref_id", models.IntegerField(default=0)),
            ],
        ),
    ]
