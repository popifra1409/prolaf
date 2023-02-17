from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Department, Document, Employee
from .serializers import DepartmentSerializer, DocumentSerializer, EmployeeSerializer


# ============== Departemnet management ====================
# get all departements
@api_view(['GET'])
def getDepartments(request):
    departements = Department.objects.all()
    serializer = DepartmentSerializer(departements, many=True)
    return Response(serializer.data)

#get a single departement
@api_view(['GET'])
def getDepartment(request, pk):
    departement = Department.objects.get(departmentId=pk)
    serializer = DepartmentSerializer(departement, many=False)
    return Response(serializer.data)


# ============== Employee management ====================
# get all employees
@api_view(['GET'])
def getEmployees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

#get a single employee
@api_view(['GET'])
def getEmployee(request, pk):
    employee = Employee.objects.get(employeeId=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


# ============== Document management ====================
# get all documents
@api_view(['GET'])
def getDocuments(request):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)
    return Response(serializer.data)

#get a single document
@api_view(['GET'])
def getDocument(request, pk):
    document = Document.objects.get(employeeId=pk)
    serializer = DocumentSerializer(document, many=False)
    return Response(serializer.data)