from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Curso, Docente, Especialidad, Matricula
from django.contrib.auth import login, authenticate, logout as user_logout
from datetime import datetime

# Create your views here.

def login_form(request):
    return render(request, "login.html")

def logueo(request):
    user = authenticate(request,username=(request.POST['username']), password=(request.POST['password']))
    if user:
        login(request,user)
        return HttpResponseRedirect('curso')
    else:
        return HttpResponseRedirect('login')

@login_required(login_url="/login")
def logout(request):
    user_logout(request)
    return render(request, "login.html")

def registro(request):
    return render(request, "registro.html")

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    pwd = request.POST['password']
    user = User.objects.create_user(username, email, pwd)
    user.save()
    if(User.objects.filter(username=username, email = email, password=pwd).exists()):
        return HttpResponseRedirect('curso')
    else:
        return HttpResponseRedirect('login')

#CURSOS  
@login_required(login_url="/login")
def curso(request):
    cursosListado=Curso.objects.select_related('docente','especialidad').order_by("codigo")
    docenteListado = Docente.objects.all().order_by('nombre').values()
    especialidadListado = Especialidad.objects.all().order_by('nombre').values()
    context={
            "cursos":cursosListado,
            "docente":docenteListado,
            "especialidad":especialidadListado
        }
    return render(request, "Cursos\RegistrarCursos.html",context)

@login_required(login_url="/login")
def savecurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = int(request.POST['numCreditos'])
    docente = Docente.objects.get(nombre=request.POST['docente'])
    especialidad = Especialidad.objects.get(nombre=request.POST['especialidad'])
    Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, docente=docente, especialidad=especialidad)
    return redirect('/')

@login_required(login_url="/login")
def deletecurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

@login_required(login_url="/login")
def datacurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    cursosListado=Curso.objects.select_related('docente','especialidad').order_by("codigo")
    docenteListado = Docente.objects.all().order_by('nombre').values()
    especialidadListado = Especialidad.objects.all().order_by('nombre').values()
    context = {
        'codigo':curso.codigo,
        'nombre':curso.nombre,
        'creditos':int(curso.creditos),
        'curso_docente': curso.docente.nombre,
        'curso_especialidad': curso.especialidad.nombre,
        'cursos':cursosListado,
        "docente":docenteListado,
        "especialidad":especialidadListado
    }
    return render(request,'Cursos\ActualizarCursos.html',context)

@login_required(login_url="/login")
def updatecurso(request):
    curso = Curso.objects.get(codigo=request.POST['txtCodigo'])
    curso.nombre = request.POST['txtNombre']
    curso.creditos = int(request.POST['numCreditos'])
    curso.docente = Docente.objects.get(nombre=request.POST['docente'])
    curso.especialidad = Especialidad.objects.get(nombre=request.POST['especialidad'])
    curso.save()
    cursosListado=Curso.objects.select_related('docente','especialidad').order_by("codigo")
    docenteListado = Docente.objects.all().order_by('nombre').values()
    especialidadListado = Especialidad.objects.all().order_by('nombre').values()
    context={
            "cursos":cursosListado,
            "docente":docenteListado,
            "especialidad":especialidadListado
        }
    return render(request, "Cursos\RegistrarCursos.html",context)

@login_required(login_url="/login")
def busquedacurso(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        listadocursos = Curso.objects.select_related('docente','especialidad').filter(nombre__startswith=nom).order_by("codigo")
        context = {
            "cursos":listadocursos
        }
        return render(request,'Cursos\BusquedaCursos.html', context)
    else:
        listadocursos = Curso.objects.select_related('docente','especialidad')

        context = {
            "cursos":listadocursos
        }
        return render(request,'Cursos\BusquedaCursos.html', context)
    
#DOCENTES
@login_required(login_url="/login")
def docente(request):
    docenteListado = Docente.objects.all().order_by('apellido').values()
    context={
            "docentes":docenteListado,
        }
    return render(request, "Docentes\RegistrarDocentes.html",context)

@login_required(login_url="/login")
def savedocente(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    date = request.POST['date']
    dni = request.POST['txtDni']
    telefono = request.POST['txtTelefono']
    Docente.objects.create(nombre=nombre, apellido=apellido, fIngreso=date, dni=dni, telefono=telefono)
    return redirect('/docente')

@login_required(login_url="/login")
def deletedocente(request, id):
    docente = Docente.objects.get(idDocente=id)
    docente.delete()
    return redirect('/docente')

@login_required(login_url="/login")
def datadocente(request, id):
    docente = Docente.objects.get(idDocente=id)
    docenteListado = Docente.objects.all().order_by('apellido').values()
    fecha = str(docente.fIngreso)
    context = {
        'docente':docente,
        "docentes":docenteListado,
        'fecha':fecha,
    }
    return render(request,'Docentes\ActualizarDocentes.html',context)

@login_required(login_url="/login")
def updatedocente(request):
    docente = Docente.objects.get(idDocente=request.POST['ID'])
    docente.nombre = request.POST['txtNombre']
    docente.apellido = request.POST['txtApellido']
    docente.fIngreso = request.POST['date']
    docente.dni = request.POST['txtDni']
    docente.telefono = request.POST['txtTelefono']
    docente.save()
    docenteListado = Docente.objects.all().order_by('apellido').values()
    context={
            "docentes":docenteListado,
        }
    return render(request, "Docentes\RegistrarDocentes.html",context)

@login_required(login_url="/login")
def busquedadocente(request):
    if request.method == 'POST':
        if 'apellido' in request.POST:
            date = False
            ape = request.POST['apellido']
            docenteListado = Docente.objects.filter(apellido__startswith=ape).order_by('apellido').values()
            docente_fechas = Docente.objects.values('fIngreso').distinct()
            context={
                    "docentes":docenteListado,
                    "docente_fechas":docente_fechas
                }
            return render(request, "Docentes\BusquedaDocentes.html",context)
        elif 'date' in request.POST:
            date = datetime.strptime(request.POST['date'],"%b %d, %Y")
            ape = False
            docenteListado = Docente.objects.filter(fIngreso=date).order_by('apellido').values()
            docente_fechas = Docente.objects.values('fIngreso').distinct()
            context={
                    "docentes":docenteListado,
                    "docente_fechas":docente_fechas
                }
            return render(request, "Docentes\BusquedaDocentes.html",context)

    else:
        docenteListado = Docente.objects.all().order_by('apellido').values()
        docente_fechas = Docente.objects.values('fIngreso').distinct()
        context={
                "docentes":docenteListado,
                "docente_fechas":docente_fechas
            }
        return render(request, "Docentes\BusquedaDocentes.html",context)
    
#ESPECIALIDADES

@login_required(login_url="/login")
def especialidad(request):
    especialidadListado = Especialidad.objects.all().order_by('nombre').values()
    context={
            "especialidades":especialidadListado,
        }
    return render(request, "Especialidades\RegistrarEspecialidades.html",context)

@login_required(login_url="/login")
def saveespecialidad(request):
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    Especialidad.objects.create(nombre=nombre, descripcion=descripcion)
    return redirect('/especialidad')

@login_required(login_url="/login")
def deleteespecialidad(request, id):
    especialidad = Especialidad.objects.get(idEspecialidad=id)
    especialidad.delete()
    return redirect('/especialidad')

@login_required(login_url="/login")
def dataespecialidad(request, id):
    especialidad = Especialidad.objects.get(idEspecialidad=id)
    especialidadListado = Especialidad.objects.all().order_by('nombre').values()
    context = {
        'especialidad':especialidad,
        "especialidades":especialidadListado,
    }
    return render(request,'Especialidades\ActualizarEspecialidades.html',context)

@login_required(login_url="/login")
def updateespecialidad(request):
    especialidad = Especialidad.objects.get(idEspecialidad=request.POST['id'])
    especialidad.nombre = request.POST['txtNombre']
    especialidad.descripcion = request.POST['txtDescripcion']
    especialidad.save()
    especialidadListado = Especialidad.objects.all().order_by('nombre').values()
    context={
            "especialidades":especialidadListado,
        }
    return render(request, "Especialidades\RegistrarEspecialidades.html",context)

@login_required(login_url="/login")
def busquedaespecialidad(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        listadoespecialidades = Especialidad.objects.filter(nombre__startswith=nom).order_by('nombre').values()
        context = {
            "especialidades":listadoespecialidades
        }
        return render(request,'Especialidades\BusquedaEspecialidades.html', context)
    else:
        listadoespecialidades = Especialidad.objects.all()
        context = {
            "especialidades":listadoespecialidades
        }
        return render(request,'Especialidades\BusquedaEspecialidades.html', context)
 
#MATRICULA  
@login_required(login_url="/login")
def matricula(request):
    matriculaListado= Matricula.objects.all()
    cursosListado = Curso.objects.all()
    context={
            "matriculas":matriculaListado,
            "cursos":cursosListado
        }
    return render(request, "Matriculas\RegistrarMatriculas.html",context)

@login_required(login_url="/login")
def savematricula(request):
    curso = request.POST['curso']
    fecha = request.POST['date']
    cuotas = int(request.POST['numCuotas'])
    curso = Curso.objects.get(nombre=request.POST['curso'])
    Matricula.objects.create(idCurso=curso, fechaMat=fecha, cuotas=cuotas)
    return redirect('/matricula')

@login_required(login_url="/login")
def deletematricula(request, id):
    matricula = Matricula.objects.get(idMatricula=id)
    matricula.delete()
    return redirect('/matricula')

@login_required(login_url="/login")
def datamatricula(request, id):
    matricula = Matricula.objects.get(idMatricula=id)
    matriculaListado= Matricula.objects.all()
    cursosListado=Curso.objects.all()
    fecha = str(matricula.fechaMat)
    context = {
        'id':matricula.idMatricula,
        'idcurso':matricula.idCurso,
        'cuotas':int(matricula.cuotas),
        'fecha':fecha,
        'cursos':cursosListado,
        "matriculas":matriculaListado,
        "matricula":matricula
    }
    return render(request,'Matriculas\ActualizarMatriculas.html',context)

@login_required(login_url="/login")
def updatematricula(request):
    matricula = Matricula.objects.get(idMatricula=request.POST['id'])
    matricula.idCurso = Curso.objects.get(nombre=request.POST['curso'])
    matricula.fechaMat = request.POST['date']
    matricula.cuotas = int(request.POST['numCuotas'])
    matricula.save()
    cursosListado=Curso.objects.all()
    matriculaListado= Matricula.objects.all()    
    context={
            "matriculas":matriculaListado,
            "cursos":cursosListado,
        }
    return render(request, "Matriculas\RegistrarMatriculas.html",context)

@login_required(login_url="/login")
def busquedamatricula(request):
    if request.method == 'POST':
        if 'date' in request.POST:
            date = datetime.strptime(request.POST['date'],"%b %d, %Y")
            matriculaListado = Matricula.objects.filter(fechaMat=date)
            matricula_fechas = Matricula.objects.values('fechaMat').distinct()
            context={
                    "matriculas":matriculaListado,
                    "matricula_fechas":matricula_fechas
                }
            return render(request, "Matriculas\BusquedaMatriculas.html",context)

    else:
        matriculaListado = Matricula.objects.all()
        matricula_fechas = Matricula.objects.values('fechaMat').distinct()
        context={
                "matriculas":matriculaListado,
                "matricula_fechas":matricula_fechas
            }
        return render(request, "Matriculas\BusquedaMatriculas.html",context)