from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^lista_personas$', login_required(views.PersonaList.as_view()), name="lista_persona"),
    url(r'^nuevo$', login_required(views.PersonaCreate.as_view()), name="nuevo_persona"),
    url(r'^editar/(?P<pk>[0-9]+)$', login_required(views.PersonaUpdate.as_view()), name="editar_persona"),
    url(r'^eliminar/(?P<pk>[0-9]+)$', login_required(views.PersonaDelete.as_view()), name="eliminar_persona"),
]
