from django.contrib.auth import get_user_model
from django.urls import path

# UserModel = get_user_model()
from rest_framework.serializers import ModelSerializer

from company.models import CompanyModel


class CompanySerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ['id', 'name', 'country', 'city']

