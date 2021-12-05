from django.contrib import admin

from covidclinic.models import Clinic


class ClinicAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "weekdaytime", "sattime", "hdaytime", "telephone"]
    list_display_links = ["name"]
admin.site.register(Clinic, ClinicAdmin)
