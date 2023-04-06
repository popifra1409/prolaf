from django.contrib import admin

# Register your models here.
from .models import Building
from .models import Lodge
from .models import Family
from .models import Member



admin.site.register(Building)
admin.site.register(Lodge)
admin.site.register(Family)
admin.site.register(Member)