"""
URL configuration for berryChill project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from website.viewsPedidos import CarritoView, AgregarProductoCarritoView, EliminarProductoCarritoView, FinalizarPedidoView, FacturaDetailView
from website.views import LoginAPIView, RegisterView, DireccionView

schema_view = get_schema_view(
   openapi.Info(
      title="BerryChill API",
      default_version='v1',
      description="Documentación interactiva con Swagger",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tu-email@dominio.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('website.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('carrito/', CarritoView.as_view(), name='carrito'),
    path('carrito/agregar/', AgregarProductoCarritoView.as_view(), name='agregar-producto'),
    path('carrito/eliminar/<int:producto_id>/', EliminarProductoCarritoView.as_view(), name='eliminar-producto'),
    path('carrito/buy/<int:pedido_id>/', FinalizarPedidoView.as_view(), name='finalizar-carrito'),
    path('factura/<int:pedido_id>/', FacturaDetailView.as_view(), name='detalleFactura'),
    
    # Swagger y Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
