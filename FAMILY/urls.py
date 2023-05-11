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
    path('members_post_weaning/',views.is_near_post_weaning, name="post_weaning"),
    path('members_pre_magnification/',views.is_near_pre_magnification, name="pre_magnification"),
    path('members_magnification/',views.is_near_magnification, name="magnification"),


#Parameter urls
    path('parameters/',views.getParameters, name="parameters"),
    path('parameters/<str:pk>/update/',views.updateParameter, name="update-Parameter"),
    path('parameters/<str:pk>/delete/',views.deleteParameter, name="delete-Parameter"),
    path('parameters/create/',views.createParameter, name="create-Parameter"),
    path('parameters/<str:pk>/',views.getParameter, name="Parameter"),


#Parameter urls
    path('param_Registrations/',views.getParam_Registrations, name="param_Registrations"),
    path('param_Registrations/<str:pk>/update/',views.updateParam_Registration, name="update-param_Registration"),
    path('param_Registrations/<str:pk>/delete/',views.deleteParam_Registration, name="delete-param_Registration"),
    path('param_Registrations/<str:memberid>/<str:nameid>/create/',views.createParam_Registration, name="create-param_Registration"),
    path('param_Registrations/<str:pk>/',views.getParam_Registration, name="param_Registration"),


]    
