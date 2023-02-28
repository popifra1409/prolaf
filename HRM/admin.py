from django.contrib import admin

# Register your models here.
from .models import Department
from .models import Manager
from .models import Document
from .models import Supplier

admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Document)
admin.site.register(Supplier)
