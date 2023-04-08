from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Building, Lodge, Family, Member
from .serializers import BuildingSerializer, LodgeSerializer, FamilySerializer, MemberSerializer


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



# ============== Members management ====================
# get all members
@api_view(['GET'])
def getMembers(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)

#get a single member
@api_view(['GET'])
def getMember(request, pk):
    member = Member.objects.get(memberId=pk)
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data)

#Update a single member
@api_view(['PUT'])
def updateMember(request, pk):
    data = request.data
    member = Member.objects.get(memberId=pk)
    serializer = MemberSerializer(instance=member, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single member
@api_view(['POST'])
def createMember(request, familyid, lodgeid, motherid, fatherid):
    data = request.data
    family = Family.objects.get(familyId=familyid)
    lodge = Lodge.objects.get(lodgeId=lodgeid)
    mother = Member.objects.get(memberId=motherid)
    father = Member.objects.get(memberId=fatherid)
    member = Member.objects.create(
        member_name=data['member_name'],
        family= family,
        lodge= lodge,
        birthdate=data['birthdate'],
        post_weaning=data['post_weaning'],
        mother=mother,
        father=father,
        gender=data['gender']
        
    )
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data) 

#delete a single member
@api_view(['DELETE'])
def deleteMember(request, pk):
    member = Member.objects.get(memberId=pk)
    member.delete()
    return Response('Member was deleted!')        