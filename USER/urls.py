""" from django.urls import path
from .import views

urlpatterns = [
    #credentials management
    path('credentials/',views.getCredentials, name="credentials"),
    path('credentials/<str:pk>/update/',views.updateCredential, name="update-credential"),
    path('credentials/<str:pk>/delete/',views.deleteCredential, name="delete-credential"),
    path('credentials/create/',views.createCredential, name="create-credential"),
    path('credentials/<str:pk>/',views.getCredential, name="credential"), 
    path('credentials/token/',views.login, name="login"),  

]
 """
from django.urls import path
from .import views

urlpatterns = [
    path('credentials/', views.getCredential, name="login"),
]
