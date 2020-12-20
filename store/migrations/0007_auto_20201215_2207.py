# Generated by Django 3.1.3 on 2020-12-15 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_identification_code',
            field=models.CharField(error_messages={'unique': 'รหัสประจำตัวประชาชนนี้มีผู้ใช้แล้ว'}, max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_username',
            field=models.CharField(error_messages={'unique': 'Username นี้มีผู้ใช้แล้ว'}, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_identification_code',
            field=models.CharField(error_messages={'unique': 'รหัสประจำตัวประชาชนนี้มีผู้ใช้แล้ว'}, max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_username',
            field=models.CharField(error_messages={'unique': 'Username นี้มีผู้ใช้แล้ว'}, max_length=20, unique=True),
        ),
    ]