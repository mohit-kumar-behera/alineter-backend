# Generated by Django 3.1.6 on 2021-07-01 15:33

import company.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_companyreview_highlight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Company Name')),
                ('tag', models.CharField(max_length=255, verbose_name='Company Tag')),
                ('founded', models.DateTimeField(verbose_name='Company Founded')),
                ('active', models.BooleanField(default=True, verbose_name='Company State')),
                ('website', models.URLField(max_length=50, verbose_name='Company Website')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTelephoneHelpline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helpline', models.CharField(max_length=20, verbose_name='Helpline Type')),
                ('telephone', models.CharField(max_length=15, verbose_name='Telephone')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyFounder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('designation', models.CharField(max_length=30, verbose_name='Designation')),
                ('profile_pic', models.ImageField(upload_to=company.models.profilepic_directory_path, verbose_name='Profile Pic')),
                ('bio', models.TextField(verbose_name='About Founder')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyEmailHelpline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helpline', models.CharField(max_length=20, verbose_name='Helpline Type')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField(verbose_name='Street Address')),
                ('city', models.CharField(max_length=40, verbose_name='City')),
                ('pin', models.CharField(max_length=6, verbose_name='PIN')),
                ('district', models.CharField(max_length=30, verbose_name='District')),
                ('state', models.CharField(max_length=30, verbose_name='State')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
