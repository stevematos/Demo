from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
# Create your views here.
from apps.persona.forms import PersonaForm
from apps.persona.models import Persona


class PersonaList(ListView):
    model = Persona
    template_name = "persona/persona_list.html"
    paginate_by = 5

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "persona/persona_form.html"
    success_url= reverse_lazy('persona:list_persona')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/persona_form.html'
    success_url = reverse_lazy('persona:list_persona')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'persona/persona_delete.html'
    success_url = reverse_lazy('persona:list_persona')
