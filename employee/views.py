from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView

from employee.models import EmployeeModel
from employee.serializers import EmployeeSerializer


class EmployeeListView(ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
