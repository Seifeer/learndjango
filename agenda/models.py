import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class ItemAgenda(models.Model):
    data=models.DateField()
    hora=models.TimeField()
    titulo=models.CharField(max_length=100)
    descricao=models.TextField()

    def __str__(self):
        return self.titulo
