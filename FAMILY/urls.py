from django.urls import path
from .import views

urlpatterns = [
    #department Building
    path('buildings/',views.getBuildings, name="buildings"),
    path('buildings/<str:pk>/update/',views.updateBuilding, name="update-building"),
    path('buildings/<str:pk>/delete/',views.deleteBuilding, name="delete-building"),
    path('buildings/create/',views.createBuilding, name="create-building"),
    path('buildings/<str:pk>/',views.getBuilding, name="building"),



]    
