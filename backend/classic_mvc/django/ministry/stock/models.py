from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group

class UserManager(BaseUserManager):
    def Create_user(self,username,password=None):
        if not username:
            raise ValueError('Usuario invalido')
        usuario  = self.model(username=username)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    

    def create_superuser(self,username,password):
        usuario = self.Create_user(username=username, password=password)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.is_active = True
        usuario.save(using=self._db)

        return usuario
    
#crea los campos en la base de datos
class Usuarios(AbstractBaseUser, PermissionsMixin):
  username=models.CharField(max_length=25, null=True, unique=True)
  first_name=models.CharField(max_length=25, null=True)
  last_name=models.CharField(max_length=25, null=True)
  dni=models.IntegerField(null=True)
  email=models.EmailField(null=True)
  is_active=models.BooleanField(default=True)
  is_staff=models.BooleanField(default=False)
  is_superuser=models.BooleanField(default=False)
  date_joined=models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(default=timezone.now)
  groups=models.ManyToManyField(Group , related_name='usuarios')
  sector = models.CharField(max_length=25, blank=True, null=True)

  objects = UserManager()

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.username



class User_compras(models.Model):
    username_compras=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
        

    def __str__(self):
        return self.username_compras

class User_deposito(models.Model):
    username_deposito=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    def __str__(self):
        return self.username_deposito
    


class Deposito(models.Model):
   nombre=models.CharField(max_length=25,blank=True, unique=True)
   direccion=models.CharField(max_length=25,blank=True, unique=True)
   observacion=models.TextField(blank=True)
   registrado_por = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
   def __str__(self):
    return self.nombre

class Area(models.Model):
   nombre=models.CharField(max_length=25,null=False, unique=True)
   responsable=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
   def __str__(self):
    return self.nombre

class Sede(models.Model):
   nombre = models.CharField(max_length=25, null=False,unique=True)
   direccion = models.CharField(max_length=25, blank=True,unique=True)
   observacion = models.TextField(max_length=30,blank=True)
   nombre_area = models.ForeignKey(Area, on_delete=models.CASCADE)
   
   def __str__(self):
    return self.nombre




class Categorias(models.Model):
   nombre=models.CharField(max_length=25, null=False,unique=True)
   descripcion=models.CharField(max_length=25, blank=True)
  
   def __str__(self):
    return self.nombre

 

class Producto(models.Model):
    nombre=models.CharField(max_length=25, null=False,unique=True)
    categoria=models.ForeignKey(Categorias,
    on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=25, blank=True, unique=True)
    cantidad_minima=models.IntegerField()
    observacion=models.TextField(blank=True)
   
    def __str__(self):
        return self.nombre
    
    def calcular_cantidad_total(self):
    # Calcular la cantidad total sumando las cantidades de las entradas relacionadas
        return sum(entrada.cantidad for entrada in self.entradaproducto_set.all())

    calcular_cantidad_total.short_description = 'Cantidad Total'
   
class EntradaProducto(models.Model):
    numero_remito=models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ubicacion=models.ForeignKey(Deposito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    Unidades_de_Medida = [
        ('kg', 'Kilogramo'),
        ('g', 'Gramo'),
        ('l', 'Litro'),
        ('ml', 'Mililitro'),
        ('U', 'Unidad')
         ]
    unidadmedida = models.CharField(max_length=10, choices=Unidades_de_Medida, default='Unidad', null = True)
       
    fecha_ingreso = models.DateField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    observacion=models.TextField(blank=True)
    
    def __str__(self):
        return f"Entrada para {self.producto.nombre} - Cantidad: {self.cantidad}."

class RegistroIngresoProducto(models.Model):
    username = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    entradas_productos = models.ManyToManyField(EntradaProducto)

    def __str__(self):
        return f"Registro por {self.username} el {self.fecha_registro}"



# class Estado_RQ(models.Model):
#      estados = [
#          ('Pendiente','Pendiente'),
#          ('En Proceso', 'En Proceso'),
#          ( 'Finalizado','Finalizado'),
       
#      ]
#      estado_rq = models.CharField(max_length=10, choices=estados, default='')
     
#      def __str__(self):
#             return self.estado_rq
   
      
####################################################################################################################
class Persona(models.Model):
   nombre = models.CharField(max_length=25, blank=True)
   apellido = models.CharField(max_length=25, blank=True)
   direccion = models.CharField(max_length=25, blank=True)
   localidad = models.CharField(max_length=25, blank=True)
   telefono = models.IntegerField()
#    observacion = models.CharField(max_length=100, blank=True)

class RQ(models.Model):
    fecha = models.DateField()
    destinatarioSyN = [
       ('----', '----'),
       ('Sede','Sede'),
       ('Persona','Persona')
        ]
    destinatario = models.CharField(max_length=25, choices=destinatarioSyN, default='----')
    # sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    # persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    

    estados = [
         ('Pendiente','Pendiente'),
         ('En Proceso', 'En Proceso'),
         ('Finalizado','Finalizado'),
            ]
    estado_rq = models.CharField(max_length=10, choices=estados, default='Pendiente')
    
    nota_gedeba = models.CharField(max_length=10)
    remito = models.CharField(max_length=10)
   
    
    
   


   
#    def save(self, *args, **kwargs):
#         if not self.pk:  
#             super().save(*args, **kwargs)  
#             producto = self.nombre_producto
#             cantidad = producto.cantidad
#             producto_nombre = self.nombre_producto.nombre
#             fecha_str = self.fecha.strftime('%Y-%m-%d')
#             self.nombre = f"RQ-{producto_nombre}-{fecha_str}"

#             try:
#                 producto.restar_stock(cantidad) 
#             except ValueError:
#                 # 
#                 raise ValueError('No hay suficiente stock disponible.')

#             super().save(*args, **kwargs)  
#         else:
#             super().save(*args, **kwargs)
    
#    def __str__(self):
#         return self.nombre


#####################################################################################################
   

# class Estado_P(models.Model):
#    estados = [
        
#         ('D','Disponible'),
#         ('P','En prestamo'),
#         ('B','Baja'),
       
#     ]
#    estado_p = models.CharField(max_length=10, choices=estados, default='Disponible')
#    def __str__(self):
#     return self.estados
   


class Patrimonio(models.Model):
   nombre = models.CharField(max_length=25, blank=True)
   descripcion = models.TextField(max_length=25, blank=True)
   cantidad = models.IntegerField()
   ubicacion = models.ForeignKey(Deposito, on_delete=models.CASCADE)
   f_ingreso = models.DateTimeField()
   estados = [
        ('Disponible','Disponible'),
        ( 'Baja','Baja')
        
           ]
   estado_p= models.CharField(max_length=10, choices=estados, default="Disponible")
   Acta_Admin_Baja_N = models.CharField(max_length=10, blank=True)
   observaciones =models.TextField(blank=True,max_length=150)
   
   def __str__(self):
      return self.nombre
   

   

      