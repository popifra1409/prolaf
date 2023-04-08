from django.urls import path
from .import views

urlpatterns = [
    #Building urls
    path('buildings/',views.getBuildings, name="buildings"),
    path('buildings/<str:pk>/update/',views.updateBuilding, name="update-building"),
    path('buildings/<str:pk>/delete/',views.deleteBuilding, name="delete-building"),
    path('buildings/create/',views.createBuilding, name="create-building"),
    path('buildings/<str:pk>/',views.getBuilding, name="building"),


#Lodge urls
    path('lodges/',views.getLodges, name="lodges"),
    path('lodges/<str:pk>/update/',views.updateLodge, name="update-lodge"),
    path('lodges/<str:pk>/delete/',views.deleteLodge, name="delete-lodge"),
    path('lodges/<str:buildingid>/create/',views.createLodge, name="create-lodge"),
    path('lodges/<str:pk>/',views.getLodge, name="lodge"),


#Family urls
    path('families/',views.getFamilies, name="families"),
    path('families/<str:pk>/update/',views.updateFamily, name="update-Family"),
    path('families/<str:pk>/delete/',views.deleteFamily, name="delete-Family"),
    path('families/<str:buildingid>/create/',views.createFamily, name="create-Family"),
    path('families/<str:pk>/',views.getFamily, name="family"),


#Member urls
    path('members/',views.getMembers, name="members"),
    path('members/<str:pk>/update/',views.updateMember, name="update-Member"),
    path('members/<str:pk>/delete/',views.deleteMember, name="delete-Member"),
    path('members/<str:familyid>/<str:lodgeid>/<str:motherid>/<str:fatherid>/create/',views.createMember, name="create-Member"),
    path('members/<str:pk>/',views.getMember, name="member"),



]    
