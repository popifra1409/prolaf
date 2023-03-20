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

#Update a single departement
@api_view(['PUT'])
def updateDepartment(request, pk):
    data = request.data
    department = Department.objects.get(departmentId=pk)
    serializer = DepartmentSerializer(instance=department, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single departement
@api_view(['POST'])
def createDepartment(request, parentid):
    data = request.data
    department_parent = Department.objects.get(departmentId=parentid)
    department = Department.objects.create(
        dept_name=data['dept_name'],
        dept_parent= department_parent,
        dept_description=data['dept_description'],
        dept_number=data['dept_number']
        
    )
    serializer = DepartmentSerializer(department, many=False)
    return Response(serializer.data)  

#delete a single departement
@api_view(['DELETE'])
def deleteDepartment(request, pk):
    department = Department.objects.get(departmentId=pk)
    department.delete()
    return Response('Department was deleted!')  

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