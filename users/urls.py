from django.urls import path

from company.views import CompanyListCreateView, CompanyReadUpdateDeleteView
from users.views import UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    # path('/<int:pk>', CompanyReadUpdateDeleteView.as_view(), name='company_read_update_delete')
]
