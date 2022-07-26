# Generated by Django 4.0.2 on 2022-04-15 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_courses_taken_course1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses_taken',
            name='course10',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course10', to='profiles.allcourses'),
        ),
        migrations.AddField(
            model_name='courses_taken',
            name='course3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course3', to='profiles.allcourses'),
        ),
        migrations.AddField(
            model_name='courses_taken',
            name='course4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course4', to='profiles.allcourses'),
        ),
        migrations.AddField(
            model_name='courses_taken',
            name='course5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course5', to='profiles.allcourses'),
        ),
        migrations.AddField(
            model_name='courses_taken',
            name='course6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course6', to='profiles.allcourses'),
        ),
        migrations.AddField(
            model_name='courses_taken',
            name='course7',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course7', to='profiles.allcourses'),
        ),
        migrations.AddField(
            model_name='courses_taken',
            name='course8',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course8', to='profiles.allcourses'),
        ),
        migrations.AddField(
            model_name='courses_taken',
            name='course9',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course9', to='profiles.allcourses'),
        ),
        migrations.AlterField(
            model_name='courses_taken',
            name='course1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course1', to='profiles.allcourses'),
        ),
        migrations.AlterField(
            model_name='courses_taken',
            name='course2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course2', to='profiles.allcourses'),
        ),
    ]
