from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class CompanyModel(models.Model):
    class Meta:
        db_table = 'companies'

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30, validators=[RegexValidator('^[a-zA-z]{2,30}$')])
