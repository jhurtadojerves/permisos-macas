# Core imports
from django.views.generic import CreateView, ListView

# Third party imports

# Local imports
from employees.models import Employee


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employees/employees_create.html"
    fields = ("name",)
    success_url = "/empleados/"


class EmployeeListView(ListView):
    model = Employee
    template_name = "employees/employees_list.html"
    context_object_name = "employees"
