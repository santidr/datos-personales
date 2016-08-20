from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Persona
from .forms import PersonaForm

# Create your views here.
class PersonaList(ListView):
    model = Persona
    template_name = 'empleados/lista_persona.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'empleados/nuevo_persona.html'
    success_url = reverse_lazy('lista_persona')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'empleados/nuevo_persona.html'
    success_url = reverse_lazy('lista_persona')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'empleados/eliminar_persona.html'
    success_url = reverse_lazy('lista_persona')

# def persona_crear(request):
#     form = PersonaForm(request.POST)
#     context = {'form': form }
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('nuevo_persona')
#
#     return render(request, 'empleados/nuevo_persona.html', context)
