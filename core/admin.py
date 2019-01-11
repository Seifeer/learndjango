from django.contrib import admin

# Registre seus modelos aqui.

from .models import Question

admin.site.register(Question)
