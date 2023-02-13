from django.contrib import admin

# Register your models here.
from .models import Department
from .models import Manager
from .models import Document
from .models import Supplier
from .models import Supplier_cont

admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Document)
admin.site.register(Supplier)
admin.site.register(Supplier_cont)
