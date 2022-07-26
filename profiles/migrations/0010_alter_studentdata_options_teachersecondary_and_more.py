# Generated by Django 4.0.2 on 2022-04-15 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_level_alter_studentdata_student_class_delete_class'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentdata',
            options={'ordering': ['nickname'], 'verbose_name': 'student datum', 'verbose_name_plural': 'students data'},
        ),
        migrations.CreateModel(
            name='TeacherSecondary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_handled', models.ManyToManyField(to='profiles.Level')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.departments')),
                ('staff_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.staffdata')),
                ('subjects_taught', models.ManyToManyField(to='profiles.Allcourses')),
            ],
            options={
                'verbose_name': 'Secondary  Class Teacher',
                'verbose_name_plural': 'Secondary Class Teachers',
            },
        ),
        migrations.CreateModel(
            name='Teacherprimary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.form')),
                ('class_handled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.level')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.departments')),
                ('staff_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.staffdata')),
                ('subjects_taught', models.ManyToManyField(to='profiles.Allcourses')),
            ],
            options={
                'verbose_name': 'Primary Class Teacher',
                'verbose_name_plural': 'Primary Class Teachers',
                'ordering': ['class_handled'],
            },
        ),
    ]
