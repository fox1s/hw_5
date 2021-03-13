from django.urls import path

from employee.views import EmployeeListView,EmployeeReadUpdateDeleteView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list_create'),
    path('/<int:pk>', EmployeeReadUpdateDeleteView.as_view(), name='employee_list_create'),
]
