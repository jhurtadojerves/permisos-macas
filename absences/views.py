# Core imports
from django.views.generic import CreateView, ListView
from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponse
from django.template import loader


# Third party imports

# Local imports
from absences.models import Absence
from absences.forms import MyCreateForm
from employees.models import Employee


class AbsenceListView(ListView):
    model = Absence
    template_name = "absences/absences_list.html"
    context_object_name = "absences"


class AbsenceCreateView(CreateView):
    model = Absence
    template_name = "absences/absences_create.html"
    form_class = MyCreateForm
    success_url = "/permisos/"


def reporte(request):
    empleados = Employee.objects.all()
    printempleados = list()
    for empleado in empleados:
        vacaciones = (
            Absence.objects.filter(
                employee=empleado, absense_type="Vacaciones"
            ).aggregate(Sum("number_of_days"))["number_of_days__sum"]
            or 0
        )
        enfermedad = (
            Absence.objects.filter(
                employee=empleado, absense_type="Enfermedad"
            ).aggregate(Sum("number_of_days"))["number_of_days__sum"]
            or 0
        )
        compensacion = (
            Absence.objects.filter(
                employee=empleado, absense_type="Compensacion"
            ).aggregate(Sum("number_of_days"))["number_of_days__sum"]
            or 0
        )
        calamidad = (
            Absence.objects.filter(
                employee=empleado, absense_type="Calamidad"
            ).aggregate(Sum("number_of_days"))["number_of_days__sum"]
            or 0
        )
        certificado = (
            Absence.objects.filter(
                employee=empleado, absense_type="Certificado"
            ).aggregate(Sum("number_of_days"))["number_of_days__sum"]
            or 0
        )
        printempleados.append(
            (empleado, vacaciones, enfermedad, compensacion, calamidad, certificado)
        )
        # View code here...
    t = loader.get_template("absences/reporte.html")
    c = {"reportes": printempleados}
    return render(request, "absences/reporte.html", c)
    # return HttpResponse(t.render(c, request), content_type="application/xhtml+xml")
