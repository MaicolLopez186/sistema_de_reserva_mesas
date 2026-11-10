from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import mesa # Importamos tu modelo exacto

# 1. Visualización y Filtros (READ - List)
class MesaListView(ListView):
    model = mesa
    template_name = 'mesas/mesa_list.html'
    context_object_name = 'mesas'
    paginate_by = 10 # Opcional

    def get_queryset(self):
        # Obtenemos todas las mesas inicialmente
        queryset = super().get_queryset()
        
        # Capturamos los datos del formulario de filtro (método GET)
        ubicacion_filtro = self.request.GET.get('ubicacion')
        capacidad_min = self.request.GET.get('capacidad_min')
        solo_disponibles = self.request.GET.get('disponible')

        # Filtro por Ubicación (Búsqueda parcial, ignora mayúsculas/minúsculas)
        if ubicacion_filtro:
            queryset = queryset.filter(ubicacion__icontains=ubicacion_filtro)
        
        # Filtro por Capacidad (numero_sillas)
        if capacidad_min:
            # NOTA: Como numero_sillas es un CharField, hacemos la comparación.
            # Si tu base de datos lo requiere, aquí podrías castear el valor.
            queryset = queryset.filter(numero_sillas__gte=capacidad_min)
            
        # Consulta de disponibilidad
        if solo_disponibles == 'on':
            queryset = queryset.filter(disponible=True)

        return queryset

# 2. Ver Detalle (READ - Detail)
class MesaDetailView(DetailView):
    model = mesa
    template_name = 'mesas/mesa_detail.html'
    context_object_name = 'mesa'

# 3. Crear (CREATE)
class MesaCreateView(CreateView):
    model = mesa
    template_name = 'mesas/mesa_form.html'
    # Excluimos 'id_mesa' porque es AutoField
    fields = ['numero_mesa', 'ubicacion', 'numero_sillas', 'disponible', 'color']
    success_url = reverse_lazy('mesa_list')

# 4. Actualizar (UPDATE)
class MesaUpdateView(UpdateView):
    model = mesa
    template_name = 'mesas/mesa_form.html'
    fields = ['numero_mesa', 'ubicacion', 'numero_sillas', 'disponible', 'color']
    success_url = reverse_lazy('mesa_list')

# 5. Eliminar (DELETE)
class MesaDeleteView(DeleteView):
    model = mesa
    template_name = 'mesas/mesa_confirm_delete.html'
    success_url = reverse_lazy('mesa_list')