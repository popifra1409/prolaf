import uuid
from django.db import models
import random
import datetime
from datetime import timedelta, date


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
    birthdate = models.DateField(blank=True, null=True)
    post_weaning = models.DateField(editable=False)
    mother = models.ForeignKey(
        "self", related_name="Mother",  null=True, blank=True, on_delete=models.SET_NULL)   
    father = models.ForeignKey(
        "self", related_name="Father",  null=True, blank=True, on_delete=models.SET_NULL)   
    gender = models.CharField(
        max_length=20, blank=True, null=True, choices= GENDER_CHOICES, default='Male')
    generation = models.IntegerField(default=0, editable=False)   
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.member_name)

    """ #post_weaning alert
    def is_near_post_weaning(self):
        post_weaning_date = self.post_weaning
        now = timezone.now().date()
        if(post_weaning_date - now)<=7:
            return True
        return False    

 """

    def save(self, *args, **kwargs):
        if self.mother:
            #get member corresponding to the mother
            member = Member.objects.get(memberId=self.mother.memberId)
            self.generation = member.generation + 1 

        self.post_weaning = self.birthdate + timedelta(days=30)
        super(Member, self).save(*args, **kwargs)

        

