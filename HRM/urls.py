from django.urls import path
from .import views

urlpatterns = [
    #department management
    path('departments/',views.getDepartments, name="departments"),
    path('departments/<str:pk>/update/',views.updateDepartment, name="update-department"),
    path('departments/<str:pk>/delete/',views.deleteDepartment, name="delete-department"),
    path('departments/<str:parentid>/create/',views.createDepartment, name="create-department"),
    path('departments/<str:pk>/',views.getDepartment, name="department"),
    

    #employee management
    path('employees/',views.getEmployees, name="employees"),
    path('employees/<str:pk>/update/',views.updateEmployee, name="update-employee"),
    path('employees/<str:pk>/delete/',views.deleteEmployee, name="delete-employee"),
    path('employees/<str:parentid>/create/',views.createEmployee, name="create-employee"),
    path('employees/<str:pk>/',views.getEmployee, name="employee"),
 


 #document management
    path('documents/',views.getDocuments, name="documents"),
    #path('documents/<str:pk>/update/',views.updateDocument, name="update-document"),
    #path('documents/<str:pk>/delete/',views.deleteDocument, name="delete-document"),
    #path('documents/<str:parentid>/create/',views.createDocument, name="create-document"),
    path('documents/<str:pk>/',views.getDocument, name="document"),
 
]