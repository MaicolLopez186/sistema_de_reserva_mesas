from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import mesa, cliente # Importamos tu modelo exacto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# 1. Visualización y Filtros (READ - List)
@method_decorator(login_required, name='dispatch')
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
@method_decorator(login_required, name='dispatch')
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




    # 1. Lista y Filtros de Clientes
class ClienteListView(ListView):
    model = cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Capturamos los filtros
        nombre_filtro = self.request.GET.get('nombre')
        apellido_filtro = self.request.GET.get('apellido')
        edad_min = self.request.GET.get('edad_min')
        solo_vip = self.request.GET.get('vip')

        if nombre_filtro:
            queryset = queryset.filter(nombre__icontains=nombre_filtro)
        if apellido_filtro:
            queryset = queryset.filter(apellido__icontains=apellido_filtro)
        if edad_min:
            queryset = queryset.filter(edad__gte=int(edad_min))
        if solo_vip == 'on':
            queryset = queryset.filter(vip=True)

        return queryset

# 2. Detalle del Cliente
class ClienteDetailView(DetailView):
    model = cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = 'cliente'

# 3. Crear Cliente
class ClienteCreateView(CreateView):
    model = cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nombre', 'apellido', 'edad', 'telefono', 'correo', 'vip']
    success_url = reverse_lazy('cliente_list')

# 4. Editar Cliente
class ClienteUpdateView(UpdateView):
    model = cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nombre', 'apellido', 'edad', 'telefono', 'correo', 'vip']
    success_url = reverse_lazy('cliente_list')

# 5. Eliminar Cliente
class ClienteDeleteView(DeleteView):
    model = cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
# NUEVA VISTA PÚBLICA (Home)
class HomeView(ListView):
    model = mesa
    template_name = 'home.html'
    context_object_name = 'mesas'
    # Queremos mostrar TODAS las mesas, pero puedes filtrar si lo deseas
