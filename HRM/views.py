from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Department, Employee, Document, Internal, External, Agent
from .serializers import DepartmentSerializer, EmployeeSerializer, DocumentSerializer, InternalSerializer, ExternalSerializer, AgentSerializer


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
def createEmployee(request, supid, departmentid):
    data = request.data
    department = Department.objects.get(departmentId=departmentid)
    supervisor = Employee.objects.get(employeeId=supid)
    employee = Employee.objects.create(
        department=department,
        supervisor=supervisor,
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

#Update a single document
@api_view(['PUT'])
def updateDocument(request, pk):
    data = request.data
    document = Document.objects.get(documentId=pk)
    serializer = DocumentSerializer(instance=document, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

  
    #create a single document
@api_view(['POST'])
def createDocument(request, employeeid):
    data = request.data
    employee = Employee.objects.get(employeeId=employeeid)
    document = Document.objects.create(
        employee= employee,
        numCni=data['numCni'],
        cniupload=data['cniupload'],
        diploma=data['diploma'],
        diplomaupload=data['diplomaupload'],
        mariagecertificate=data['mariagecertificate']
        
    )
    serializer = DocumentSerializer(document, many=False)
    return Response(serializer.data)  

#delete a single document
@api_view(['DELETE'])
def deleteDocument(request, pk):
    document = Document.objects.get(documentId=pk)
    document.delete()
    return Response('Document was deleted!') 


# ============== Internal Contract management ==================== 
# get all internal contracts
@api_view(['GET'])
def getInternals(request):
    internals = Internal.objects.all()
    serializer = InternalSerializer(internals, many=True)
    return Response(serializer.data)

#get a single Internal contract
@api_view(['GET'])
def getInternal(request, pk):
    internal = Internal.objects.get(contractId=pk)
    serializer = InternalSerializer(internal, many=False)
    return Response(serializer.data)     

#Update a single internal contract
@api_view(['PUT'])
def updateInternal(request, pk):
    data = request.data
    internal = Internal.objects.get(contractId=pk)
    serializer = InternalSerializer(instance=internal, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single internal contract
@api_view(['POST'])
def createInternal(request, employeeid):
    data = request.data
    employee = Employee.objects.get(employeeId=employeeid)
    internal = Internal.objects.create(
        contract_no=data['contract_no'],
        employee= employee,
        dateofcreation=data['dateofcreation'],
        duration=data['duration'],
        formofcontract=data['formofcontract'],
        contractupload=data['contractupload']
        
    )
    serializer = InternalSerializer(internal, many=False)
    return Response(serializer.data)  

#delete a single internal contract
@api_view(['DELETE'])
def deleteInternal(request, pk):
    internal = Internal.objects.get(contractId=pk)
    internal.delete()
    return Response('Internal Contract was deleted!')      
     

# ============== External Contract management ==================== 
# get all external contracts
@api_view(['GET'])
def getExternals(request):
    externals = External.objects.all()
    serializer = ExternalSerializer(externals, many=True)
    return Response(serializer.data)

#get a single External contract
@api_view(['GET'])
def getExternal(request, pk):
    external = External.objects.get(contractId=pk)
    serializer = ExternalSerializer(external, many=False)
    return Response(serializer.data)     

#Update a single external contract
@api_view(['PUT'])
def updateExternal(request, pk):
    data = request.data
    external = External.objects.get(contractId=pk)
    serializer = ExternalSerializer(instance=external, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single external contract
@api_view(['POST'])
def createExternal(request, agentid):
    data = request.data
    client = Client.objects.get(agentId=agentid)
    external = External.objects.create(
        contract_no=data['contract_no'],
        agent= agent,
        dateofcreation=data['dateofcreation'],
        duration=data['duration'],
        formofcontract=data['formofcontract'],
        contractupload=data['contractupload']
        
    )
    serializer = ExternalSerializer(external, many=False)
    return Response(serializer.data)  

#delete a single external contract
@api_view(['DELETE'])
def deleteExternal(request, pk):
    external = External.objects.get(contractId=pk)
    external.delete()
    return Response('External Contract was deleted!')


# ============== Agent management ==================== 
# get all agents
@api_view(['GET'])
def getAgents(request):
    agents = Agent.objects.all()
    serializer = AgentSerializer(agents, many=True)
    return Response(serializer.data)

#get a single agent
@api_view(['GET'])
def getAgent(request, pk):
    agent = Agent.objects.get(agentId=pk)
    serializer = AgentSerializer(agent, many=False)
    return Response(serializer.data)     

#Update a single agent
@api_view(['PUT'])
def updateAgent(request, pk):
    data = request.data
    agent = Agent.objects.get(agentId=pk)
    serializer = AgentSerializer(instance=agent, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single agent
@api_view(['POST'])
def createAgent(request):
    data = request.data
    agent = Agent.objects.create(
        agenttype=data['agenttype'],
        firstname=data['firstname'],
        lastname=data['lastname'],
        address=data['address'],
        phone=data['phone'],
        email=data['email'],
        company=data['company'],
        niu=data['niu'],
        observation=data['observation'],
        bankaccount=data['bankaccount']

    )
    serializer = AgentSerializer(agent, many=False)
    return Response(serializer.data)  

#delete a single Agent
@api_view(['DELETE'])
def deleteAgent(request, pk):
    agent = Agent.objects.get(agentId=pk)
    agent.delete()
    return Response('Agent was deleted!')      


""" # ============== Client management ==================== 
# get all clients
@api_view(['GET'])
def getClients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

#get a single Client
@api_view(['GET'])
def getClient(request, pk):
    client = Client.objects.get(agentId=pk)
    serializer = ClientSerializer(client, many=False)
    return Response(serializer.data)     

#Update a single client
@api_view(['PUT'])
def updateClient(request, pk):
    data = request.data
    client = Client.objects.get(agentId=pk)
    serializer = ClientSerializer(instance=client, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single client
@api_view(['POST'])
def createClient(request):
    data = request.data
    client = Client.objects.create(
        firstname=data['firstname'],
        lastname=data['lastname'],
        address=data['address'],
        phone=data['phone'],
        email=data['email'],
        company=data['company'],
        niu=data['niu'],
        observation=data['observation'],
        bankaccount=data['bankaccount']

    )
    serializer = ClientSerializer(client, many=False)
    return Response(serializer.data)  

#delete a single client
@api_view(['DELETE'])
def deleteClient(request, pk):
    client = Client.objects.get(agentId=pk)
    client.delete()
    return Response('Client was deleted!')                
          

# ============== Supplier management ==================== 
# get all suppliers
@api_view(['GET'])
def getSuppliers(request):
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)

#get a single supplier
@api_view(['GET'])
def getSupplier(request, pk):
    supplier = Supplier.objects.get(agentId=pk)
    serializer = SupplierSerializer(supplier, many=False)
    return Response(serializer.data)     

#Update a single supplier
@api_view(['PUT'])
def updateSupplier(request, pk):
    data = request.data
    supplier = Supplier.objects.get(agentId=pk)
    serializer = SupplierSerializer(instance=supplier, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single supplier
@api_view(['POST'])
def createSupplier(request):
    data = request.data
    supplier = Supplier.objects.create(
        firstname=data['firstname'],
        lastname=data['lastname'],
        address=data['address'],
        phone=data['phone'],
        email=data['email'],
        company=data['company'],
        niu=data['niu'],
        observation=data['observation'],
        bankaccount=data['bankaccount']

    )
    serializer = SupplierSerializer(supplier, many=False)
    return Response(serializer.data)  

#delete a single client
@api_view(['DELETE'])
def deleteSupplier(request, pk):
    supplier = Supplier.objects.get(agentId=pk)
    supplier.delete()
    return Response('Supplier was deleted!') """

