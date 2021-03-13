from django.urls import path

from employee.views import EmployeeListView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list_create')
]
