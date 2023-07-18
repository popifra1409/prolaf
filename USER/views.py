from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CredentialsSerializer
from .models import Credentials
from rest_framework.decorators import api_view


@api_view(['POST'])
def getCredential(self, request):
    pseudo = request.data.get('pseudo')
    password = request.data.get('password')

    try:               
        Credential = Credentials.objects.get(pseudo=pseudo, password=password)
        serializer = CredentialsSerializer(Credential)
        return Response(serializer.data)
    except Credentials.DoesNotExist:              
        return Response({'error': 'Invalid credentials'}, status=400)





"""from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Credentials
from .serializers import CredentialsSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse


# ============== Login Checked ====================



def login(request):
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo')
        password = request.POST.get('password')

        user = Credentials(request, pseudo=pseudo, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message': 'Invalid request method'}, status=400)

# ============== Credential management ====================
# get all credentials
@api_view(['GET'])
def getCredentials(request):
    credentials = Credentials.objects.all()
    serializer = CredentialsSerializer(credentials, many=True)
    return Response(serializer.data)

#get a single credentials
@api_view(['GET'])
def getCredential(request, pk):
    credential = Credentials.objects.get(userId=pk)
    serializer = CredentialsSerializer(credential, many=False)
    return Response(serializer.data)

#Update a single credentials
@api_view(['PUT'])
def updateCredential(request, pk):
    data = request.data
    Credential = Credentials.objects.get(userId=pk)
    serializer = CredentialsSerializer(instance=Credential, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

#create a single credential
@api_view(['POST'])
def createCredential(request):
    data = request.data
    credential = Credentials.objects.create(
        username=data['username'],
        pseudo=data['pseudo'],
        password=data['password']
        
    )
    serializer = CredentialsSerializer(credential, many=False)
    return Response(serializer.data)  

#delete a single credentials
@api_view(['DELETE'])
def deleteCredential(request, pk):
    credential = Credentials.objects.get(userId=pk)
    credential.delete()
    return Response('Credential was deleted!')  """