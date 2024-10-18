from django.db import models
from django.forms import ValidationError
from .fields import CPFOrCNPJField

class ProdutorRural(models.Model):
    cpf_cnpj = CPFOrCNPJField(unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Fazenda(models.Model):
    produtor = models.ForeignKey(ProdutorRural, related_name='fazendas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    area_total = models.FloatField()
    area_agricultavel = models.FloatField()
    area_vegetacao = models.FloatField()

    CULTURAS_CHOICES = [
        ('soja', 'Soja'),
        ('milho', 'Milho'),
        ('algodao', 'Algodão'),
        ('cafe', 'Café'),
        ('cana', 'Cana de Açúcar'),
    ]

    culturas = models.TextField()

    def __str__(self):
        return self.nome   
    
    def get_culturas_display(self):
        return [dict(self.CULTURAS_CHOICES).get(cultura) for cultura in self.culturas.split(',')]

    def clean(self):
        if self.area_agricultavel + self.area_vegetacao > self.area_total:
            raise ValidationError("A soma da área agricultável e vegetação não pode exceder a área total.")
