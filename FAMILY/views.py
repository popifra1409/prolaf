from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Building
from .serializers import BuildingSerializer


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

#create a single departement
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