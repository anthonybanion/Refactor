
from django.shortcuts import render, redirect
from django.contrib.auth.views import (LoginView, 
                                       LogoutView, 
                                       PasswordChangeView, 
                                       PasswordResetView,
                                     )
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy

from .models import Usuarios,Producto,Categorias,Area,Deposito,EntradaProducto,RegistroIngresoProducto,Patrimonio,Sede,RQ, Persona


from django.views.generic import (CreateView, 
                                  DeleteView, 
                                  DateDetailView,
                                  DetailView,
                                  ListView,
                                  TemplateView, 
                                  UpdateView,
                                  View)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateUserForm, ChangeUserform,LoginForm,ProductoForm,EntradaProductoForm,RegistroIngresoProductoForm,ProductSearchForm,CategoriasForm,PatrimonioForm,AreaForm,DepositoForm,SedeForm, SeleccionarDepositoForm, FiltrarProductosForm, AgregarProductoForm,RQForm, PersonaForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse





# Create your views here.
class Home(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    login_url = "/"
    
class CreateUser(LoginRequiredMixin,CreateView):
    model = Usuarios
    template_name = "registration/createuser.html"
    form_class = CreateUserForm
    success_url = '/home'
    login_url = "/"

  
    
class Login(LoginView):
    model = Usuarios
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url='/'
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Usuario o contraseña incorrectos.')
        return super().form_invalid(form)

 
            
class Logout(LoginRequiredMixin,LogoutView):
    template_name = 'registration/logout.html'
    success_url= reverse_lazy('registration/login.html')
    login_url = "/" 
    
    
class Delete_User(LoginRequiredMixin,DeleteView):
    model = Usuarios
    template_name ="registration/deleteuser.html"
    success_url='/listuser' 
    cancel_url='/listuser'
    login_url = "/"
    
class List_User(LoginRequiredMixin,ListView):
    model = Usuarios
    template_name = "registration/listuser.html"
    login_url = "/"

class EditUserView(LoginRequiredMixin,UpdateView):
    model = Usuarios
    template_name = "registration/edituser.html"
    form_class = ChangeUserform
    success_url = '/listuser'
    login_url = "/"

class DataUser(DetailView):
    model = Usuarios
    template_name = "registration/datauser.html"
    context_object_name = 'user'
    login_url = "/"


##### View Categorias####


class CategoriasView(LoginRequiredMixin,CreateView):
    model = Categorias
    template_name = "categorias/createcategorias.html"
    form_class = CategoriasForm
    success_url = '/home'
    login_url = '/login'

class ListCategorias(LoginRequiredMixin,ListView):
    model = Categorias
    template_name = "categorias/listcategoria.html"
    login_url = "/"

class EditCategoriaView(LoginRequiredMixin,UpdateView):
    model = Categorias
    template_name = "categorias/editcategoria.html"
    form_class = CategoriasForm
    success_url = '/listcategoria'
    login_url = "/"

class Delete_Categoria(LoginRequiredMixin,DeleteView):
    model = Categorias
    template_name ="categorias/deletecategoria.html"
    success_url='/listcategoria' 
    cancel_url='/listcategoria'
    login_url = "/"   




#### View Registro Ingreso

class RegistrarEntrada(LoginRequiredMixin, CreateView):
    model = EntradaProducto
    template_name = 'registrar_entrada.html'
    form_class = EntradaProductoForm
    success_url = '/detalle_producto/' 

class Delete_EP(LoginRequiredMixin,DeleteView):
    model = EntradaProducto
    template_name ="entradaproducto/deleteentradaproducto.html"
    success_url='/detalle_producto/'
    cancel_url='/detalle_producto/'
    login_url = "/"
    


class EditEPView(LoginRequiredMixin,UpdateView):
    model = EntradaProducto
    template_name = "entradaproducto/editentradaproducto.html"
    form_class = EntradaProductoForm
    success_url = '/listentradaproducto'
    login_url = "/"



class CrearRegistroIngreso(View):
    template_name = 'crear_registro_ingreso.html'

    def get(self, request):
        form = RegistroIngresoProductoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistroIngresoProductoForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.save()
            return redirect('lista_registros_ingreso')  # Redirigir a la lista de registros de ingreso
        return render(request, self.template_name, {'form': form})
    


#### View Product




class CreateProduct(LoginRequiredMixin,CreateView):
    model = Producto
    template_name = "productos/create_product.html"
    form_class = ProductoForm
    success_url = "/entradaproducto"
    login_url = "/"

    # def get_success_url(self):
    #     referer = self.request.META.get('HTTP_REFERER')
    #     return referer or reverse_lazy('nombre_de_la_vista_de_redireccion')
    
class ListProduct(LoginRequiredMixin,ListView):
    model = Producto
    template_name = "productos/listproduct.html"
    login_url = "/"

    context_object_name = "productos"

    def get_queryset(self):
        queryset = super().get_queryset()
        form = ProductSearchForm(self.request.GET)

        if form.is_valid():
            categoria = form.cleaned_data.get('categoria')
            nombre = form.cleaned_data.get('nombre')

            if categoria:
                queryset = queryset.filter(categoria__nombre__icontains=categoria)


            if nombre:
                queryset = queryset.filter(nombre__icontains=nombre)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductSearchForm(self.request.GET)
        return context




class EditProductView(LoginRequiredMixin,UpdateView):
    model = Producto
    template_name = "productos/editproduct.html"
    form_class = ProductoForm
    success_url = '/listproduct'
    login_url = "/"

class Delete_Product(LoginRequiredMixin,DeleteView):
    model = Producto
    template_name ="productos/deleteproduct.html"
    success_url='/listproduct' 
    cancel_url='/listproduct'
    login_url = "/"   


class EntradaProductoView(CreateView):
    model = EntradaProducto
    template_name = "productos/entradaproducto.html"
    form_class = EntradaProductoForm
    success_url='/listproduct' 
    cancel_url='/listproduct'
    login_url = "/"  

class ListEntradaProducto(LoginRequiredMixin,ListView):
    model = EntradaProducto
    template_name = "productos/listentradaproducto.html"
    login_url = "/"

    def get_queryset(self):
        producto_nombre = self.kwargs['producto_nombre']
        return EntradaProducto.objects.filter(producto__nombre=producto_nombre)
    

#### View Area

class CreateArea(LoginRequiredMixin,CreateView):
    model = Area
    template_name = "area/createarea.html"
    form_class = AreaForm
    success_url = '/home'
    login_url = "/"

class ListArea(LoginRequiredMixin,ListView):
    model = Area
    template_name = "area/listarea.html"
    login_url = "/"

class EditAreaView(LoginRequiredMixin,UpdateView):
    model = Area
    template_name = "area/editarea.html"
    form_class = AreaForm
    success_url = '/listarea'
    login_url = "/"

class Delete_Area(LoginRequiredMixin,DeleteView):
    model = Area
    template_name ="area/deletearea.html"
    success_url='/listarea' 
    cancel_url='/listarea'
    login_url = "/"   


#### View Sede

class CreateSede(LoginRequiredMixin,CreateView):
    model = Sede
    template_name = "sede/createsede.html"
    form_class = SedeForm
    success_url = '/home'
    login_url = "/"

class ListSede(LoginRequiredMixin,ListView):
    model = Sede
    template_name = "sede/listsede.html"
    login_url = "/"

class EditSedeView(LoginRequiredMixin,UpdateView):
    model = Sede
    template_name = "sede/editsede.html"
    form_class = SedeForm
    success_url = '/listsede'
    login_url = "/"

class Delete_Sede(LoginRequiredMixin,DeleteView):
    model = Sede
    template_name ="sede/deletesede.html"
    success_url='/listsede' 
    cancel_url='/listsede'
    login_url = "/"   


    
# Vistas de deposito

class CreateDeposito(LoginRequiredMixin,CreateView):
    model = Deposito
    template_name = "deposito/createdeposit.html"
    form_class = DepositoForm
    success_url = '/entradaproducto'
    login_url = "/"

class ListDeposito(LoginRequiredMixin,ListView):
    model = Deposito
    template_name = "deposito/listdeposit.html"
    login_url = "/"

class EditDeposito(LoginRequiredMixin,UpdateView):
    model = Deposito
    template_name = "deposito/editdeposit.html"
    form_class = DepositoForm
    success_url = '/listdeposito'
    login_url = "/"

class Delete_Deposito(LoginRequiredMixin,DeleteView):
    model = Deposito
    template_name ="deposito/deletedeposit.html"
    success_url='/listdeposito' 
    cancel_url='/listdeposito'
    login_url = "/"   
    
# Vistas de Patrimonio

class CreatePatrimonio(LoginRequiredMixin,CreateView):
    model = Patrimonio
    template_name = "patrimonio/createpatrimonio.html"
    form_class = PatrimonioForm
    success_url = '/home'
    login_url = "/"

class ListPatrimonio(LoginRequiredMixin,ListView):
    model = Patrimonio
    template_name = "patrimonio/listpatrimonio.html"
    login_url = "/"

class EditPatrimonio(LoginRequiredMixin,UpdateView):
    model = Patrimonio
    template_name = "patrimonio/editpatrimonio.html"
    form_class = PatrimonioForm
    success_url = '/listpatrimonio'
    login_url = "/"

class Delete_Patrimonio(LoginRequiredMixin,DeleteView):
    model = Patrimonio
    template_name ="patrimonio/deletepatrimonio.html"
    success_url='/listpatrimonio' 
    cancel_url='/listpatrimonio'
    login_url = "/"   
    
    

### RQs ###

class CreateRQ(LoginRequiredMixin,CreateView):
    model = RQ
    template_name = "RQ/createrq.html"
    form_class = RQForm
    success_url = '/home'
    login_url = "/"



class ListRQ(LoginRequiredMixin,ListView):
    model = RQ
    template_name = "RQ/listrq.html"
    login_url = "/"

class EditRQView(LoginRequiredMixin,UpdateView):
    model = RQ
    template_name = "RQ/editrq.html"
    form_class = RQForm
    success_url = '/listrq'
    login_url = "/"

class DeleteRQ(LoginRequiredMixin,DeleteView):
    model = RQ
    template_name ="RQ/deleterq.html"
    success_url='/listrq' 
    cancel_url='/listrq'
    login_url = "/"   



class crearRQ(ListView):
    model = Deposito
    template_name = "RQ/createRQ.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = SeleccionarDepositoForm()
        return context

# Aca agrupa los Productos pero no me da detalles

class FiltrarProductosView(View):
    template_name = 'RQ/filtrar_productos.html'

    def get(self, request):
        form = FiltrarProductosForm()
        productos = []
        return render(request, self.template_name, {'form': form, 'productos': productos})

    def post(self, request):
        form = FiltrarProductosForm(request.POST)
        productos = []

        if form.is_valid():
            deposito_seleccionado = form.cleaned_data['deposito']
            # Obtener todas las entradas relacionadas con el depósito seleccionado
            entradas = EntradaProducto.objects.filter(ubicacion=deposito_seleccionado)

            # Agrupar las entradas por nombre del producto y calcular la cantidad total
            productos = (
                entradas.values('producto__nombre','fecha_ingreso','fecha_vencimiento')
                .annotate(cantidad_total=Sum('cantidad'))
                .order_by('producto__nombre')
            )

        return render(request, self.template_name, {'form': form, 'productos': productos})


# De esta forma muestra cada instancia.
# class FiltrarProductosView(View):
#     template_name = 'RQ/filtrar_productos.html'

#     def get(self, request):
#         form = FiltrarProductosForm()
#         productos = []
#         return render(request, self.template_name, {'form': form, 'productos': productos})

#     def post(self, request):
#         form = FiltrarProductosForm(request.POST)
#         productos = []

#         if form.is_valid():
#             deposito_seleccionado = form.cleaned_data['deposito']
#             # Obtener todas las entradas relacionadas con el depósito seleccionado
#             entradas = EntradaProducto.objects.filter(ubicacion=deposito_seleccionado)

#             # Agrupar las entradas por nombre del producto y calcular la cantidad total
#             productos = (
#                 entradas.values('producto__nombre', 'fecha_ingreso', 'fecha_vencimiento')
#                 .annotate(cantidad_total=Sum('cantidad'))
#                 .order_by('producto__nombre', 'fecha_ingreso')
#             )

#         return render(request, self.template_name, {'form': form, 'productos': productos})


class FiltrarProductosView(View):
    template_name = 'RQ/filtrar_productos.html'

    def get(self, request):
        form = FiltrarProductosForm()
        productos = []
        entradas_individuales = []  # Lista para almacenar las entradas individuales
        return render(request, self.template_name, {'form': form, 'productos': productos, 'entradas_individuales': entradas_individuales})

    def post(self, request):
        form = FiltrarProductosForm(request.POST)
        productos = []
        entradas_individuales = []

        if form.is_valid():
            deposito_seleccionado = form.cleaned_data['deposito']
            # Obtener la cantidad total agrupada por nombre de producto
            productos = (
                EntradaProducto.objects
                .filter(ubicacion=deposito_seleccionado)
                .values('producto__nombre')
                .annotate(cantidad_total=Sum('cantidad'))
                .order_by('producto__nombre')
            )
            # Obtener las entradas individuales relacionadas con el depósito seleccionado
            entradas_individuales = EntradaProducto.objects.filter(ubicacion=deposito_seleccionado)

        agregar_form = AgregarProductoForm()  # Formulario para agregar productos
        productos_seleccionados = []  # Lista para almacenar productos seleccionados

        if request.method == 'POST' and 'agregar' in request.POST:
            agregar_form = AgregarProductoForm(request.POST)
            if agregar_form.is_valid():
                cantidad_seleccionada = agregar_form.cleaned_data['cantidad']
                entrada_id_seleccionada = agregar_form.cleaned_data['entrada_id']
                entrada_seleccionada = EntradaProducto.objects.get(pk=entrada_id_seleccionada)
                if cantidad_seleccionada > 0 and cantidad_seleccionada <= entrada_seleccionada.cantidad:
                    # Agrega el producto seleccionado a la lista
                    productos_seleccionados.append({
                        'entrada_id': entrada_id_seleccionada,
                        'producto_nombre': entrada_seleccionada.producto.nombre,
                        'cantidad_seleccionada': cantidad_seleccionada,
                    })
                else:
                    # Muestra un mensaje de error si la cantidad no es válida
                    messages.error(request, 'La cantidad debe ser mayor que 0 y no debe exceder la cantidad disponible.')

        return render(request, self.template_name, {
            'form': form,
            'productos': productos,
            'entradas_individuales': entradas_individuales,
            'agregar_form': agregar_form,
            'productos_seleccionados': productos_seleccionados,  # Lista de productos seleccionados
        })
        

def confirmar_view(request):
    if request.method == 'POST':
        # Obtén los productos del carrito y las cantidades
        productos = request.POST.getlist('productos[]')  # Asegúrate de que coincida con el nombre de tus campos ocultos
        detalles_productos = []

        # Actualiza la base de datos con las cantidades restantes
        for producto in productos:
            nombre, fecha_vencimiento, cantidad = producto.split(',')
            producto_db = Producto.objects.get(nombre=nombre, fecha_vencimiento=fecha_vencimiento)
            producto_db.cantidad -= int(cantidad)
            producto_db.save()

            # Agrega detalles del producto confirmado a la lista
            detalles_productos.append({
                'nombre': nombre,
                'cantidad': int(cantidad),
                'id': producto_db.id
            })

        # Limpia el carrito después de confirmar
        request.session['carrito'] = {}

        # Redirige a la página de detalles de productos confirmados
        return render(request, 'RQ/detalles_confirmacion.html', {'detalles_productos': detalles_productos})

    return render(request, 'RQ/detalles_confirmacion.html')


class createPersona(CreateView):
    model = Persona
    template_name = 'RQ/createPersona.html'
    form_class = PersonaForm

def get(self, request, *args, **kwargs):
        form = self.form_class()
        html_form = self.render_to_string(self.template_name, {'form': form}, request=request)
        return JsonResponse({'html': html_form})

def cargar_tabla_sede(request):
    sedes = Sede.objects.values('id', 'nombre')
    return JsonResponse({'sedes': list(sedes)})