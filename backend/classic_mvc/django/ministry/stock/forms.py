from django import forms
from .models import Usuarios, Group, Producto,EntradaProducto,RegistroIngresoProducto,Categorias,Deposito,Area,Patrimonio,Sede,RQ, Persona
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, PasswordResetForm,SetPasswordForm
from django.contrib.auth import  get_user_model, password_validation, get_backends
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render

Usuarios = get_user_model()




class CreateUserForm(UserCreationForm):

    groups = forms.ModelChoiceField(queryset=Group.objects.all(), label='Seleccionar permisos')
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class': 'class="form-group registration-input'}))
    first_name = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class': 'class="form-group registration-input'}))
    last_name = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'class': 'class="form-group registration-input'}))
    email = forms.CharField(label='Email',widget=forms.TextInput(attrs={'class': 'class="form-group registration-input'}))
    dni = forms.CharField(label='dni',widget=forms.TextInput(attrs={'class': 'class="form-group registration-input'}))
    sector = forms.CharField(label='Sector',widget=forms.TextInput(attrs={'class': 'class="form-group registration-input'}))
    password1 = forms.CharField(max_length=10, widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(max_length=10, widget=forms.PasswordInput, label='Repetir Contraseña')
    is_active = forms.BooleanField(initial=True, required=False, widget=forms.CheckboxInput)
    is_staff = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput)
    is_superuser = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput)



    class Meta:
        model = Usuarios
        fields = ('first_name','last_name','email','dni','sector', 'username', 'password1', 'password2', 'groups', 'is_active', 'is_staff', 'is_superuser')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        if self.cleaned_data['groups']:
            group = self.cleaned_data['groups']
            user.groups.add(group)
        return user


class ChangeUserform(UserChangeForm):
    # password1 = forms.CharField(max_length=10, widget=forms.PasswordInput, label='Contraseña')
    # password2 = forms.CharField(max_length=10, widget=forms.PasswordInput, label='Repetir Contraseña')
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),label='permisos')
    class Meta:
        model= Usuarios
        fields=('first_name','last_name','email','dni','sector', 'username', 'groups', 'is_active', 'is_staff', 'is_superuser')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombre de Usuario')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label='Contraseña')


class PassReset(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),)


class PassConfirm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Nueva Contraseña")
    new_password2 = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Repetir Contraseña" )

    # error_messages = {
    #     "password_mismatch": _("The two password fields didn’t match."),
    # }
    # new_password1 = forms.CharField(
    #     label=_("New password"),
    #     widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    #     strip=False,
    #     help_text=password_validation.password_validators_help_text_html(),
    # )
    # new_password2 = forms.CharField(label=_("New password confirmation"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),)

    # def __init__(self, user, *args, **kwargs):
    #     self.user = user
    #     super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


################## Categoias #################

class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre', 'descripcion']



################## Productos #################


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'cantidad_minima']

class EntradaProductoForm(forms.ModelForm):
    class Meta:
        model = EntradaProducto
        fields = ['numero_remito','producto','ubicacion', 'cantidad','unidadmedida',
                   'fecha_ingreso', 'fecha_vencimiento','observacion']


class RegistroIngresoProductoForm(forms.ModelForm):
    class Meta:
        model = RegistroIngresoProducto
        fields = ['entradas_productos']


class ProductSearchForm(forms.Form):
    categoria = forms.CharField(max_length=100, required=False)
    nombre = forms.CharField(max_length=100, required=False)




################## RQ #################


# class RQForm(forms.ModelForm):

#     class Meta:
#         model = RQ
#         fields = ['fecha','nombre_sede','nombre_producto','fecha_entrega','estado_rq','categorias','nota_gedeba','remito_interno','grups','usuario'

#         ]

################## Area #################

class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = ['nombre','responsable']


################## Deposito #################

class DepositoForm(forms.ModelForm):
    class Meta:
        model = Deposito
        fields = ['nombre', 'direccion', 'observacion', 'registrado_por' ]


class SeleccionarDepositoForm(forms.Form):
    deposito = forms.ModelChoiceField(
        queryset=Deposito.objects.all(),
        empty_label="Seleccionar un depósito",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

################## Patrimonio #################


class PatrimonioForm(forms.ModelForm):
    class Meta:
        model = Patrimonio
        fields = ['nombre', 'descripcion', 'cantidad', 'ubicacion', 'f_ingreso',  'estado_p' ]



################## Sede #################

class SedeForm(forms.ModelForm):
    class Meta:
        model: Sede
        fields = [ 'nombre', 'direccion', 'observacion', 'nombre_area'



        ]

class FiltrarProductosForm(forms.Form):
    deposito = forms.ModelChoiceField(
        queryset=Deposito.objects.all(),
        empty_label="Seleccionar un depósito",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )


class AgregarProductoForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1)
    entrada_id = forms.IntegerField(widget=forms.HiddenInput())



################## RQ #################

class RQForm (forms.ModelForm):
     class Meta:
        model = RQ
        fields = ["fecha", 'destinatario','estado_rq','nota_gedeba','remito']

# class RQForm(forms.ModelForm):
#     class Meta:d
#         model = RQ
#         fields = ['remito','destinatario', 'nota_gedeba', 'sede', 'persona']
#         widgets = {
#             'fecha': forms.DateInput(attrs={'value': 'now'}),
#             'estado_rq': forms.HiddenInput(attrs={'value': 'En Proceso'}),
#             'operador': forms.HiddenInput(),
#             'nombre_operador': forms.HiddenInput(),
#             'carrito': forms.HiddenInput()
#         }

#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super(RQForm, self).__init__(*args, **kwargs)

#         # Asegúrate de ajustar estos campos según tu modelo de Usuario
#         # self.fields['operador'].initial = user
#         # self.fields['nombre_operador'].initial = f"{user.first_name} {user.last_name}"

#         self.fields['sede'].queryset = Sede.objects.all()
#         self.fields['persona'].widget = forms.HiddenInput()

# # views.py
# 

#def create_rq(request):
#    user = request.user
#    form = RQForm(user=user)

#    return render(request, 'RQ/createRQ.html', {'form': form})

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'direccion', 'localidad', 'telefono']

def vista_principal(request):
    sedes = Sede.objects.values('id', 'nombre')
    return render(request, 'ruta/a/tu/formulario.html', {'sedes': list(sedes)})