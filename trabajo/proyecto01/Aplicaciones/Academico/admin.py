from django.contrib import admin
from .models import Curso, Docente, Especialidad, Matricula

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display=['codigo', 'nombre', 'creditos', 'docente', 'especialidad']

class DocenteAdmin(admin.ModelAdmin):
    list_display=['idDocente', 'apellido', 'nombre', 'fIngreso', 'dni', 'telefono']

class EspecialidadAdmin(admin.ModelAdmin):
    list_display=['idEspecialidad', 'nombre', 'descripcion']

class MatriculaAdmin(admin.ModelAdmin):
    list_display=["idMatricula","idCurso","fechaMat","cuotas"]

admin.site.register(Curso, CursoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Matricula, MatriculaAdmin)