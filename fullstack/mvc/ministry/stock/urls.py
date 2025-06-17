from django.urls import path
from .views import (Home, Login,Logout, 
                    CreateUser, Delete_User, List_User, EditUserView,
                    CreateProduct,ListProduct,DataUser,EditProductView,Delete_Product,
                    RegistrarEntrada,CrearRegistroIngreso,EntradaProductoView,ListEntradaProducto,EditEPView,Delete_EP,
                    CategoriasView,ListCategorias,Delete_Categoria,EditCategoriaView,
                    CreateDeposito,ListDeposito,Delete_Deposito,EditDeposito,
                    CreateArea,ListArea,Delete_Area,EditAreaView,
                    CreatePatrimonio,ListPatrimonio,Delete_Patrimonio,EditPatrimonio,
                    CreateSede,ListSede,Delete_Sede,EditSedeView, crearRQ, FiltrarProductosView, confirmar_view,
                    CreateRQ,ListRQ,DeleteRQ,EditRQView, createPersona
                    
                   )
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .forms import (PassReset, PassConfirm)

urlpatterns = [
    # /Login and home/ 
    path('',Login.as_view(), name='login'),
    path('home', Home.as_view(),name='home'),
    path('logout/',Logout.as_view(), name='logout'), 
    # / User/
    path('createuser/',CreateUser.as_view(), name='createuser'),
    path('deleteuser/<int:pk>/', Delete_User.as_view(), name='deleteuser'),
    path('listuser/', List_User.as_view(), name='ListUser'), 
    path('edituser/<int:pk>/',EditUserView.as_view(),name = 'edituser'),
    path('data_user/<int:pk>/', DataUser.as_view(), name='datauser'),
    # / Reset password /
    path('pw-reset/', PasswordResetView.as_view(template_name='registration/password_reset_form_custom.html', form_class=PassReset), name = 'password_reset'),
    path('pw-reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm_custom.html', form_class=PassConfirm), name = 'password_reset_confirm'),
    path('pw-reset_done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done_custom.html'), name = 'password_reset_done'),
    path('pw-reset_complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete_custom.html'), name = 'password_reset_complete'),
    # / Productos /
    path('create_product/',CreateProduct.as_view(template_name='productos/create_product.html'), name='createproduct'),
    path('listproduct/', ListProduct.as_view(), name='listproduct'), 
    path('deleteproduct/<int:pk>/', Delete_Product.as_view(), name='deleteproduct'),
    path('editproduct/<int:pk>/',EditProductView.as_view(),name = 'editproduct'),
    path('registrar_entrada/', RegistrarEntrada.as_view() , name='registrar_entrada'),
    path('crear_registro_ingreso/', CrearRegistroIngreso.as_view(), name='crear_registro_ingreso'),
    # / Entrada de Producto /
    path('entradaproducto/', EntradaProductoView.as_view(), name='entradaproducto'),
    path('listentradaproducto/<str:producto_nombre>/', ListEntradaProducto.as_view(), name='listentradaproducto'),
    path('deleteentradaproducto/<int:pk>/', Delete_EP.as_view(), name='deleteentradaproducto'),
    path('editentradaproducto/<int:pk>/',EditEPView.as_view(),name = 'editentradaproducto'),
    # / Area /
    path('createarea/',CreateArea.as_view(), name='createarea'),
    path('listarea/', ListArea.as_view(), name='listarea'), 
    path('deletearea/<int:pk>/', Delete_Area.as_view(), name='deletearea'),
    path('editarea/<int:pk>/',EditAreaView.as_view(),name = 'editarea'),
    
    # / Deposito /
    path('listdeposito',ListDeposito.as_view(),name = 'listdeposito'),
    path('editdeposito/<int:pk>/',EditDeposito.as_view(),name = 'editdeposito'),
    path('deletedeposito/<int:pk>/',Delete_Deposito.as_view(),name = 'deletedeposito'),
    path('createdeposito',CreateDeposito.as_view(),name = 'createdeposito'), 
    # / Patrimonio /
    path('editpatrimonio/<int:pk>/',EditPatrimonio.as_view(),name = 'editpatrimonio'),
    path('deletepatrimonio/<int:pk>/',Delete_Patrimonio.as_view(),name = 'deletepatrimonio'),
    path('createpatrimonio',CreatePatrimonio.as_view(),name = 'createpatrimonio'),
    path('listpatrimonio',ListPatrimonio.as_view(),name = 'listpatrimonio'), 
    # / Categorias /
    path('createcategorias/', CategoriasView.as_view(), name='createcategorias'),
    path('editcategoria/<int:pk>/',EditCategoriaView.as_view(),name = 'editcategoria'),
    path('deletecategoria/<int:pk>/', Delete_Categoria.as_view(), name='deletecategoria'),
    path('listcategoria',ListCategorias.as_view(),name = 'listcategoria'), 

    # / Sede /
    path('createsede/',CreateSede.as_view(), name='createsede'),
    path('listsede/', ListSede.as_view(), name='listsede'), 
    path('deletesede/<int:pk>/', Delete_Sede.as_view(), name='deletesede'),
    path('editsede/<int:pk>/',EditSedeView.as_view(),name = 'editsede'),
    
    
    # / RQs /
    path('crearRQ/', crearRQ.as_view(),name = 'crearRQ'),
    path('filtrar_productos/', FiltrarProductosView.as_view(), name='filtrar_productos'),
    path('confirm_view/', confirmar_view, name='confirm_view'),
    
    path('createrq/',CreateRQ.as_view(), name='createrq'),
    path('listrq/',ListRQ.as_view(), name='listrq'),
    path('deleterq/<int:pk>/', DeleteRQ.as_view(), name='deleterq'),
    path('editrq/<int:pk>/',EditRQView.as_view(),name = 'editrq'),
    path('create_persona/', createPersona.as_view(), name='create_persona'),

]