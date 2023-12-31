# Generated by Django 4.2.6 on 2023-10-20 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_illness_medicalhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='illness',
            name='illness_id',
        ),
        migrations.RemoveField(
            model_name='medicalhistory',
            name='illness_id',
        ),
        migrations.AddField(
            model_name='illness',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('request_id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('request_date', models.DateField()),
                ('SSN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.patient')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.doctor')),
            ],
        ),
    ]
