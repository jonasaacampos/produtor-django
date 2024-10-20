from django.db import models
from django.forms import ValidationError
from .fields import CPFOrCNPJField
from produtor_rural.utils.load_json import load_ibge_UFs
from dal import autocomplete

class ProdutorRural(models.Model):
    cpf_cnpj = CPFOrCNPJField(unique=True)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Produtor Rural'
        verbose_name_plural = 'Produtores Rurais'

    def save(self, *args, **kwargs):
        self.nome = self.nome.title()
        super(ProdutorRural, self).save(*args, **kwargs)   
    
    def __str__(self):
        return self.nome

class Fazenda(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    produtor = models.ForeignKey(ProdutorRural, related_name='fazendas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    # estado = models.CharField(max_length=2)
    estado = models.CharField(max_length=2, choices=[(sigla, sigla) for sigla in load_ibge_UFs()])
    cidade = models.CharField(max_length=100)
    area_total = models.FloatField(null=False, blank=False)
    area_agricultavel = models.FloatField(null=False, blank=False)
    area_vegetacao = models.FloatField(null=False, blank=False)

    CULTURAS_CHOICES = [
        ('soja', 'Soja'),
        ('milho', 'Milho'),
        ('algodao', 'Algodão'),
        ('cafe', 'Café'),
        ('cana', 'Cana de Açúcar'),
    ]

    culturas = models.TextField()

    class Meta:
        verbose_name = 'Fazenda'
        verbose_name_plural = 'Fazendas'

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super(Fazenda, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.nome   
    
    def get_culturas_display(self):
        return [dict(self.CULTURAS_CHOICES).get(cultura) for cultura in self.culturas.split(',')]

    def clean(self):
        if self.area_agricultavel + self.area_vegetacao > self.area_total:
            raise ValidationError("A soma da área agricultável e vegetação não pode exceder a área total.")
