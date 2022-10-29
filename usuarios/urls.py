from django.urls import path
from . import views


app_name = 'usuarios'



urlpatterns = [
    path('lista/', views.UsuarioList.as_view(), name='lista'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo'),
    path('eliminar/<int:pk>', views.UsuarioDelete.as_view(), name='eliminar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('signup/', views.SignupUsuario.as_view(), name='signup'),
    path('cambia_grupo/<int:id_gpo>/<int:id_usuario>', views.cambia_grupo, name='cambia_grupo'),
    path('logout/', views.logout_view, name='logout'),

]
