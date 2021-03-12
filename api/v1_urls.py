from django.urls import path, include

urlpatterns = [
    path('/users', include('users.urls')),
    path('/company', include('company.urls'))
]
