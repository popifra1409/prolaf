import uuid
from django.db import models
import random
import datetime

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

    EMPLOYEE_CHOICES = (('supervisor', 'SUPERVISOR'), ('manager', 'MANAGER'), ('accountant',
                        'ACCOUNTANT'), ('worker ', 'WORKER'))                  

    employeeId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    employeeMat = models.CharField(max_length=30, blank=False, null=False, editable=False, unique=True)
    department = models.ForeignKey(
        Department, blank=False, null=False, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(
        "self", related_name="Supervisor",  null=True, blank=True, on_delete=models.SET_NULL)    
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
        null=True, blank=True, upload_to="profiles/", default="")
    function = models.CharField(max_length=255, blank=True, null=True)
    hiringdate = models.DateField(blank=False, null=False)
    seniority = models.IntegerField()
    salary = models.FloatField()
    whatsappnumber = models.CharField(max_length=20, blank=True, null=True)
    facebooklink = models.CharField(max_length=255, blank=True, null=True)
    resourcecontact = models.CharField(max_length=20, blank=True, null=True)
    resourcename = models.CharField(max_length=255, blank=True, null=True)
    isChiefOfDepartment = models.BooleanField(max_length=5, default=False)
    typeofemployee = models.CharField(
        max_length=255, blank=True, null=True, choices= EMPLOYEE_CHOICES, default='WORKER')
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.firstname)

    def save(self, *args, **kwargs):
        #get current date and time
        now = datetime.datetime.now()
        #Generate a random number between 1 to 1000
        rand_num = random.randint(1, 1000)
        #Format the matricule
        if not self.employeeMat:
            self.employeeMat =  f"{'EMP'}-{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{rand_num}"
        super(Employee, self).save(*args, **kwargs)
    

class Document(models.Model):
    documentId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    documentref = models.CharField(max_length=50, blank=False, null=False, editable=False, unique=True)  
    employee = models.OneToOneField(
        Employee, blank=False, null=False, on_delete=models.CASCADE)
    numCni = models.CharField(
        max_length=100, blank=False, null=False, unique=True)
    cniupload = models.FileField(null=False, upload_to="documents/cni/")
    diploma = models.CharField(max_length=255, blank=True, null=True)
    diplomaupload = models.FileField(blank=False, null=False, upload_to="documents/diploma/")
    mariagecertificate = models.FileField(blank=True, null=True, upload_to="documents/mariage/")
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.documentref)

    def save(self, *args, **kwargs):
        #get current date and time
        now = datetime.datetime.now()
        #Generate a random number between 1 to 1000
        rand_num = random.randint(1, 1000)
        #Format the matricule
        if not self.documentref:
            if self.cniupload:
                cni = "ID"
            if self.diplomaupload:
                dip = "DI"
            if self.mariagecertificate:
                mac = "MC"
            else: 
                mac = ""
            self.documentref =  f"{'DOC'}-{cni}{dip}{mac}-{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{rand_num}"
        super(Document, self).save(*args, **kwargs)    


class Agent(models.Model):
    agentId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    AGENT_CHOICES = (('supplier', 'Supplier'), ('client', 'Client'))
    agenttype = models.CharField(
        max_length=255, blank=True, null=True, choices= AGENT_CHOICES)    
    firstname = models.CharField(max_length=255, blank=False, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=False, null=True)
    phone = models.CharField(max_length=255, blank=False, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    niu = models.CharField(max_length=255, blank=False, null=True)
    observation = models.CharField(max_length=255, blank=True, null=True)
    bankaccount = models.CharField(max_length=255, blank=False, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.firstname)
    
    """ class Meta:
        abstract = True

class Client(Agent):
    pass

class Supplier(Agent):
    pass  """

class Contract(models.Model):
    contractId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    contract_no = models.CharField(max_length=255, blank=False, null=True)
    dateofcreation = models.DateField(max_length=255, blank=False, null=True)
    duration = models.DateField(max_length=255, blank=True, null=True)
    formofcontract = models.CharField(max_length=255, blank=False, null=True)
    contractupload = models.FileField(
        upload_to="", blank=False, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.contract_no)

    class Meta:
        abstract = True

class Internal(Contract):
    employee = models.OneToOneField(
        Employee, blank=False, null=False, on_delete=models.CASCADE)          
    

class External(Contract):
    AGENT_CHOICES = (('supplier', 'Supplier'), ('client', 'Client'))
    agenttype = models.CharField(
        max_length=255, blank=False, null=True, choices= AGENT_CHOICES)
    agentname = models.OneToOneField(
    Agent, blank=False, null=True, on_delete=models.CASCADE)
   

                    
    



