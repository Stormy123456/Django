# Generated by Django 3.1.3 on 2020-12-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201211_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]