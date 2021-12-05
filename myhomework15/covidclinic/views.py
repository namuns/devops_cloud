from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from covidclinic.models import Clinic



def index(request: HttpRequest) -> HttpResponse:
    qs = Clinic.objects.all()
    return render(request, "covidclinic/index.html", {
        "clinic_list": qs,
    })

def clinic_list(request: HttpRequest) -> HttpResponse:
    qs = Clinic.objects.all()

    context_data = {
        "clinic_list": qs,
    }

    return render(request, "covidclinic/index.html", context_data)

