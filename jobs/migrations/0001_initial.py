# Generated by Django 4.2.11 on 2024-03-18 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[('10:00 - 11:00', '10:00 - 11:00'), ('11:00 - 12:00', '11:00 - 12:00'), ('12:00 - 13:00', '12:00 - 13:00'), ('13:00 - 14:00', '13:00 - 14:00'), ('14:00 - 15:00', '14:00 - 15:00'), ('15:00 - 16:00', '15:00 - 16:00')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('cv', models.FileField(blank=True, upload_to='cv/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_benefits', models.TextField()),
                ('address', models.CharField(max_length=60)),
                ('job_details', models.TextField()),
                ('job_requirements', models.TextField()),
                ('interview_date', models.DateField(blank=True, null=True)),
                ('hired', models.BooleanField()),
                ('available_times', models.ManyToManyField(related_name='jobs', to='jobs.availabletime')),
            ],
        ),
    ]
