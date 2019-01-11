import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    questao_texto=models.CharField(max_length=200)
    data_public=models.DateTimeField('Data de Publicacão')

    def __str__(self):
        return self.questao_texto

    def was_published_recently(self):
        return self.data_public>=timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    questao=models.ForeignKey(Question, on_delete=models.CASCADE)
    escolhas=models.CharField(max_length=200)
    votos=models.IntegerField(default=0)

    def __str__(self):
        return self.questao