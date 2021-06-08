# Generated by Django 3.1.6 on 2021-06-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(default='cricket', max_length=60, unique=True, verbose_name='Email address'),
            preserve_default=False,
        ),
    ]