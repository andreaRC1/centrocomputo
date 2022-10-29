from django.urls import path
from . import views

app_name = 'equipos'

urlpatterns = [
    path('lista/', views.EquipoList.as_view(), name='lista'),
    path('nuevo/', views.EquipoCrear.as_view(), name='nuevo'),
    path('editar/<int:pk>', views.EquipoEditar.as_view(), name='editar'),
    path('eliminar/<int:pk>', views.EquipoDelete.as_view(), name='eliminar'),
    path('detalles/<int:pk>', views.EquipoDetail.as_view(), name='detalles'),
]
