from django.contrib import admin
from .models import UserProfile, UsuarioAcademic
# Register your models here.

class PerfilesAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['user']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['user__email','curp']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    list_filter = ['tipo_usuario','genero']
class PerfilesAcademicAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['correo_electronico','matricula','curp', 'nombre','apellido_paterno','apellido_materno']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['nombre','curp', 'correo_electronico', 'matricula']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    list_filter = ['oferta_educativa']
admin.site.register(UserProfile,PerfilesAdmin)
admin.site.register(UsuarioAcademic,PerfilesAcademicAdmin)