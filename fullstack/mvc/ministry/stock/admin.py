from django.contrib import admin
from.models import Producto,Categorias,Area,Deposito,Sede,Patrimonio,EntradaProducto,RegistroIngresoProducto#Estado_P,Estado_RQ,RQ,
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth import get_user_model






Usuario = get_user_model()

class Usuarioadmin(UserAdmin):
    list_display = ['username']
    readonly_fields = ('date_joined',) 


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'descripcion','cantidad_minima','observacion', 'calcular_cantidad_total')

    def calcular_cantidad_total(self, obj):
        return obj.calcular_cantidad_total()

    calcular_cantidad_total.short_description = 'Cantidad Total'
    
class RQAdmin(admin.ModelAdmin):
    exclude = ('nombre',)








admin.site.register(Usuario)
admin.site.register(Producto,ProductoAdmin)
#admin.site.register(Nota_GedebaAdmin)
admin.site.register(Categorias)
admin.site.register(Area)
admin.site.register(Deposito)
admin.site.register(Sede)
#admin.site.register(Estado_RQ)
#admin.site.register(RQ,RQAdmin)
#admin.site.register(Estado_P)
admin.site.register(Patrimonio)
admin.site.register(EntradaProducto)
admin.site.register(RegistroIngresoProducto)



