from django.db import models

# Create your models here.
from company.models import CompanyModel


class EmployeeModel(models.Model):
    class Meta:
        db_table = 'employee'

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    profession = models.CharField(max_length=30)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='employees')
