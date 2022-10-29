from .models import Equipo
from .forms import EquipoForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin


class EquipoList(PermissionRequiredMixin, ListView):
    permission_required = 'usuarios.cajero_permiso'
    paginate_by = 10
    model = Equipo
    context_object_name = 'equipos'
    extra_context = {'etiqueta': 'Lista', 'lista_equipos': True}


class EquipoCrear(PermissionRequiredMixin, CreateView):
    permission_required = 'auth.administrador_permiso'
    model = Equipo
    form_class = EquipoForm
    extra_context = {
        'etiqueta': 'Nuevo',
        'boton': 'Agregar',
        'nuevo_equipo': True}
    success_url = reverse_lazy('equipos:lista')


class EquipoEditar(PermissionRequiredMixin, UpdateView):
    permission_required = 'usuarios.cajero_permiso'
    model = Equipo
    form_class = EquipoForm
    extra_context = {
        'etiqueta': 'Editar',
        'boton': 'Guardar',
        'edit_equipo': True}
    success_message = "El equipo se actualizó con exito"
    success_url = reverse_lazy('equipos:lista')


class EquipoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'auth.administrador_permiso'
    model = Equipo
    extra_context = {'etiqueta': 'Eliminar', 'del_equipo': True}
    success_url = reverse_lazy('equipos:lista')


class EquipoDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'usuarios.cajero_permiso'
    model = Equipo
    extra_context = {
        'etiqueta': 'Detalles',
        'boton': 'Regresar',
        'det_equipo': True}
