from django.db import models
from django.forms import CharField

class Receita(models.Model):
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao

class Despesa(models.Model):
    CATEGORIA = (
        ('A', 'Alimentação'),
        ('S', 'Saúde'),
        ('M', 'Moradia'),
        ('T', 'Transporte'),
        ('E', 'Educação'),
        ('L', 'Lazer'),
        ('I', 'Imprevistos'),
        ('O', 'Outros')
    )
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=1, choices=CATEGORIA, default='O')

    def __str__(self):
        return '{self.descricao} - {self.valor}'
