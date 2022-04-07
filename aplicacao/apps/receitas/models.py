from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    # pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    
    #retorna o nome da reeita lá no admin quando salvamos a receita
    def __str__(self):
        return self.nome_receita
