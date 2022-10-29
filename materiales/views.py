from django.shortcuts import render, redirect, get_object_or_404
from .models import Material, TipoMaterial
from .forms import MaterialForm, TipoMaterialForm
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django_weasyprint import WeasyTemplateResponseMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('auth.administrador_permiso', raise_exception=True)
def lista_tipomaterial(request):
    tipomateriales = TipoMaterial.objects.all()
    context = {'tipomateriales': tipomateriales, "cat_lista": True}
    return render(request, 'lista_tipomaterial.html', context)


@login_required
@permission_required('auth.administrador_permiso', raise_exception=True)
def nuevo_tipomaterial(request):
    form = TipoMaterialForm()
    if request.method == 'POST':
        form = TipoMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipomaterial:lista')

    context = {'form': form, "tmt_nueva": True}
    return render(request, 'alta_tipomaterial.html', context)


@login_required
@permission_required('auth.administrador_permiso', raise_exception=True)
def eliminar_tipomaterial(request, id):
    tipomaterial = get_object_or_404(TipoMaterial, id=id)
    tipomaterial.delete()

    return redirect('tipomaterial:lista')


@login_required
@permission_required('auth.administrador_permiso', raise_exception=True)
def editar_tipomaterial(request, id):
    tipomaterial = get_object_or_404(TipoMaterial, id=id)
    form = TipoMaterialForm(instance=tipomaterial)
    if request.method == 'POST':
        form = TipoMaterialForm(request.POST, instance=tipomaterial)
        if form.is_valid():
            form.save()
            return redirect('tipomaterial:lista')
    context = {'form': form, "cat_edit": True}
    return render(request, 'editar_tipomaterial.html', context)


class MaterialList(PermissionRequiredMixin, ListView):
    permission_required = 'auth.administrador_permiso'
    paginate_by = 10
    model = Material
    context_object_name = 'materiales'
    extra_context = {'etiqueta': 'Lista', 'mt_lista': True}


class MaterialDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'auth.administrador_permiso'
    model = Material
    extra_context = {'etiqueta': 'Eliminar', 'mt_del': True}
    success_url = reverse_lazy('materiales:lista')


class MaterialCrear(PermissionRequiredMixin, CreateView):
    permission_required = 'auth.administrador_permiso'
    model = Material
    form_class = MaterialForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar', 'mt_nuevo': True}
    success_url = reverse_lazy('materiales:lista')


class MaterialActualizar(PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.administrador_permiso'
    model = Material
    form_class = MaterialForm
    extra_context = {
        'etiqueta': 'Actualizar',
        'boton': 'Guardar',
        'mt_edit': True}
    success_url = reverse_lazy('materiales:lista')


class MaterialDetalle(PermissionRequiredMixin, DetailView):
    permission_required = 'auth.administrador_permiso'
    model = Material
    extra_context = {
        'etiqueta': 'Detalles',
        'boton': 'Regresar',
        'mt_det': True}


class VistaPdf(PermissionRequiredMixin, ListView):
    permission_required = 'auth.administrador_permiso'
    model = Material
    context_object_name = 'materiales'
    template_name = 'materiales/materiales_pdf.html'


class MaterialesPdf(WeasyTemplateResponseMixin, VistaPdf):
    model = Material
    pdf_attachment = False
    pdf_filename = 'Lista_materiales.pdf'
