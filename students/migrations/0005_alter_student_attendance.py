# Generated by Django 5.2 on 2025-04-19 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='attendance',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
