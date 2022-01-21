# Generated by Django 3.2 on 2022-01-21 16:32

from django.db import migrations, models

import file_field_utils.db.fields
import file_field_utils.db.utils.backend


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=64, verbose_name="Title")),
                (
                    "image",
                    file_field_utils.db.fields.SVGAndImageField(
                        blank=True,
                        upload_to=file_field_utils.db.utils.backend.UploadPath(""),
                        verbose_name="Image",
                    ),
                ),
                (
                    "image_1",
                    file_field_utils.db.fields.SVGAndImageField(
                        blank=True,
                        upload_to=file_field_utils.db.utils.backend.UploadPath(
                            "example_dir"
                        ),
                        verbose_name="Image 1",
                    ),
                ),
                (
                    "image_2",
                    file_field_utils.db.fields.SVGAndImageField(
                        blank=True,
                        upload_to=file_field_utils.db.utils.backend.UploadPathWithID(
                            ""
                        ),
                        verbose_name="Image 2",
                    ),
                ),
                (
                    "image_3",
                    file_field_utils.db.fields.SVGAndImageField(
                        blank=True,
                        upload_to=file_field_utils.db.utils.backend.UploadPathWithID(
                            "example_dir"
                        ),
                        verbose_name="Image 3",
                    ),
                ),
            ],
            options={
                "verbose_name": "News",
                "verbose_name_plural": "News",
            },
        ),
    ]
