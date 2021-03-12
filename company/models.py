from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

UserModel = get_user_model()


class CompanyModel(models.Model):
    class Meta:
        db_table = 'companies'

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30, validators=[RegexValidator('^[a-zA-z]{2,30}$')])
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='companies')
