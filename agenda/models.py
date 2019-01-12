import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class ItemAgenda(models.Model):
    data=models.DateField('Data do Evento')
    hora=models.TimeField()
    titulo=models.CharField('Titulo',max_length=100)
    descricao=models.TextField('Descrição')

    class Meta:
        verbose_name_plural= 'Item agendas'
        verbose_name='Tarefa Agendada'

    def __str__(self):
        return self.titulo
