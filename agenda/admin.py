from django.contrib import admin

# Register your models here.

from .models import ItemAgenda

admin.site.register(ItemAgenda)

#default:"Administração do django"="Titulo maior"
admin.site.site_header='Painel de Controle'

#default:"Administração do site"="Titulo menor"
admin.site.index_title='Recursos'

#default:"Site de Administração do django"="Titulo da aba"
admin.site.site_title='Admin Django'