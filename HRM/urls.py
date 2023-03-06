from django.urls import path
from .import views

urlpatterns = [
    #department management
    #path('', views.getRoutes, name="routes"),
    path('departments/',views.getDepartments, name="departments"),
    path('departments/<str:pk>/',views.getDepartment, name="department"),
    

    #manager management
    #path('', views.getRoutes, name="routes")
    path('employees/',views.getEmployees, name="managers"),
    path('employees/<str:pk>/',views.getEmployee, name="manager"),
 
]