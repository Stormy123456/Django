# Generated by Django 3.1.3 on 2020-12-11 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201211_0755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='updated_at',
        ),
    ]