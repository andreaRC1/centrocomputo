from django.contrib import admin
from .models import Operacion, TipoOperacion

admin.site.register(Operacion)
admin.site.register(TipoOperacion)