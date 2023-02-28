from rest_framework.serializers import ModelSerializer
from .models import Client, Supplier, Internal, External, Department, Supervisor, Manager, Accountant,Worker, Document

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SupervisorSerializer(ModelSerializer):
    class Meta:
        model = Supervisor
        fields = '__all__'       

class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'   

class AccountantSerializer(ModelSerializer):
    class Meta:
        model = Accountant
        fields = '__all__' 

class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
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
