from django.contrib import admin
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipos/', include('equipos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('materiales/', include('materiales.urls')),
    path('operaciones/', include('operaciones.urls')),
    path('tipomaterial/', include('materiales.urls_tipomaterial')),
    path('', views.LoginUsuario.as_view())
]
