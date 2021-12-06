from django.contrib import admin
from covidclinic.models import Clinic

class ClinicAdmin(admin.ModelAdmin):
     list_display = ["id", "name", "address", "weekdaytime", "telephone"]
     list_display_links = ["name"]


admin.site.register(Clinic, ClinicAdmin)