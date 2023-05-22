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
    path('pigs/',views.getPigs, name="pigs"),
    path('pigs/<str:pk>/update/',views.updatePig, name="update-Pig"),
    path('pigs/<str:pk>/delete/',views.deletePig, name="delete-Pig"),
    path('pigs/<str:familyid>/<str:lodgeid>/<str:motherid>/<str:fatherid>/create/',views.createPig, name="create-Pig"),
    path('pigs/<str:pk>/',views.getPig, name="pig"),
    path('pigs_post_weaning/',views.is_near_post_weaning, name="post_weaning"),
    path('pigs_pre_magnification/',views.is_near_pre_magnification, name="pre_magnification"),
    path('pigs_magnification/',views.is_near_magnification, name="magnification"),


#Parameter urls
    path('parameters/',views.getParameters, name="parameters"),
    path('parameters/<str:pk>/update/',views.updateParameter, name="update-Parameter"),
    path('parameters/<str:pk>/delete/',views.deleteParameter, name="delete-Parameter"),
    path('parameters/create/',views.createParameter, name="create-Parameter"),
    path('parameters/<str:pk>/',views.getParameter, name="Parameter"),


#Pig_ParamRegistrations urls
    path('pig_ParamRegistrations/',views.getPig_ParamRegistrations, name="pig_ParamRegistrations"),
    path('pig_ParamRegistrations/<str:pk>/update/',views.updatePig_ParamRegistration, name="update-pig_ParamRegistration"),
    path('pig_ParamRegistrations/<str:pk>/delete/',views.deletePig_ParamRegistration, name="delete-pig_ParamRegistration"),
    path('pig_ParamRegistrations/<str:memberid>/<str:nameid>/create/',views.createPig_ParamRegistration, name="create-pig_ParamRegistration"),
    path('pig_ParamRegistrations/<str:pk>/',views.gePig_ParamRegistration, name="pig_ParamRegistration"),


#Lodge_Registration urls
    path('pig_LodgeRegistrations/',views.getPig_LodgeRegistrations, name="lodge_Registrations"),
    path('pig_LodgeRegistrations/<str:pk>/update/',views.updatePig_LodgeRegistration, name="update-pig_LodgeRegistration"),
    path('pig_LodgeRegistrations/<str:pk>/delete/',views.deletePig_LodgeRegistration, name="delete-pig_LodgeRegistration"),
    path('pig_LodgeRegistrations/<str:memberid>/<str:lodgeid>/create/',views.createPig_LodgeRegistration, name="create-pig_LodgeRegistration"),
    path('pig_LodgeRegistrations/<str:pk>/',views.getPig_LodgeRegistration, name="pig_LodgeRegistration"),    


]    
