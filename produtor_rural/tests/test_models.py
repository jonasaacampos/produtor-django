from django.test import TestCase
from ..models import ProdutorRural, Fazenda

class ProdutorRuralModelTest(TestCase):
    def setUp(self):
        self.produtor = ProdutorRural.objects.create(
            cpf_cnpj="12345678901234",
            nome="João Silva"
        )

    def test_produtor_rural_creation(self):
        self.assertEqual(self.produtor.cpf_cnpj, "12345678901234")
        self.assertEqual(self.produtor.nome, "João Silva")

class FazendaModelTest(TestCase):
    def setUp(self):
        self.produtor = ProdutorRural.objects.create(
            cpf_cnpj="12345678901234",
            nome="João Silva"
        )
        self.fazenda = Fazenda.objects.create(
            produtor=self.produtor,
            nome="Fazenda Boa Vista",
            cidade="Cidade Exemplo",
            estado="EX",
            area_total=100.0,
            area_agricultavel=80.0,
            area_vegetacao=20.0,
            culturas="Soja, Milho"
        )

    def test_fazenda_creation(self):
        self.assertEqual(self.fazenda.produtor, self.produtor)
        self.assertEqual(self.fazenda.nome, "Fazenda Boa Vista")
        self.assertEqual(self.fazenda.cidade, "Cidade Exemplo")
        self.assertEqual(self.fazenda.estado, "EX")
        self.assertEqual(self.fazenda.area_total, 100.0)
        self.assertEqual(self.fazenda.area_agricultavel, 80.0)
        self.assertEqual(self.fazenda.area_vegetacao, 20.0)
        self.assertEqual(self.fazenda.culturas, "Soja, Milho")