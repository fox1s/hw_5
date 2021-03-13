# UserModel = get_user_model()
from rest_framework.serializers import ModelSerializer

from company.models import CompanyModel
from employee.serializers import EmployeeSerializer


class CompanySerializer(ModelSerializer):
    employees = EmployeeSerializer(many=True, required=False)

    class Meta:
        model = CompanyModel
        # exclude = ['user']
        fields = ['id', 'name', 'country', 'city', 'user', 'employees']
