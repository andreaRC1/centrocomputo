from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Usuario
from .forms import UsuarioForm, UsuarioFormLog
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required


def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

class LoginUsuario(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

class SignupUsuario(CreateView):
    template_name = 'signup.html'
    model = Usuario
    form_class = UsuarioFormLog
    #extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'nuevo_user':True}
    success_url = reverse_lazy('usuarios:login')

@login_required

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(instance=usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:lista')
    context = {'form': form }
    return render(request, 'editar_usuario.html', context) 

@login_required
@permission_required('auth.administrador_permiso', raise_exception=True)
def obtiene_usuario_grupo(request, id):
    if request.method != 'GET':
        return JsonResponse({'error':_('peticion incorrecta')},safe=False, status=403)
    id_usuario = request.GET.get('id')
    grupos = Groups.objects.filter(user_id=id_usuario)
    json=[]
    if not grupos:
        json.append({'error': _('sin grupos asignados')})
    for group in grupos:
        json.append({'id usuario':id_usuario,
        'id_grupo':grupo})
    return JsonResponse(json, safe=False)

def cambia_grupo(request, id_gpo, id_usuario):
    grupo = Group.objects.get(id=id_gpo)
    usuario= Usuario.objects.get(id=id_usuario)

    if grupo in usuario.groups.all():
        if usuario.groups.count() <= 1:
            messages.error(request, 'El usuario debe pertenecer a un grupo minimo')
        else:
            usuario.groups.remove(grupo)
            messages.success(request, 'El usuario ya no pertenece al grupo')
    else:
        usuario.groups.add(grupo)
        messages.success(request, 'El usuario se agrego al grupo')

    return redirect('usuarios:lista')


# Create your views here.
class NuevoUsuario(PermissionRequiredMixin, CreateView):
    permission_required = 'auth.administrador_permiso'
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar'}
    success_url = reverse_lazy('usuarios:lista')

    def form_valid(self, form):
        user = form.save(commit=False)
        return super().form_valid(form)

class UsuarioList(PermissionRequiredMixin, ListView):
    permission_required = ('usuarios.cajero_permiso')
    paginate_by = 10
    model = Usuario
    context_object_name = 'usuarios'
    lista_grupos = Group.objects.all()
    extra_context={'us_lista':True,
                    'lista_grupos': lista_grupos}
    
class UsuarioActualizar(PermissionRequiredMixin, UpdateView):
    
    model = Usuario
    fields = '__all__'
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    success_url = reverse_lazy('usuarios:lista')


class UsuarioDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'auth.administrador_permiso'   
    model = Usuario
    success_url = reverse_lazy('usuarios:lista')
    extra_context = {'etiqueta':'Eliminar', 'user_del':True}

class UsuarioDetalle(PermissionRequiredMixin, DetailView):
    permission_required = 'usuarios.cajero_permiso'
    model = Usuario
    extra_context = {'etiqueta':'Detalles', 'boton':'Regresar'}
