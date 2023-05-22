from django.contrib import admin



# Register your models here.
from .models import Building
from .models import Lodge
from .models import Family
from .models import Pig
from .models import Parameter
from .models import Pig_ParamRegistration
from .models import Pig_LodgeRegistration



admin.site.register(Building)
admin.site.register(Lodge)
admin.site.register(Family)
admin.site.register(Pig)
admin.site.register(Parameter)
admin.site.register(Pig_ParamRegistration)
admin.site.register(Pig_LodgeRegistration)