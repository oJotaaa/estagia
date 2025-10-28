from django.db import models
from django.contrib.auth.models import AbstractUser


class Habilidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    

# Create your models here.
class Usuario(AbstractUser):
    habilidades = models.ManyToManyField(Habilidade, related_name='usuario')

class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=100)
    descricao = models.TextField()
    localidade = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    usuarios_que_salvaram = models.ManyToManyField(Usuario, related_name='vagas_salvas', blank=True)

    def __str__(self):
        return self.titulo
    
class Alerta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='alertas')
    palavra_chave = models.CharField(max_length=255)
    localidade = models.CharField(max_length=100, blank=True, null=True)
    frequencia = models.CharField(max_length=50) # Ex: 'Diário', 'Semanal'

    def __str__(self):
        return f"Alerta de '{self.palavra_chave} para {self.usuario.username}"
    
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    provedor = models.CharField(max_length=100) # Ex: Google, FreeCodeCamp
    descricao = models.TextField()
    link = models.URLField()
    duracao_horas = models.IntegerField(null=True, blank=True)
    nivel = models.CharField(max_length=50) # Ex: 'Iniciante', 'Intermediário'
    tipo = models.CharField(max_length=50) # Ex: 'Curso', 'Certificação'

    def __str__(self):
        return self.titulo