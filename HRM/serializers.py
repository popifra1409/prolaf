from rest_framework.serializers import ModelSerializer
from .models import Client,Supplier, Internal, External,Employee, Department, Document

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

class InternalSerializer(ModelSerializer):
    class Meta:
        model = Internal
        fields = '__all__'       

class ExternalSerializer(ModelSerializer):
    class Meta:
        model = External
        fields = '__all__' 

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__' 

class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'                                     

""" class AgentSerializer(ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'    """   
