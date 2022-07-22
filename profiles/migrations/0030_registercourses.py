# Generated by Django 4.0.2 on 2022-04-23 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0029_exam_teacher_username_alter_studentdata_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.ManyToManyField(to='profiles.Allcourses')),
                ('my_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
