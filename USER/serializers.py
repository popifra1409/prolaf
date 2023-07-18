from rest_framework.serializers import ModelSerializer
from .models import Credentials
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = ['pseudo', 'password']
