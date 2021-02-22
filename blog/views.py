from django.http import response
from django.shortcuts import redirect, render
from .models import *
from .forms import PlacasForms
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse




def inicio (request):
    return render (request, 'blog/index.html',{})

def base (request):
    return render(request, 'base.html')  

class CreatePlaca (CreateView):
    model= Placas
    form_class = PlacasForms
    template_name = 'blog/crear_autor.html'
    success_url = reverse_lazy ('Listado')


    
def ListPlaca (request):
    busqueda = request.POST.get("buscar")
    placa=Placas.objects.all()
    
    if busqueda:
        placa = Placas.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(chasis__icontains = busqueda) |
            Q(noPlaca__icontains = busqueda) |
            Q(compania__icontains = busqueda) |
            Q(Estado__icontains = busqueda) 

        ).distinct()

    return render (request,  "blog/Listado.html", {"placas": placa})


def documentos (request):
    busqueda = request.POST.get("buscar")
    placas=Placas.objects.all()
    
    if busqueda:
        placas = Placas.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(chasis__icontains = busqueda) |
            Q(noPlaca__icontains = busqueda) |
            Q(compania__icontains = busqueda) |
            Q(Estado__icontains = busqueda) 

        ).distinct()

    return render (request,  "blog/documentos.html", {"placas": placas})

class UpdatePlaca (UpdateView):
    model= Placas
    form_class = PlacasForms
    template_name = 'blog/editar.html'
    success_url = reverse_lazy ('Listado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Autor'] = Placas.objects.filter(id = True)
        return context

def DeletePlacas(request,id):
    placa = Placas.objects.get(pk = id)
    placa.delete()
    placa=Placas.objects.all()
    return render(request,'blog/Listado.html',{ "placas": placa, "mensaje":'ok'})
    


