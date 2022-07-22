# Generated by Django 4.0.2 on 2022-05-02 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0035_rename_admitted_apply_admitted_apply_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='nickname',
            field=models.ForeignKey(default=profiles.models.CustomUser, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
