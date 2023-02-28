import uuid
from django.db import models

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

class Employee(models.Model):
    STATUS_CHOICES = (('single', 'Single'), ('married', 'Married'), ('divorce',
                        'Divorce'), ('widower ', 'Widower'), ('partner', 'Partner'))

    GENDER_CHOICES = (('male', 'Male'), ('female',
                      'Female'), ('other', 'Non precised'))

    employeeId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    employeeMat = models.CharField(
        max_length=150, blank=False, null=False, editable=False, unique=False)
    department = models.ForeignKey(
        Department, blank=False, null=False, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(
        max_length=20, blank=True, null=True, choices= GENDER_CHOICES, default='Non précisé')
    status = models.CharField(
        max_length=255, blank=True, null=True, choices= STATUS_CHOICES, default='celibat')
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
        return str(self.firstname)
    
    class Meta:
        abstract = True

class Supervisor(Employee):
    pass

class Manager(Employee):
    manager = models.ForeignKey(Supervisor, related_name="manager", null=True, blank=True, on_delete=models.SET_NULL)

class Accountant(Employee):
    manager = models.ForeignKey(Supervisor, related_name="accountant", null=True, blank=True, on_delete=models.SET_NULL)

class Worker(Employee):
    manager = models.ForeignKey(Supervisor, related_name="worker", null=True, blank=True, on_delete=models.SET_NULL)

class Document(models.Model):
    documentId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    supervisor = models.OneToOneField(
        Supervisor, blank=False, null=False, on_delete=models.CASCADE)
    manager = models.OneToOneField(
        Manager, blank=False, null=False, on_delete=models.CASCADE)
    accountant = models.OneToOneField(
        Accountant, blank=False, null=False, on_delete=models.CASCADE)
    worker = models.OneToOneField(
        Worker, blank=False, null=False, on_delete=models.CASCADE)
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


class Agent(models.Model):
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
    
    class Meta:
        abstract = True

class Client(Agent):
    pass

class Supplier(Agent):
    pass

class Contract(models.Model):
    contractId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    contract_no = models.CharField(max_length=255, blank=True, null=True)
    dateofcreation = models.DateField(max_length=255, blank=True, null=True)
    duration = models.DateField(max_length=255, blank=True, null=True)
    formofcontract = models.CharField(max_length=255, blank=True, null=True)
    contractupload = models.FileField(
        upload_to="", blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.contract_no)
    
    class Meta:
        abstract = True

class Internal(Contract):
    supervisor = models.OneToOneField(
        Supervisor, blank=False, null=False, on_delete=models.CASCADE)
    manager = models.OneToOneField(
        Manager, blank=False, null=False, on_delete=models.CASCADE)
    accountant = models.OneToOneField(
        Accountant, blank=False, null=False, on_delete=models.CASCADE)
    worker = models.OneToOneField(
        Worker, blank=False, null=False, on_delete=models.CASCADE)

class External(Contract):
    client = models.OneToOneField(
        Client, blank=False, null=False, on_delete=models.CASCADE)
    supplier = models.OneToOneField(
        Supplier, blank=False, null=False, on_delete=models.CASCADE)

