# Generated by Django 5.2 on 2025-04-19 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='full_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
    ]
