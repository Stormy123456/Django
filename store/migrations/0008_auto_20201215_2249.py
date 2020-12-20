# Generated by Django 3.1.3 on 2020-12-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20201215_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_identification_code',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_username',
            field=models.CharField(error_messages={'unique': 'This username has already been registered.'}, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_identification_code',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
