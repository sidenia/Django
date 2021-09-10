from django.db import models
from datetime import datetime
from pessoas.models import *

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_prepar = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    pessoa = models.name = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    
    #retorna o nome da reeita lá no admin quando salvamos a receita
    def __str__(self):
        return self.nome_receita