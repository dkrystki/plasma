# Generated by Django 3.0 on 2020-01-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0003_auto_20191215_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='lease_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='lease_start',
            field=models.DateField(null=True),
        ),
    ]
