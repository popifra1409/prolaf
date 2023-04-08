from rest_framework.serializers import ModelSerializer
from .models import Building, Lodge, Family, Member

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


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'                
