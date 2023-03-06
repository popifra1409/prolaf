from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Department, Manager
from .serializers import DepartmentSerializer, ManagerSerializer


# ============== Departement management ====================
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
# get all managers
@api_view(['GET'])
def getEmployees(request):
    employees = Manager.objects.all()
    serializer = ManagerSerializer(employees, many=True)
    return Response(serializer.data)

#get a single manager
@api_view(['GET'])
def getEmployee(request, pk):
    employee = Manager.objects.get(employeeId=pk)
    serializer = ManagerSerializer(employee, many=False)
    return Response(serializer.data)


# ============== Document management ====================