from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Al quitar 'mesas/' de aquí, delegamos toda la raíz a tu app
    path('', include('reservas.urls')), 
]