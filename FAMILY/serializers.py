from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Building, Lodge, Family, Pig, Fowl, Parameter,Param_Registration, Lodge_Registration

class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class LodgeSerializer(ModelSerializer):
    class Meta:
        model = Lodge
        fields = '__all__'


class FamilySerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'       

class PigSerializer(ModelSerializer):
    class Meta:
        model = Pig
        fields = '__all__'

class FowlSerializer(ModelSerializer):
    class Meta:
        model = Fowl
        fields = '__all__'        

class ParameterSerializer(ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'                        

class ParamRegistrationSerializer(ModelSerializer):
    parameter = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Param_Registration
        fields = '__all__'

class LodgeRegistrationSerializer(ModelSerializer):
    class Meta:
        model = Lodge_Registration
        fields = '__all__'        