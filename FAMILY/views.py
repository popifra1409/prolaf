from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Building, Lodge, Family, Pig, Parameter,ParamRegistration, Lodge_Registration
from .serializers import BuildingSerializer, LodgeSerializer, FamilySerializer, PigSerializer, ParameterSerializer, ParamRegistrationSerializer, LodgeRegistrationSerializer


# ============== Building management ====================
# get all buildings
@api_view(['GET'])
def getBuildings(request):
    buildings = Building.objects.all()
    serializer = BuildingSerializer(buildings, many=True)
    return Response(serializer.data)

#get a single building
@api_view(['GET'])
def getBuilding(request, pk):
    building = Building.objects.get(buildingId=pk)
    serializer = BuildingSerializer(building, many=False)
    return Response(serializer.data)

#Update a single building
@api_view(['PUT'])
def updateBuilding(request, pk):
    data = request.data
    building = Building.objects.get(buildingId=pk)
    serializer = BuildingSerializer(instance=building, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single building
@api_view(['POST'])
def createBuilding(request):
    data = request.data
    building = Building.objects.create(
        building_name=data['building_name'],
        building_description=data['building_description'],
        
    )
    serializer = BuildingSerializer(building, many=False)
    return Response(serializer.data)  

#delete a single building
@api_view(['DELETE'])
def deleteBuilding(request, pk):
    building = Building.objects.get(buildingId=pk)
    building.delete()
    return Response('Building was deleted!')  


# ============== Lodge management ====================
# get all lodges
@api_view(['GET'])
def getLodges(request):
    lodges = Lodge.objects.all()
    serializer = LodgeSerializer(lodges, many=True)
    return Response(serializer.data)

#get a single lodge
@api_view(['GET'])
def getLodge(request, pk):
    lodge = Lodge.objects.get(lodgeId=pk)
    serializer = LodgeSerializer(lodge, many=False)
    return Response(serializer.data)

#Update a single lodge
@api_view(['PUT'])
def updateLodge(request, pk):
    data = request.data
    lodge = Lodge.objects.get(lodgeId=pk)
    serializer = LodgeSerializer(instance=lodge, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single lodge
@api_view(['POST'])
def createLodge(request, buildingid):
    data = request.data
    building = Building.objects.get(buildingId=buildingid)
    lodge = Lodge.objects.create(
        lodge_name=data['lodge_name'],
        building= building,
        lodge_description=data['lodge_description'],
        capacity=data['capacity']
        
    )
    serializer = LodgeSerializer(lodge, many=False)
    return Response(serializer.data) 

#delete a single lodge
@api_view(['DELETE'])
def deleteLodge(request, pk):
    lodge = Lodge.objects.get(lodgeId=pk)
    lodge.delete()
    return Response('Lodge was deleted!')    


    # ============== Family management ====================
# get all families
@api_view(['GET'])
def getFamilies(request):
    families = Family.objects.all()
    serializer = FamilySerializer(families, many=True)
    return Response(serializer.data)

#get a single family
@api_view(['GET'])
def getFamily(request, pk):
    family = Family.objects.get(familyId=pk)
    serializer = FamilySerializer(family, many=False)
    return Response(serializer.data)

#Update a single family
@api_view(['PUT'])
def updateFamily(request, pk):
    data = request.data
    family = Family.objects.get(familyId=pk)
    serializer = FamilySerializer(instance=family, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single family
@api_view(['POST'])
def createFamily(request, buildingid):
    data = request.data
    building = Building.objects.get(buildingId=buildingid)
    family = Family.objects.create(
        family_name=data['family_name'],
        building= building,
        family_description=data['family_description']
        
    )
    serializer = FamilySerializer(family, many=False)
    return Response(serializer.data) 

#delete a single lodge
@api_view(['DELETE'])
def deleteFamily(request, pk):
    family = Family.objects.get(familyId=pk)
    family.delete()
    return Response('Family was deleted!')       



# ============== Pigs management ====================
# get all pigs
@api_view(['GET'])
def getPigs(request):
    pigs = Pig.objects.all()
    serializer = PigSerializer(pigs, many=True)
    return Response(serializer.data)

#get a single pig
@api_view(['GET'])
def getPig(request, pk):
    pig = Pig.objects.get(memberId=pk)
    serializer = PigSerializer(pig, many=False)
    return Response(serializer.data)

#Update a single pig
@api_view(['PUT'])
def updatePig(request, pk):
    data = request.data
    pig = Pig.objects.get(memberId=pk)
    serializer = PigSerializer(instance=pig, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single pig
@api_view(['POST'])
def createPig(request, familyid, lodgeid, motherid, fatherid):
    data = request.data
    family = Family.objects.get(familyId=familyid)
    lodge = Lodge.objects.get(lodgeId=lodgeid)
    mother = Pig.objects.get(memberId=motherid)
    father = Pig.objects.get(memberId=fatherid)
    pig = Pig.objects.create(
        member_name=data['member_name'],
        family= family,
        lodge= lodge,
        birthdate=data['birthdate'],
        mother=mother,
        father=father,
        gender=data['gender']
        
    )
    serializer = PigSerializer(pig, many=False)
    return Response(serializer.data) 

#delete a single pig
@api_view(['DELETE'])
def deletePig(request, pk):
    pig = Pig.objects.get(memberId=pk)
    pig.delete()
    return Response('Pig was deleted!')


# ============== Parameter management ====================
# get all parameters
@api_view(['GET'])
def getParameters(request):
    parameters = Parameter.objects.all()
    serializer = ParameterSerializer(parameters, many=True)
    return Response(serializer.data)

#get a single parameter
@api_view(['GET'])
def getParameter(request, pk):
    parameter = Parameter.objects.get(parameterId=pk)
    serializer = ParameterSerializer(parameter, many=False)
    return Response(serializer.data)

#Update a single parameter
@api_view(['PUT'])
def updateParameter(request, pk):
    data = request.data
    parameter = Parameter.objects.get(parameterId=pk)
    serializer = ParameterSerializer(instance=parameter, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single member
@api_view(['POST'])
def createParameter(request):
    data = request.data
    parameter = Parameter.objects.create(
        name=data['name'],
        unit=data['unit']       
    )
    serializer = ParameterSerializer(parameter, many=False)
    return Response(serializer.data) 

#delete a single parameter
@api_view(['DELETE'])
def deleteParameter(request, pk):
    parameter = Parameter.objects.get(parameterId=pk)
    parameter.delete()
    return Response('Parameter was deleted!')



# ============== ParamRegistration management ====================
# get all ParamRegistrations
@api_view(['GET'])
def getParamRegistrations(request):
    paramRegistrations = ParamRegistration.objects.all()
    serializer = ParamRegistrationSerializer(paramRegistrations, many=True)
    return Response(serializer.data)

#get a single ParamRegistration
@api_view(['GET'])
def geParamRegistration(request, pk):
    paramRegistration = ParamRegistration.objects.get(paramRegistrationId=pk)
    serializer = ParamRegistrationSerializer(paramRegistration, many=False)
    return Response(serializer.data)

#Update a single Param_Registration
@api_view(['PUT'])
def updateParamRegistration(request, pk):
    data = request.data
    paramRegistration = ParamRegistration.objects.get(paramRegistrationId=pk)
    serializer = ParamRegistrationSerializer(instance=paramRegistration, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single ParamRegistration
@api_view(['POST'])
def createParamRegistration(request, memberid, nameid):
    data = request.data
    member = Pig.objects.get(memberId=memberid)
    parameter = Parameter.objects.get(parameterId=nameid)
    param_Registration = ParamRegistration.objects.create(
        pig_name = member,
        parameter = parameter,
        value=data['value']     
    )
    serializer = ParamRegistrationSerializer(param_Registration, many=False)
    return Response(serializer.data) 

#delete a single param_Registration
@api_view(['DELETE'])
def deleteParamRegistration(request, pk):
    paramRegistration = ParamRegistration.objects.get(paramRegistrationId=pk)
    paramRegistration.delete()
    return Response('ParamRegistration was deleted!')


#post_weaning alert
@api_view(['GET'])
def is_near_post_weaning(request): 
    now = timezone.now().date()
    members = Member.objects.filter(post_weaning__gt=now, post_weaning__lte=now+timedelta(days=7))
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)

#pre_magnification alert
@api_view(['GET'])
def is_near_pre_magnification(request):
    now = timezone.now().date()
    members = Member.objects.filter(pre_magnification__gt=now, pre_magnification__lte=now+timedelta(days=7)) #lte=less than or equal to
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)

 #magnification alert
@api_view(['GET'])
def is_near_magnification(request):
    now = timezone.now().date()
    members = Member.objects.filter(magnification__gt=now, magnification__lte=now+timedelta(days=7))
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data) 


    # ============== Lodge_Registration management ====================
# get all Lodge_Registration
@api_view(['GET'])
def getLodge_Registrations(request):
    lodge_Registrations = Lodge_Registration.objects.all()
    serializer = LodgeRegistrationSerializer(lodge_Registrations, many=True)
    return Response(serializer.data)

#get a single Lodge_Registration
@api_view(['GET'])
def getLodge_Registration(request, pk):
    lodge_Registration = Lodge_Registration.objects.get(lodgeRegistrationId=pk)
    serializer = LodgeRegistrationSerializer(lodge_Registration, many=False)
    return Response(serializer.data)

#Update a single Lodge_Registration
@api_view(['PUT'])
def updateLodge_Registration(request, pk):
    data = request.data
    lodge_Registration = Lodge_Registration.objects.get(lodgeRegistrationId=pk)
    serializer = LodgeRegistrationSerializer(instance=lodge_Registration, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single Lodge_Registration
@api_view(['POST'])
def createLodge_Registration(request, memberid, lodgeid):
    data = request.data
    member = Member.objects.get(memberId=memberid)
    lodge =  Lodge.objects.get(lodgeId=lodgeid)
    lodge_Registration = Lodge_Registration.objects.create(
        member = member,
        lodge = lodge,
        enteryDate=data['enteryDate'],
        enteryReason=data['enteryReason'],
        weight=data['weight'],
        isFinSejour=data['isFinSejour'],
        leavingDate=data['leavingDate'],
        leavingReason=data['leavingReason']      
    )
    serializer = LodgeRegistrationSerializer(lodge_Registration, many=False)
    return Response(serializer.data) 

#delete a single lodge_Registration
@api_view(['DELETE'])
def deleteLodge_Registration(request, pk):
    lodge_Registration = Lodge_Registration.objects.get(lodgeRegistrationId=pk)
    lodge_Registration.delete()
    return Response('Lodge_Registration was deleted!')

