from django.contrib import admin

# Register your models here.
from .models import Department
from .models import Employee
from .models import Document
from .models import Internal
from .models import External
from .models import Agent



admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Document)
admin.site.register(Internal)
admin.site.register(External)
admin.site.register(Agent)
