from rest_framework.serializers import ModelSerializer
from .models import Building, Lodge, Family, Pig, Parameter, Pig_ParamRegistration, Pig_LodgeRegistration

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

class ParameterSerializer(ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'                        

class Pig_ParamRegistrationSerializer(ModelSerializer):
    class Meta:
        model = Pig_ParamRegistration
        fields = '__all__'

class Pig_LodgeRegistrationSerializer(ModelSerializer):
    class Meta:
        model = Pig_LodgeRegistration
        fields = '__all__'        