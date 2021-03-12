from django.contrib.auth import get_user_model
from django.urls import path

# UserModel = get_user_model()
from rest_framework.serializers import ModelSerializer

from company.models import CompanyModel
from company.serializers import CompanySerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    companies = CompanySerializer(many=True, required=True)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_superuser', 'is_staff', 'is_active', 'companies']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
