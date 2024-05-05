from dataclasses import dataclass
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estudiantes
# Create your views here.
TEMPLATE_DIRS=(
    'os.path.join(BASE_DIR,"templates")'
)

def index(request):
    return render(request,"index.html")

def listar(request):
    users=Estudiantes.objects.all()
    datos={'usuarios':users}
    return render(request,"estudiantes/listar.html", datos)

def agregar(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('f_nac'):
            user=Estudiantes()
            user.nombre=request.POST.get('nombre')
            user.apellido=request.POST.get('apellido')
            user.correo=request.POST.get('correo')
            user.telefono=request.POST.get('telefono')
            user.f_nac=request.POST.get('f_nac')
            user.save()
            return redirect('listar')
    else:
        return render(request,"estudiantes/agregar.html")

def actualizar(request):
    if request.method=='POST':
        if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('f_nac'):
            user=Estudiantes()
            user.id=request.POST.get('id')
            user.nombre=request.POST.get('nombre')
            user.apellido=request.POST.get('apellido')
            user.correo=request.POST.get('correo')
            user.telefono=request.POST.get('telefono')
            user.f_nac=request.POST.get('f_nac')
            user.save()
            return redirect('listar')
    else:
        users=Estudiantes.objects.all()
        datos={'usuarios':users}
        return render(request,"estudiantes/actualizar.html",datos)

def eliminar(request):
    if request.method=='POST':
        id_a_borrar=request.POST.get('id')
        tupla=Estudiantes.objects.get(id=id_a_borrar)
        tupla.delete()
        return redirect('listar')
    else:
        users=Estudiantes.objects.all()
        datos={'usuarios':users}
        return render(request,"estudiantes/eliminar.html", datos)

