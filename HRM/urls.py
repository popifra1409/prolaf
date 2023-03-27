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
    path('employees/<str:supid>/<str:departmentid>/create/',views.createEmployee, name="create-employee"),
    path('employees/<str:pk>/',views.getEmployee, name="employee"),
 


 #document management
    path('documents/',views.getDocuments, name="documents"),
    path('documents/<str:pk>/update/',views.updateDocument, name="update-document"),
    path('documents/<str:pk>/delete/',views.deleteDocument, name="delete-document"),
    path('documents/<str:employeeid>/create/',views.createDocument, name="create-document"),
    path('documents/<str:pk>/',views.getDocument, name="document"),


#Internal contract management
    path('internals/',views.getInternals, name="internals"),
    path('internals/<str:pk>/update/',views.updateInternal, name="update-internal"),
    path('internals/<str:pk>/delete/',views.deleteInternal, name="delete-internal"),
    path('internals/<str:employeeid>/create/',views.createInternal, name="create-internal"),
    path('internals/<str:pk>/',views.getInternal, name="internal"),    
 

 #External contract management
    path('externals/',views.getExternals, name="externals"),
    path('externals/<str:pk>/update/',views.updateExternal, name="update-external"),
    path('externals/<str:pk>/delete/',views.deleteExternal, name="delete-external"),
    path('externals/<str:agentid>/create/',views.createExternal, name="create-external"),
    path('externals/<str:pk>/',views.getExternal, name="external"),    
 

 #Agent management
    path('agents/',views.getAgents, name="agents"),
    path('agents/<str:pk>/update/',views.updateAgent, name="update-agent"),
    path('agents/<str:pk>/delete/',views.deleteAgent, name="delete-agent"),
    path('agents/create/',views.createAgent, name="create-agent"),
    path('agents/<str:pk>/',views.getAgent, name="agent"),    
 

]