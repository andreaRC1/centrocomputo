from django.urls import path
from . import views

app_name = 'materiales'

urlpatterns = [
    path('lista/', views.MaterialList.as_view(), name='lista'),
    path('nuevo/', views.MaterialCrear.as_view(), name='nuevo'),
    path('ver/<int:pk>', views.MaterialDetalle.as_view(), name='ver'),
    path('editar/<int:pk>', views.MaterialActualizar.as_view(), name='editar'),
    path('eliminar/<int:pk>', views.MaterialDelete.as_view(), name='eliminar'),
    path('pdf/', views.MaterialesPdf.as_view(), name='pdf'),

    #path('grafica/', views.Grafica.as_view(), name='grafica'),


]
