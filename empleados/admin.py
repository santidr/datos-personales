from django.contrib import admin
from .models import Persona
from .forms import PersonaForm

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'fecha_registro', 'actualizado']
    form = PersonaForm

admin.site.register(Persona, PersonaAdmin)
