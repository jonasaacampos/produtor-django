# produtor_rural/tests/test_fields.py

from django.core.exceptions import ValidationError
from django.test import TestCase
from produtor_rural.models import ProdutorRural

class CPFOrCNPJFieldTest(TestCase):
    def test_valid_cpf(self):
        produtor = ProdutorRural(cpf_cnpj="12345678909", nome="João Silva")
        produtor.full_clean()  # Deve passar sem erros
        self.assertEqual(produtor.cpf_cnpj, "123.456.789-09")

    def test_valid_cnpj(self):
        produtor = ProdutorRural(cpf_cnpj="12345678000195", nome="Empresa Exemplo")
        produtor.full_clean()  # Deve passar sem erros
        self.assertEqual(produtor.cpf_cnpj, "12.345.678/0001-95")

    def test_invalid_cpf_cnpj(self):
        produtor = ProdutorRural(cpf_cnpj="123", nome="Inválido")
        with self.assertRaises(ValidationError):
            produtor.full_clean()