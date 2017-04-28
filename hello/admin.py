from django.contrib import admin

# Register your models here.
from .models import Building, BuildingInstance

admin.site.register(Building)
admin.site.register(BuildingInstance)