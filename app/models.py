from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=10)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade de Estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=10)
    sobrenome = models.CharField('Sobrenome', max_length=10)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
 