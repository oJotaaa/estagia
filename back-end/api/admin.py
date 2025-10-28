from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Habilidade, Vaga, Alerta, Curso

admin.site.register(Usuario, UserAdmin)

# Register your models here.
admin.site.register(Curso)
admin.site.register(Vaga)
admin.site.register(Alerta)
admin.site.register(Habilidade)