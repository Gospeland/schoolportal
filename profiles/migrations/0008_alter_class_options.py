# Generated by Django 4.0.2 on 2022-04-15 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_class_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['class_name'], 'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
    ]
