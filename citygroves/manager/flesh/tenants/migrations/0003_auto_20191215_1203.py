# Generated by Django 3.0 on 2019-12-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_auto_20191215_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrer',
            name='email',
            field=models.EmailField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='referrer',
            name='first_name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='referrer',
            name='last_name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='referrer',
            name='phone',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]