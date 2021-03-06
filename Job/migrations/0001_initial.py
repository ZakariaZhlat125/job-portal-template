# Generated by Django 4.0.4 on 2022-05-03 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1500)),
                ('date', models.DateTimeField(auto_now=True)),
                ('workplace_type', models.CharField(choices=[('onsite', 'On-site'), ('hybrid', 'Hybrid'), ('remote', 'Remote')], default='onsite', max_length=32)),
                ('employment_type', models.CharField(choices=[('full_time', 'Full time'), ('part_time', 'Part time'), ('contract', 'Contract'), ('temporary', 'Temporary'), ('volenteer', 'Volenteer'), ('internshp', 'Internship')], default='full_time', max_length=25)),
                ('experience', models.CharField(max_length=400)),
                ('skills', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('job_function', models.CharField(max_length=200)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'unique_together': {('user', 'job')},
            },
        ),
    ]
