from django.contrib import admin

from tenants.models import Person, Address, Referrer, Application, Tenant

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Referrer)
admin.site.register(Application)
admin.site.register(Tenant)
