# Generated by Django 2.2.11 on 2020-08-11 05:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0162_auto_20200811_1101"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalpatientregistration",
            name="address_old",
        ),
        migrations.RemoveField(
            model_name="historicalpatientregistration",
            name="name_old",
        ),
        migrations.RemoveField(
            model_name="historicalpatientregistration",
            name="phone_number_old",
        ),
        migrations.RemoveField(
            model_name="patientregistration",
            name="address_old",
        ),
        migrations.RemoveField(
            model_name="patientregistration",
            name="name_old",
        ),
        migrations.RemoveField(
            model_name="patientregistration",
            name="phone_number_old",
        ),
    ]
