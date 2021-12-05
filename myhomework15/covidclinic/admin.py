from django.contrib import admin

from covidclinic.models import Clinic


class ClinicAdmin(admin.ModelAdmin):
    pass


admin.site.register(Clinic, ClinicAdmin)
