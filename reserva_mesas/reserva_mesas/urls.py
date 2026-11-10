from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # <-- Importamos esta vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mesas/', include('reservas.urls')),
    
    # Esta línea hace que la ruta vacía (la raíz) redirija a /mesas/
    path('', RedirectView.as_view(url='/mesas/', permanent=True)), 
]