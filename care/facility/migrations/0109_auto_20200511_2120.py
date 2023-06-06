# Generated by Django 2.2.11 on 2020-05-11 15:50

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0108_auto_20200510_1612"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientsearch",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="patientsearch",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="patientsearch",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name="patientsearch",
            name="modified_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="ambulance",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="ambulancedriver",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="building",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="facility",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="facilitycapacity",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="facilitypatientstatshistory",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="facilitystaff",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="facilityvolunteer",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="hospitaldoctors",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="inventorylog",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="patientconsultation",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="patientregistration",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="patientsample",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="patientsampleflow",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="room",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="staffroomallocation",
            name="external_id",
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
    ]
