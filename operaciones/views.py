from contextlib import ContextDecorator
from materiales.models import TipoMaterial
from .models import Operacion
from usuarios.models import Usuario
from .forms import OperacionForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.template import RequestContext
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

class OperacionList(PermissionRequiredMixin, ListView):
    permission_required = 'usuarios.cajero_permiso'
    paginate_by = 10
    model = Operacion
    context_object_name = 'operaciones'
    extra_context = {'etiqueta': 'Lista', 'oper_list': True}

class NuevaOperacion(PermissionRequiredMixin, CreateView):
    permission_required = 'auth.administrador_permiso'
    model = Operacion
    form_class = OperacionForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar'}
    success_url = reverse_lazy('operaciones:lista')


    def form_valid(self, form):
        user = form.save(commit=False)
        return super().form_valid(form)



def nueva_operacion(request):
    form = OperacionForm()
    if request.method == 'POST':
        try:
            form = OperacionForm(request.POST, request.FILES)
            matricula = request.POST['matricula']
            if matricula != "":
                matricula = matricula
            else:
                matricula = "00000000"
            #nombre = request.POST['nombre']
            #precio_unitario = request.POST['precio_unitario']
            #cantidad = request.POST['cantidad']
            #tipo= request.POST['tipo']
            if form.is_valid():
                tipo = form.cleaned_data["tipo"]
                precio = getattr(tipo,'precio_unitario')
                cantidad= form.cleaned_data.get("cantidad")
                precio_total = precio*cantidad

                #usuario = Usuario.objects.get(matricula = matricula)
                usuario = Usuario.objects.get(id = request.user.id)
                material = TipoMaterial.objects.get(id = request.POST['material'])
                oper = Operacion.objects.create(tipo=tipo,
                                            cantidad = cantidad,
                                            usuario = usuario,
                                            material = material,
                                            precio_total=precio_total)
                result = oper.save()
                if matricula != "00000000":
                    total = int(cantidad) * int(precio)
                    if total > usuario.saldo:
                        context = {'form':form, 'status': "error", 'mensaje':"No hay saldo suficiente."}
                        return render(request, 'operaciones/operacion_form.html', context) 
                    usuario.saldo -= total
                    usuario.save()
                context = {'form':form, 'status': "ok", 'mensaje':"Operación realizada."}
                return render(request, 'operaciones/operacion_form.html', context)
        except:
            print(form)
            context = {'form':form, 'status': "error", 'mensaje':"Datos incorrectos."}
            return render(request, 'operaciones/operacion_form.html', context)
    context = {'form':form, 'status': "nuevo"}
    return render(request, 'operaciones/operacion_form.html', context)


class OperacionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'usuarios.cajero_permiso'
    model = Operacion
    extra_context = {'etiqueta': 'Eliminar', 'op_del': True}
    success_url = reverse_lazy('operaciones:lista')


class OperacionDetalle(PermissionRequiredMixin, DetailView):
    permission_required = 'usuarios.cajero_permiso'
    model = Operacion
    extra_context = {
        'etiqueta': 'Detalles',
        'boton': 'Regresar',
        'mt_det': True
    }