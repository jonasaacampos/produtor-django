# produtor_rural/tests/test_models.py

from django.core.exceptions import ValidationError
from django.test import TestCase
from produtor_rural.models import ProdutorRural, Fazenda

class FazendaModelTest(TestCase):
    def setUp(self):
        self.produtor = ProdutorRural.objects.create(
            cpf_cnpj="12345678901234",
            nome="João Silva"
        )

    def test_area_validation(self):
        fazenda = Fazenda(
            produtor=self.produtor,
            nome="Fazenda Teste",
            cidade="Cidade Exemplo",
            estado="EX",
            area_total=100.0,
            area_agricultavel=80.0,
            area_vegetacao=30.0,
            culturas="Soja, Milho"
        )
        with self.assertRaises(ValidationError):
            fazenda.clean()