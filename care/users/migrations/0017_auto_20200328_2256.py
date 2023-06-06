# Generated by Django 2.2.11 on 2020-03-28 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0016_auto_20200327_1954"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="new_district",
        ),
        migrations.AddField(
            model_name="user",
            name="local_body",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="users.LocalBody",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="state",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to="users.State"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="district",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="users.District",
            ),
        ),
    ]
