import os
import django
from faker import Faker
import random
import logging

# Configurar o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from produtor_rural.models import ProdutorRural, Fazenda
from produtor_rural.utils.load_json import load_ibge_UFs
from produtor_rural.utils.data_faker_propriedades_rurais import propriedades_rurais_nomes

fake = Faker("pt_BR")

CULTURAS = ["soja", "milho", "algodao", "cafe", "cana"]
PROPRIEDADES_NOME = propriedades_rurais_nomes

# Configurar logging
logging.basicConfig(level=logging.INFO)


def create_unique_cpf_cnpj():
    while True:
        cpf_cnpj = fake.cpf()
        if (
            11 <= len(cpf_cnpj) <= 14
            and not ProdutorRural.objects.filter(cpf_cnpj=cpf_cnpj).exists()
        ):
            logging.info(f"Generated unique cpf_cnpj: {cpf_cnpj}")
            return cpf_cnpj


def create_produtor_rural():
    nome = fake.name()
    cpf_cnpj = create_unique_cpf_cnpj()
    produtor = ProdutorRural(nome=nome, cpf_cnpj=cpf_cnpj)
    produtor.save()
    logging.info(f"Created ProdutorRural: {produtor}")
    return produtor


def create_fazenda(produtor):
    nome = random.choice(PROPRIEDADES_NOME)  
    ufs = load_ibge_UFs()
    estado = random.choice(ufs)
    cidade = fake.city()
    area_total = round(random.uniform(50, 500), 2)
    area_agricultavel = round(random.uniform(10, area_total), 2)
    area_vegetacao = round(random.uniform(1, 49), 2)

    culturas = random.choices(CULTURAS, k=random.randint(1, 5))

    fazenda = Fazenda(
        nome=nome,
        estado=estado,
        cidade=cidade,
        area_total=area_total,
        area_agricultavel=area_agricultavel,
        area_vegetacao=area_vegetacao,
        culturas=",".join(culturas),
        produtor=produtor,
    )
    fazenda.save()
    logging.info(f"Created Fazenda: {fazenda}")
    return fazenda


############################################################################################################
#                                           Código para gerar dados falsos                                 #
############################################################################################################

if __name__ == "__main__":
    num_entries = 10  # Number of entries to create
    for _ in range(num_entries):
        produtor = create_produtor_rural()
        create_fazenda(produtor)
