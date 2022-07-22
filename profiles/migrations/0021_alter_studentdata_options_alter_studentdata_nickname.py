# Generated by Django 4.0.2 on 2022-04-18 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_alter_studentdata_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentdata',
            options={'ordering': ['nickname'], 'verbose_name': 'student datum', 'verbose_name_plural': 'students data'},
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='nickname',
            field=models.ForeignKey(default=profiles.models.CustomUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]