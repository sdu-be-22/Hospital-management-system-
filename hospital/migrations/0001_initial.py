# Generated by Django 4.0.2 on 2022-05-04 20:49

import datetime
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
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
                ('doctor', models.CharField(choices=[('Aruzhan Askar', 'Aruzhan Askar'), ('Dosbol Bekgali', 'Dosbol Bekgali'), ('Nick Adel', 'Nick Adel'), ('Lucy Andro', 'Lucy Andro'), ('Aleksey Sergey', 'Aleksey Sergey'), ('Nikolas Spark', 'Nikolas Spark'), ('Samat Kozhagul', 'Samat Kozhagul'), ('Alma Serikkyzy', 'Alma Serikkyzy')], default='Doctor1', max_length=30, null=True)),
                ('email', models.EmailField(max_length=20)),
                ('app_date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('Not Completed', 'Not Completed'), ('Completed', 'Completed'), ('Canceled', 'Canceled'), ('Postponed', 'Postponed')], default='Not Completed', max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=1000000)),
                ('room', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=40)),
                ('last_name', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
                ('mobile', models.CharField(max_length=20)),
                ('mod_date', models.DateField(default=datetime.date.today)),
                ('status', models.BooleanField(default=False)),
                ('blood_pressure', models.IntegerField(default=0)),
                ('heart_beat', models.IntegerField(default=0)),
                ('haemoglobin', models.IntegerField(default=0)),
                ('sugar', models.IntegerField(default=0)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/')),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('status', models.BooleanField(default=False)),
                ('university', models.CharField(default='', max_length=500)),
                ('experience', models.CharField(default='', max_length=500)),
                ('awards', models.CharField(default='', max_length=500)),
                ('description', models.TextField(default='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.category')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
