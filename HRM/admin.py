from django.contrib import admin

# Register your models here.
from .models import Department
from .models import Employee
from .models import Documents
from .models import Agent
from .models import Contract

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Documents)
admin.site.register(Agent)
admin.site.register(Contract)

