from django.urls import path
from . import views

app_name = 'tipomaterial'

urlpatterns = [
    path('lista/', views.lista_tipomaterial, name='lista'),
    path('eliminar/<int:id>', views.eliminar_tipomaterial, name='eliminar'),
    path('alta/', views.nuevo_tipomaterial, name='alta'),
    path('editar/<int:id>', views.editar_tipomaterial, name='editar'),
]
