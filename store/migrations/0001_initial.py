# Generated by Django 3.1.3 on 2020-12-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('emp_username', models.CharField(error_messages={'unique_error_message': 'This username has already been registered.'}, max_length=20, unique=True)),
                ('emp_password', models.CharField(max_length=100)),
                ('emp_prefix', models.CharField(max_length=10)),
                ('emp_fname', models.CharField(max_length=20)),
                ('emp_lname', models.CharField(max_length=20)),
                ('emp_identification_code', models.CharField(max_length=13, unique=True)),
                ('emp_bdate', models.DateTimeField()),
                ('emp_image', models.ImageField(default='', upload_to='employee_image')),
                ('emp_status_finger', models.BooleanField(default=False)),
                ('status_login', models.IntegerField()),
                ('emp_finger1', models.CharField(default='', max_length=10000, null=True)),
                ('emp_finger2', models.CharField(default='', max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('fac_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='major',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('mjr_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='typeuser',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('typ_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('user_username', models.CharField(max_length=20, unique=True)),
                ('user_password', models.CharField(max_length=150)),
                ('user_prefix', models.CharField(max_length=10)),
                ('user_fname', models.CharField(max_length=20)),
                ('user_lname', models.CharField(max_length=20)),
                ('user_identification_code', models.CharField(max_length=13, unique=True)),
                ('user_type', models.CharField(max_length=20)),
                ('user_bdate', models.DateTimeField()),
                ('user_image', models.ImageField(default='', upload_to='user_image')),
                ('user_status_finger', models.BooleanField(default=False)),
                ('status_login', models.IntegerField()),
                ('user_finger1', models.CharField(default='', max_length=10000, null=True)),
                ('user_finger2', models.CharField(default='', max_length=10000, null=True)),
            ],
        ),
    ]
