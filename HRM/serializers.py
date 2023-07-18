from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Agent, Internal, External,Employee, Department, Document

class DepartmentSerializer(ModelSerializer):
    dept_parent = serializers.SlugRelatedField(slug_field='dept_name', read_only=True)

    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(ModelSerializer):
    department = serializers.SlugRelatedField(slug_field='dept_name', read_only=True)
    supervisor = serializers.SlugRelatedField(slug_field='firstname', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'        


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class AgentSerializer(ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'                         

class InternalSerializer(ModelSerializer):
    class Meta:
        model = Internal
        fields = '__all__'       

class ExternalSerializer(serializers.ModelSerializer):
    agentname = serializers.SlugRelatedField(slug_field='firstname', read_only=True)


    class Meta:
        model = External
        fields = '__all__'

    """
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__' 

class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'      """                                

     
