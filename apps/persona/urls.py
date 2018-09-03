from django.urls import path
from apps.persona import views

app_name='persona'

urlpatterns = [
    path('listar',views.PersonaList.as_view(),name="list_persona"),
    path('crear',views.PersonaCreate.as_view(),name="create_persona"),
]