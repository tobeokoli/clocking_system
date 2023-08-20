from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'salary', 'is_admin', 'first_name', 'last_name', 'username')
        extra_kwargs = {'password': {'write_only': True}}