from django.contrib import admin
from .models import (
    Producto,
    Compra,
    Sala,
    Usuario,
    Fondo,
)
# Register your models here.

admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Sala)
admin.site.register(Usuario)
admin.site.register(Fondo)
