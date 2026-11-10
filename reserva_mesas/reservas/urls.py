from django.urls import path
from . import views

urlpatterns = [
    path('', views.MesaListView.as_view(), name='mesa_list'),
    path('<int:pk>/', views.MesaDetailView.as_view(), name='mesa_detail'),
    path('crear/', views.MesaCreateView.as_view(), name='mesa_create'),
    path('<int:pk>/editar/', views.MesaUpdateView.as_view(), name='mesa_update'),
    path('<int:pk>/eliminar/', views.MesaDeleteView.as_view(), name='mesa_delete'),
]