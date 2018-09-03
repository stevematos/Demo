from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,ListView
from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from apps.persona.forms import PersonaForm
from apps.persona.models import Persona


class PersonaList(ListView):
    model = Persona
    template_name = "persona/persona_list.html"

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "persona/persona_form.html"
    success_url= reverse_lazy('persona:list_persona')

