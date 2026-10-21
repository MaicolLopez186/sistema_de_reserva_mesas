from django.contrib import admin
from .models import mesa
from .models import cliente

admin.site.register(mesa)
admin.site.register(cliente)