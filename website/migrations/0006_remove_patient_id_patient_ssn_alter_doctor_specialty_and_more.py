# Generated by Django 4.2.6 on 2023-10-06 23:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_doctor_specialty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AddField(
            model_name='patient',
            name='SSN',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxValueValidator(999999999)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(choices=[('General', 'General'), ('Pediatrics', 'Pediatrics'), ('Dermatology', 'Dermatology'), ('Surgery', 'Surgery'), ('Oncology', 'Oncology')], max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]
