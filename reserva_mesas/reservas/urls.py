from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Redirección principal
    path('', RedirectView.as_view(url='/mesas/', permanent=True)),

    # --- RUTAS DE MESAS ---
    path('mesas/', views.MesaListView.as_view(), name='mesa_list'),
    path('mesas/<int:pk>/', views.MesaDetailView.as_view(), name='mesa_detail'),
    path('mesas/crear/', views.MesaCreateView.as_view(), name='mesa_create'),
    path('mesas/<int:pk>/editar/', views.MesaUpdateView.as_view(), name='mesa_update'),
    path('mesas/<int:pk>/eliminar/', views.MesaDeleteView.as_view(), name='mesa_delete'),

    # --- RUTAS DE CLIENTES ---
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/crear/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
]