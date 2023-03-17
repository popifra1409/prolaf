from django.urls import path
from .import views

urlpatterns = [
    #department management
    path('departments/',views.getDepartments, name="departments"),
    path('departments/<str:pk>/update/',views.updateDepartment, name="update-department"),
    path('departments/<str:pk>/delete/',views.deleteDepartment, name="delete-department"),
    path('departments/<str:parentid>/create/',views.createDepartment, name="create-department"),
    path('departments/<str:pk>/',views.getDepartment, name="department"),
    

    #manager management
    #path('', views.getRoutes, name="routes")
    path('employees/',views.getEmployees, name="managers"),
    path('employees/<str:pk>/',views.getEmployee, name="manager"),
 
]