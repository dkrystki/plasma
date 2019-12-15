from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    email = models.EmailField(max_length=127, null=True, blank=True)
    dob = models.DateField(max_length=127, null=True)
    phone = models.CharField(max_length=127, null=True, blank=True)


class Address(models.Model):
    street_line1 = models.CharField(max_length=127, null=True, blank=True)
    street_line2 = models.CharField(max_length=127, null=True, blank=True)
    street_line3 = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=127, null=True, blank=True)
    state = models.CharField(max_length=127, null=True, blank=True)
    country = models.CharField(max_length=127, null=True, blank=True)
    post_code = models.CharField(max_length=127, null=True, blank=True)
    raw_address = models.CharField(max_length=512)


class Referrer(models.Model):
    first_name = models.CharField(max_length=127, null=True, blank=True)
    last_name = models.CharField(max_length=127, null=True, blank=True)
    email = models.EmailField(max_length=127, null=True, blank=True)
    phone = models.CharField(max_length=127, null=True, blank=True)
    applicant = models.ForeignKey(Person, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)


class Application(models.Model):
    from housing.models import Room

    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    current_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    number_of_ppl_to_move_in = models.IntegerField()
    move_in_date = models.DateField()
    guarantor_will_pay = models.BooleanField()
    centerlink_will_pay = models.BooleanField()
    is_employed = models.BooleanField()
    have_sufficient_funds = models.BooleanField()
    is_local_student = models.BooleanField()
    is_international_student = models.BooleanField()
    is_young_professional = models.BooleanField()
    referrers = models.ManyToManyField(Referrer)
    digital_signature = models.ImageField(null=True)


class Tenant(models.Model):
    from housing.models import Room
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
