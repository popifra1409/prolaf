from rest_framework.serializers import ModelSerializer
from .models import Agent, Contract, Department, Employee, Document

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'        

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'                

class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'                         

class AgentSerializer(ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'                                        
