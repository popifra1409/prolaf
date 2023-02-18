from django.urls import path
from .import views

urlpatterns = [
    #department management
    #path('', views.getRoutes, name="routes"),
    path('departments/',views.getDepartments, name="departments"),
    path('departments/<str:pk>/',views.getDepartment, name="department"),
    

    #employee management
    #path('', views.getRoutes, name="routes")
    path('employees/',views.getEmployees, name="employees"),
    path('employees/<str:pk>/',views.getEmployee, name="employee"),
  

    #document management
    #path('', views.getRoutes, name="routes")
    path('employees/',views.getEmployees, name="employees"),
    path('employees/<str:pk>/',views.getEmployee, name="employee"),


    #contract management
    #path('', views.getRoutes, name="routes")
    path('contracts/',views.getContracts, name="contracts"),
    path('contracts/<str:pk>/',views.getContract, name="contract"),


    #agents management
    #path('', views.getRoutes, name="routes")
    path('agents/',views.getAgents, name="agents"),
    path('agents/<str:pk>/',views.getAgent, name="agent"),
 
]