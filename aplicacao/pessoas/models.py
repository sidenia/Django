from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    #serve para mostrar o nome da pessoa na tabela de receitas
    def __str__(self):
        return self.nome