from django.db.models import query
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from covidclinic.models import Clinic


def clinic_list(request: HttpRequest) -> HttpResponse:
    qs = Clinic.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    context_data = {
        "clinic_list": qs,
    }
    return render(request, "covidclinic/clinic_list.html", context_data)


def clinic_detail(request: HttpRequest, pk: int) -> HttpResponse:
    clinic = Clinic.objects.get(pk=pk)
    context_data = {
        "clinic": clinic,
    }
    return render(request, "covidclinic/clinic_detail.html", context_data)
