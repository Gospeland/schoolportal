# Generated by Django 4.0.2 on 2022-04-18 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_customuser_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_teacher',
        ),
    ]
