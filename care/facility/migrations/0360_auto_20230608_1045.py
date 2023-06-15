# Generated by Django 2.2.11 on 2023-06-08 05:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0359_auto_20230529_1907"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fileupload",
            name="file_type",
            field=models.IntegerField(
                choices=[
                    (1, "PATIENT"),
                    (2, "CONSULTATION"),
                    (3, "SAMPLE_MANAGEMENT"),
                    (4, "CLAIM"),
                    (5, "DISCHARGE_SUMMARY"),
                    (6, "COMMUNICATION"),
                ],
                default=1,
            ),
        ),
    ]
