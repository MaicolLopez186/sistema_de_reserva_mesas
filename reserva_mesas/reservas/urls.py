from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # EL HOME AHORA ES LA PÁGINA PRINCIPAL
    path('', views.HomeView.as_view(), name='home'),

    # --- RUTAS PROTEGIDAS ---
    path('mesas/', views.MesaListView.as_view(), name='mesa_list'),
    path('mesas/<int:pk>/', views.MesaDetailView.as_view(), name='mesa_detail'),
    path('mesas/crear/', views.MesaCreateView.as_view(), name='mesa_create'),
    path('mesas/<int:pk>/editar/', views.MesaUpdateView.as_view(), name='mesa_update'),
    path('mesas/<int:pk>/eliminar/', views.MesaDeleteView.as_view(), name='mesa_delete'),

  
    # ... (las demás rutas de clientes se quedan igual) ...
]