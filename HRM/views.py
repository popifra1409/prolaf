from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Department, Employee, Document
from .serializers import DepartmentSerializer, EmployeeSerializer, DocumentSerializer


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
# get all employee
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

  #Update a single employee
@api_view(['PUT'])
def updateEmployee(request, pk):
    data = request.data
    employee = Employee.objects.get(employeeId=pk)
    serializer = EmployeeSerializer(instance=employee, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

 #create a single employee
@api_view(['POST'])
def createEmployee(request, parentid):
    data = request.data
    department = Department.objects.get(departmentId=parentid)
    employee = Employee.objects.create(
        employeeMat=data['employeeMat'],
        department=department,
        firstname=data['firstname'],
        lastname=data['lastname'],
        birthdate=data['birthdate'],
        birthplace=data['birthplace'],
        gender=data['gender'],
        status=data['status'],
        email=data['email'],
        address=data['address'],
        phone=data['phone'],
        photo=data['photo'],
        function=data['function'],
        hiringdate=data['hiringdate'],
        seniority=data['seniority'],
        salary=data['salary'],
        whatsappnumber=data['whatsappnumber'],
        facebooklink=data['facebooklink'],
        resourcecontact=data['resourcecontact'],
        resourcename=data['resourcename'],
        isChiefOfDepartment=data['isChiefOfDepartment'],
        typeofemployee=data['typeofemployee']
        
    )
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)  

#delete a single employee
@api_view(['DELETE'])
def deleteEmployee(request, pk):
    employee = Employee.objects.get(employeeId=pk)
    employee.delete()
    return Response('Employee was deleted!')       


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
    document = Document.objects.get(documentId=pk)
    serializer = DocumentSerializer(document, many=False)
    return Response(serializer.data)
