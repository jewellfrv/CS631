# Generated by Django 4.2.6 on 2023-10-20 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_inpatient_treatment_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalhistory',
            old_name='illness_id',
            new_name='illness',
        ),
        migrations.RenameField(
            model_name='medicalhistory',
            old_name='SSN',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='SSN',
            new_name='patient',
        ),
        migrations.RemoveField(
            model_name='request',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='request',
            name='request_id',
        ),
        migrations.AddField(
            model_name='request',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.doctor'),
        ),
        migrations.AddField(
            model_name='request',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='treatment_type',
            field=models.CharField(choices=[('General', 'General'), ('Surgery', 'Surgery')], default='General', max_length=20),
        ),
    ]