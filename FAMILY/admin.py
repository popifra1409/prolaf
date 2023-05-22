from django.contrib import admin



# Register your models here.
from .models import Building
from .models import Lodge
from .models import Family
from .models import Pig
from .models import Parameter
from .models import ParamRegistration
from .models import Lodge_Registration



admin.site.register(Building)
admin.site.register(Lodge)
admin.site.register(Family)
admin.site.register(Pig)
admin.site.register(Parameter)
admin.site.register(ParamRegistration)
admin.site.register(Lodge_Registration)