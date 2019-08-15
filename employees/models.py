# Core imports
from django.db import models

# Third party imports

# Local imports


class Employee(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
