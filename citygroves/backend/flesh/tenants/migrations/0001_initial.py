# Generated by Django 3.0 on 2020-02-02 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("housing", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("street_line1", models.CharField(blank=True, max_length=127, null=True)),
                ("street_line2", models.CharField(blank=True, max_length=127, null=True)),
                ("street_line3", models.CharField(blank=True, max_length=127, null=True)),
                ("city", models.CharField(blank=True, max_length=127, null=True)),
                ("state", models.CharField(blank=True, max_length=127, null=True)),
                ("country", models.CharField(blank=True, max_length=127, null=True)),
                ("post_code", models.CharField(blank=True, max_length=127, null=True)),
                ("raw_address", models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=127)),
                ("middle_names", models.CharField(blank=True, max_length=127)),
                ("last_name", models.CharField(max_length=127)),
                ("email", models.EmailField(blank=True, max_length=127, null=True)),
                ("dob", models.DateField(max_length=127, null=True)),
                ("phone", models.CharField(blank=True, max_length=127, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tenant",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("lease_start", models.DateField(null=True)),
                ("lease_end", models.DateField(null=True)),
                ("people", models.ManyToManyField(to="tenants.Person")),
                ("room", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="housing.Room")),
            ],
        ),
        migrations.CreateModel(
            name="Referrer",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(blank=True, max_length=127, null=True)),
                ("last_name", models.CharField(blank=True, max_length=127, null=True)),
                ("email", models.EmailField(blank=True, max_length=127, null=True)),
                ("phone", models.CharField(blank=True, max_length=127, null=True)),
                (
                    "address",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="tenants.Address"),
                ),
                ("applicant", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="tenants.Person")),
            ],
        ),
        migrations.CreateModel(
            name="EntryNotice",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("planned_on", models.DateField()),
                ("planned_time", models.CharField(max_length=63)),
                ("details", models.CharField(max_length=255, null=True)),
                ("is_inspection", models.BooleanField(default=True)),
                ("is_cleaning", models.BooleanField(default=False)),
                ("is_repairs_or_maintenance", models.BooleanField(default=False)),
                ("is_pest_control", models.BooleanField(default=False)),
                ("is_showing_to_buyer", models.BooleanField(default=False)),
                ("is_valutation", models.BooleanField(default=False)),
                ("is_fire_and_rescue", models.BooleanField(default=False)),
                ("tenant", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="tenants.Tenant")),
            ],
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number_of_ppl_to_move_in", models.IntegerField()),
                ("move_in_date", models.DateField()),
                ("guarantor_will_pay", models.BooleanField()),
                ("centerlink_will_pay", models.BooleanField()),
                ("is_employed", models.BooleanField()),
                ("have_sufficient_funds", models.BooleanField()),
                ("is_local_student", models.BooleanField()),
                ("is_international_student", models.BooleanField()),
                ("is_young_professional", models.BooleanField()),
                ("digital_signature", models.ImageField(null=True, upload_to="")),
                (
                    "current_address",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="tenants.Address"),
                ),
                (
                    "person",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="tenants.Person"),
                ),
                ("referrers", models.ManyToManyField(to="tenants.Referrer")),
                ("room", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="housing.Room")),
            ],
        ),
    ]
