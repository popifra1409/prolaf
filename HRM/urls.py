from django.urls import path
from .import views

urlpatterns = [
    #department management
    path('', views.getRoutes, name="routes"),
    path('departments/',views.getDepartments, name="departments"),
    path('departments/<str:pk>/',views.getDepartment, name="department"),
    

    #employee management
  

    #document management

    #contract management


    #agents management
 
]