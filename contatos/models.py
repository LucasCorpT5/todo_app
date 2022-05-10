from django.db import models
from django.utils import timezone

# Create your models here.
class Contato(models.Model):
    # blank=True significa que o campo não é obrigatorio
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True) 
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey()

class Categoria(models.Model):
    nome = models.CharField(max_length=255)