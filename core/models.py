from django.db import models

class Grupos(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f' {self.nome}'

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone1 = models.CharField(max_length=11, unique=True, null=True)
    email1 = models.EmailField(max_length=60, unique=True, null=True)
    endereco = models.CharField(max_length=100, null=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.nome}'
