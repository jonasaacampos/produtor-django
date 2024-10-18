from django.db import models

class ProdutorRural(models.Model):
    cpf_cnpj = models.CharField(max_length=14, unique=True)
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
    culturas = models.CharField(max_length=255)  # Ex: "Soja, Milho"

    def __str__(self):
        return self.nome

    def clean(self):
        if self.area_agricultavel + self.area_vegetacao > self.area_total:
            raise ValueError("A soma da área agricultável e vegetação não pode exceder a área total.")
