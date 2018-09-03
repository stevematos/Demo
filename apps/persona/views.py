from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
# Create your views here.
from algoritmos.extras import leer_json
from apps.persona.forms import PersonaForm
from apps.persona.models import Persona, Categoria


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





#VIEW PARA LLENAR DATOS CON EL URL DADO POR PyMPack
def recibir_data(request):
    data=leer_json('http://ec2-34-236-250-113.compute-1.amazonaws.com:9000/categories/')
    for dato in data:
        obj, created = Categoria.objects.get_or_create(
            id=dato['id'],
            defaults={
                        'name':dato['name'],
                        'image':dato['image'],
                        'description':dato['description']
                    }
        )
    return HttpResponse(data)