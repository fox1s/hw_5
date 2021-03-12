from django.contrib.auth import get_user_model
from django.urls import path

# UserModel = get_user_model()
from rest_framework.serializers import ModelSerializer

from company.models import CompanyModel

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_superuser', 'is_staff', 'is_active']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
