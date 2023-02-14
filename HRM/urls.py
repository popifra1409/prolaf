from django.contrib import admin
from django.urls import path

urlpatterns = [
    #department management
    path('newDepartment/', admin.site.urls),
    path('updateDepartment/', admin.site.urls),
    path('deleteDepartment/', admin.site.urls),
    path('displayDepartment/', admin.site.urls),
    path('allDepartment/', admin.site.urls),

    #employee management
    path('newEmplyoyee/', admin.site.urls),
    path('updateEmployee/', admin.site.urls),
    path('deleteEmployee/', admin.site.urls),
    path('displayEmployee/', admin.site.urls),
    path('allEmployee/', admin.site.urls),

    #document management
    path('newDocument/', admin.site.urls),
    path('updateDocument/', admin.site.urls),
    path('deleteDocument/', admin.site.urls),
    path('displayDocument/', admin.site.urls),
    path('allDocument/', admin.site.urls),

    #contract management
    path('newContract/', admin.site.urls),
    path('updateContract/', admin.site.urls),
    path('deleteContract/', admin.site.urls),
    path('displayContract/', admin.site.urls),
    path('allContract/', admin.site.urls),

    #agents management
    path('newAgent/', admin.site.urls),
    path('updateAgent/', admin.site.urls),
    path('deleteAgent/', admin.site.urls),
    path('displayAgent/', admin.site.urls),
    path('allAgent/', admin.site.urls),
]