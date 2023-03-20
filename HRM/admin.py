from django.contrib import admin

# Register your models here.
from .models import Department
from .models import Employee
from .models import Document
from .models import Supplier



admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Document)
admin.site.register(Supplier)
