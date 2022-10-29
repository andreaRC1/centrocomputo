from django.urls import path
from . import views

app_name = 'operaciones'

urlpatterns = [
    path('lista/', views.OperacionList.as_view(), name='lista'),
    path('nuevo/', views.nueva_operacion, name='nuevo'),
    path(
        'eliminar/<int:pk>',
        views.OperacionDelete.as_view(),
        name='eliminar'),
    path('ver/<int:pk>', views.OperacionDetalle.as_view(), name='ver'),
    #path('validar-matricula/', views.validar_matricula, name='validar_matricula'),
]
