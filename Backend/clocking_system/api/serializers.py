from rest_framework import serializers
from .models import Signing

class SigningSerializer(serializers.ModelSerializer):

    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Signing
        fields = '__all__'