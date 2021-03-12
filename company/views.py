from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from company.models import CompanyModel
from company.serializers import CompanySerializer


class CompanyListCreateView(ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = CompanyModel.objects.all()
        city = self.request.query_params.get('city')
        if city:
            queryset = queryset.filter(city__iexact=city)
        return queryset


class CompanyReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
