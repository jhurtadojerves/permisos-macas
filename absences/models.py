# Core imports
from django.core.validators import MinValueValidator
from django.db import models

# Third party imports

# Local imports
from employees.models import Employee


class Absence(models.Model):
    type_choices = [
        ("Vacaciones", "Cargo a Vacaciones"),
        ("Enfermedad", "Enfermedad"),
        ("Compensacion", "Compensación"),
        ("Calamidad", "Calamidad"),
        ("Certificado", "Presentar Certificado"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    absense_type = models.CharField(
        max_length=16, choices=type_choices, default="Vacaciones"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_days = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )

