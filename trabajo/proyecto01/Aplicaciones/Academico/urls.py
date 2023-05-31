from django.urls import path
from .import views

app_name = 'Academico'

urlpatterns = [
    path('',views.curso),

    path('login',views.login_form),
    path('logueo',views.logueo),
    path('logout',views.logout),
    path('registro',views.registro),
    path('register',views.register),

    path('home',views.curso),
    path('curso',views.curso),
    path('registrarcurso',views.savecurso),
    path('eliminarcurso/<codigo>',views.deletecurso),
    path('datacurso/<codigo>',views.datacurso),
    path('edicioncurso',views.updatecurso),
    path('busquedacurso',views.busquedacurso),

    path('docente',views.docente),
    path('registrardocente',views.savedocente),
    path('eliminardocente/<id>',views.deletedocente),
    path('datadocente/<id>',views.datadocente),
    path('ediciondocente',views.updatedocente),
    path('busquedadocente',views.busquedadocente),

    path('especialidad',views.especialidad),
    path('registrarespecialidad',views.saveespecialidad),
    path('eliminarespecialidad/<id>',views.deleteespecialidad),
    path('dataespecialidad/<id>',views.dataespecialidad),
    path('edicionespecialidad',views.updateespecialidad),
    path('busquedaespecialidad',views.busquedaespecialidad),

    path('matricula',views.matricula),
    path('registrarmatricula',views.savematricula),
    path('datamatricula/<id>',views.datamatricula),
    path('eliminarmatricula/<id>',views.deletematricula),
    path('edicionmatricula',views.updatematricula),
    path('busquedamatricula',views.busquedamatricula),
]