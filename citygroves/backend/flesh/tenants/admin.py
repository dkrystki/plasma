from django.contrib import admin

from tenants import models

admin.site.register(models.Person)
admin.site.register(models.Address)
admin.site.register(models.Referrer)
admin.site.register(models.Application)
admin.site.register(models.Tenant)
admin.site.register(models.EntryNotice)
