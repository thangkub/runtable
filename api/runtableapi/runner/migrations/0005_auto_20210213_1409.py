# Generated by Django 3.1.4 on 2021-02-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runner', '0004_auto_20210210_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='running',
            name='distant',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
