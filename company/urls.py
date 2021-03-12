from django.urls import path

from company.views import CompanyListCreateView, CompanyReadUpdateDeleteView

urlpatterns = [
    path('', CompanyListCreateView.as_view(), name='company_list_create'),
    path('/<int:pk>', CompanyReadUpdateDeleteView.as_view(), name='company_read_update_delete')
]
