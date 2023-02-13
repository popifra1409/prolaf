import uuid
from django.db import models
from polymorphic.models import PolymorphicModel

class Department(models.Model):
    departmentId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    dept_parent = models.ForeignKey(
        "self", related_name="Departement_parent",  null=True, blank=True, on_delete=models.SET_NULL)
    dept_name = models.CharField(max_length=50, blank=False, null=False)
    dept_description = models.CharField(max_length=200, blank=True, null=True)
    dept_number = models.CharField(max_length=255, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.dept_name)


class Employee(PolymorphicModel):
    STATUS_CHOICES = (('celibat', 'Célibataire'), ('marie', 'Marié(e)'), ('divorce',
                                                                          'Divorcé(e)'), ('veuf ', 'Veuf(ve)'), ('concubin', 'Concubinage'))

    GENDER_CHOICES = (('male', 'Masculin'), ('female',
                      'Féminin'), ('other', 'Non précisé'))

    employeeId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    employeeMat = models.CharField(
        max_length=150, blank=False, null=False, editable=False, unique=True)
    department = models.ForeignKey(
        Department, blank=False, null=False, on_delete=models.CASCADE)
    superieur = models.ForeignKey(
        "self", related_name="supérieur", null=True, blank=True, on_delete=models.SET_NULL)
    firstname = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(
        max_length=20, blank=True, null=True, choices=STATUS_CHOICES, default='celibat')
    status = models.CharField(
        max_length=255, blank=True, null=True, choices=GENDER_CHOICES, default='Non précisé')
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(
        null=True, blank=True, upload_to='', default="")
    function = models.CharField(max_length=255, blank=True, null=True)
    hiringdate = models.DateField(blank=False, null=False)
    seniority = models.IntegerField()
    salary = models.FloatField()
    whatsappnumber = models.CharField(max_length=20, blank=True, null=True)
    facebooklink = models.CharField(max_length=255, blank=True, null=True)
    resourcecontact = models.CharField(max_length=20, blank=True, null=True)
    resourcename = models.CharField(max_length=255, blank=True, null=True)
    isChiefOfDepartment = models.BooleanField(max_length=5, default=False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.employeeMat)

class Manager(Employee):
    pass

class Supervisor(Employee):
    pass

class Accountant(Employee):
    pass


class Worker(Employee):
    pass


class Document(models.Model):
    documentId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    employee = models.OneToOneField(
        Employee, blank=False, null=False, on_delete=models.CASCADE)
    numCni = models.CharField(
        max_length=100, blank=True, null=True, unique=True)
    cniupload = models.FileField(null=False)
    diploma = models.CharField(max_length=255, blank=True, null=True)
    diplomaupload = models.FileField(max_length=255, blank=False, null=False)
    mariagecertificate = models.FileField(
        max_length=255, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.numCni)


class Agent(PolymorphicModel):
    agentId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
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

class Client(Agent):
    pass

class Supplier(Agent):
    pass

class Contract(PolymorphicModel):
    contractId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    employee = models.OneToOneField(
        Employee, blank=True, null=True, on_delete=models.CASCADE)
    agent = models.OneToOneField(
        Agent, blank=True, null=True, on_delete=models.CASCADE)
    contract_no = models.CharField(max_length=255, blank=True, null=True)
    dateofcreation = models.DateField(max_length=255, blank=True, null=True)
    duration = models.DateField(max_length=255, blank=True, null=True)
    formofcontract = models.CharField(max_length=255, blank=True, null=True)
    contractupload = models.FileField(
        upload_to="ContractFile/contract.pdf", blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.contract_no)

class Employee_cont(Contract):
    pass

class Supplier_cont(Contract):
    pass

class Client_cont(Contract):
    pass
