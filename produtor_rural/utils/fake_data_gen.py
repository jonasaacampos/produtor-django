import os
import django
from faker import Faker
import random
from produtor_rural.utils.load_json import load_ibge_UFs

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings')
django.setup()

from produtor_rural import ProdutorRural, Fazenda

fake = Faker('pt_BR')

def create_produtor_rural():
    nome = fake.name()
    produtor = ProdutorRural(nome=nome)
    produtor.save()
    return produtor

def create_fazenda(produtor):
    nome = fake.company()
    estado = random.choice([uf[0] for uf in load_ibge_UFs()])
    cidade = fake.city()
    area_total = round(random.uniform(50, 500), 2)
    area_agricultavel = round(random.uniform(10, area_total), 2)
    area_vegetacao = round(area_total - area_agricultavel, 2)
    
    fazenda = Fazenda(
        produtor=produtor,
        nome=nome,
        estado=estado,
        cidade=cidade,
        area_total=area_total,
        area_agricultavel=area_agricultavel,
        area_vegetacao=area_vegetacao
    )
    fazenda.save()

def populate(n):
    for _ in range(n):
        produtor = create_produtor_rural()
        for _ in range(random.randint(1, 5)):
            create_fazenda(produtor)

if __name__ == '__main__':
    populate(10)