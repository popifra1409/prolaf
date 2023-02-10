import uuid
from django.db import models

# Create your models here.

class Department(models.Model):
   departmentId = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
   Employee = models.ManyToOneRel(Employee, blank=True, null=True, on_delete=models.CASCADE)
   subDepartement = models.ForeignKey("sub departement","self",related_name="sub_departement", on_delete=models.CASCADE,null=True, blank=True)
   dept_name = models.CharField(max_length=255, blank=True, null=True)
   description = models.CharField(max_length=255, blank=True, null=True)
   deptnumber = models.CharField(max_length=255, blank=True, null=True)
   createDate = models.DateTimeField(auto_now_add=True)
   updateDate = models.DateTimeField(auto_now=True)

   def __str__(self):
        return str(self.dept_name)


class Employee(models.Model):
    employeeId = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE)
    subEmployee = models.ForeignKey("sub Employee","self",related_name="sub_Employee", on_delete=models.CASCADE,null=True, blank=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(max_length=10, blank=True, null=True)
    birthplace = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=20,blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    function = models.CharField(max_length=255, blank=True, null=True)
    hiringdate = models.DateField(max_length=10, blank=True, null=True)
    seniority = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    whatsappnumber = models.CharField(max_length=255, blank=True, null=True)
    facebooklink = models.CharField(max_length=255, blank=True, null=True)
    resourcecontact = models.CharField(max_length=255, blank=True, null=True)
    resourcename = models.CharField(max_length=255, blank=True, null=True)
    isChiefOfDepartment = models.BooleanField(max_length=5, default=False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.firstname)

    class Meta:
        abstract = True

class Manager(Employee):
    manage_empl = models.CharField(max_length=255)

class Supervisor(Employee):  
    supervise_work = models.CharField(max_length=255)  

class Accountant(Employee):
    pay_empl = models.CharField(max_length=255)

class Worker(Employee):
    firm_work = models.CharField(max_length=255)


class Documents(models.Model):
    documentId = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    employee = models.OneToOneField(Employee, blank=True, null=True, on_delete=models.CASCADE)
    numCni = models.CharField(max_length=255, blank=True, null=True)    
    cniupload = models.FileField(null=True)
    diploma = models.CharField(max_length=255, blank=True, null=True)
    diplomaupload = models.FileField(max_length=255, blank=True, null=True)
    marriagecertificate = models.FileField(max_length=255, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.numCni)


class Agent(models.Model):
    agentId = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    niu = models.CharField(max_length=255, blank=True, null=True)
    observation = models.CharField(max_length=255, blank=True, null=True)
    bankaccount = models.CharField(max_length=255, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.firstname)   

    class Meta:
        abstract = True

class Client(Agent):
    paydate = models.DateField(max_length=255)
    
class Supplier(Agent):  
    deliverydate = models.DateField(max_length=255) 
                 

class Contract(models.Model):
    contractId = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    employee = models.OneToOneField(Employee, blank=True, null=True, on_delete=models.CASCADE)
    agents = models.OneToOneField(Agent, blank=True, null=True, on_delete=models.CASCADE)
    contract_no = models.CharField(max_length=255, blank=True, null=True)
    dateofcreation = models.DateField(max_length=255, blank=True, null=True)
    duration = models.DateField(max_length=255, blank=True, null=True)
    formofcontract = models.CharField(max_length=255, blank=True, null=True)
    contractupload = models.FieldFile(upload_to="ContractFile/contract.pdf", blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.contract_no)

    class Meta:
        abstract = True

class Employee_cont(Contract):
    paydate = models.DateField(max_length=255)

class Supplier_cont(Contract):  
    deliverydate = models.DateField(max_length=255)  

class Client_cont(Contract):
    paydate = models.DateField(max_length=255)




    