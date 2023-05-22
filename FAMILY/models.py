import uuid
from django.db import models
import random
import datetime
from datetime import timedelta, date
from django.utils import timezone
from django.utils.timezone import make_aware



# Buildings Model
class Building(models.Model):
    buildingId =  models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    building_name = models.CharField(max_length=100, blank=False, null=False)
    building_description = models.CharField(max_length=200, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.building_name) 


# Lodges Model
class Lodge(models.Model):
    lodgeId =  models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    building = models.ForeignKey(
        Building, blank=False, null=False, on_delete=models.CASCADE)        
    lodge_name = models.CharField(max_length=50, blank=False, null=False)
    lodge_description = models.CharField(max_length=200, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.lodge_name)                


# Family Model
class Family(models.Model):
    familyId =  models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    building = models.ForeignKey(
        Building, blank=True, null=True, on_delete=models.SET_NULL)    
    family_name = models.CharField(max_length=50, blank=False, null=False)
    family_description = models.CharField(max_length=200, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)     

    def __str__(self):
        return str(self.family_name)


# Members Model
class Member(models.Model):

    GENDER_CHOICES = (('male', 'Male'), ('female',
                      'Female'))               

    memberId =  models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    family = models.ForeignKey(
        Family, blank=False, null=False, on_delete=models.CASCADE) 
    lodge = models.ForeignKey(
        Lodge, blank=True, null=True, on_delete=models.SET_NULL)     
    member_name = models.CharField(max_length=150, blank=False, null=False)
    birthdate = models.DateField(max_length=150,blank=True, null=True)   
    gender = models.CharField(
        max_length=20, blank=True, null=True, choices= GENDER_CHOICES, default='Male')
    generation = models.IntegerField(default=0, editable=False)   
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.member_name)

    class Meta:
        abstract = True

class Pig(Member):
    mother = models.ForeignKey(
        "self", related_name="Mother",  null=True, blank=True, on_delete=models.SET_NULL)   
    father = models.ForeignKey(
        "self", related_name="Father",  null=True, blank=True, on_delete=models.SET_NULL)
    post_weaning = models.DateTimeField(editable=False)
    pre_magnification = models.DateTimeField(editable=False, null=True)
    magnification = models.DateTimeField(editable=False, null=True)        
            

    def save(self, *args, **kwargs): 

        if self.mother:
            #get member corresponding to the mother
            member = Pig.objects.get(memberId=self.mother.memberId)
            self.generation = member.generation + 1

        birthdate = datetime.datetime.strptime(self.birthdate,'%Y-%m-%d')
        self.post_weaning = make_aware(birthdate + timedelta(days=30))
        self.pre_magnification = make_aware(birthdate + timedelta(days=60))
        self.magnification = make_aware(birthdate + timedelta(days=90))
        super(Pig, self).save(*args, **kwargs)
        
     


#Parameter Model
class Parameter(models.Model):
    parameterId =  models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=150, blank=False, null=False)    
    unit = models.CharField(max_length=15, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.name)


 #Parameter Registration Model
class Param_Registration(models.Model):
    paramRegistrationId =  models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)          
    parameter = models.ForeignKey(
        Parameter, blank=False, null=False, on_delete=models.CASCADE)               
    value = models.CharField(max_length=20,  blank= False, null= False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True

class Pig_ParamRegistration(Param_Registration):
    pig_name = models.ForeignKey(
        "pig",  null=True, blank=True, on_delete=models.SET_NULL)
        
    def __str__(self):
        return str(self.pig_name)




# LodgesRegistration Model
class Lodge_Registration(models.Model):
    lodgeRegistrationId =  models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    lodge = models.ForeignKey(
        Lodge, blank=False, null=False, on_delete=models.CASCADE)            
    enteryDate = models.DateField(blank=True, null=True)
    enteryReason = models.CharField(max_length=200, blank=False, null=True)
    weight = models.IntegerField(blank=True, null=True)
    isFinSejour = models.BooleanField(max_length=5, default=False)
    leavingDate = models.DateField(blank=True, null=True)
    leavingReason = models.CharField(max_length=200, blank=False, null=True) 
    duration = models.IntegerField(editable=False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.lodge) 

    def save(self, *args, **kwargs):
        #This works for the Django admin but not for the API
        now = timezone.now().date()
        self.duration = (now - self.enteryDate).days
        
        #This works for the API but not for the django admin
        #newentery = self.enteryDate.strftime('%m/%d/%Y')
        enteryDate = datetime.datetime.strptime(self.enteryDate,'%Y-%m-%d')
        now = datetime.datetime.today()
        self.duration = (now - enteryDate).days

        super(Lodge_Registration, self).save(*args, **kwargs)


    class Meta:
        abstract = True

class Pig_LodgeRegistration(Lodge_Registration):
    pig_name = models.ForeignKey(
        "pig",  null=True, blank=True, on_delete=models.SET_NULL)
        
    def __str__(self):
        return str(self.pig_name)
        

