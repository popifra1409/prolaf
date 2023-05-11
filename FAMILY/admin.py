from django.contrib import admin

# Register your models here.
from .models import Building
from .models import Lodge
from .models import Family
from .models import Member
from .models import Parameter
from .models import Param_Registration


admin.site.register(Building)
admin.site.register(Lodge)
admin.site.register(Family)
admin.site.register(Member)
admin.site.register(Parameter)
admin.site.register(Param_Registration)