from django.urls import path
from apps.persona import views

app_name='persona'

urlpatterns = [
    path('',views.PersonaList.as_view(),name="list_persona"),
    path('crear',views.PersonaCreate.as_view(),name="create_persona"),
    path('editar/<pk>',views.PersonaUpdate.as_view(),name="update_persona"),
    path('eliminar/<pk>', views.PersonaDelete.as_view(), name="delete_persona"),
    #path('data',views.recibir_data,name="recibir_data"),
]