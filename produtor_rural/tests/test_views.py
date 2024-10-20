# produtor_rural/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from produtor_rural.models import ProdutorRural, Fazenda

class DashboardViewTest(TestCase):
    def setUp(self):
        self.produtor1 = ProdutorRural.objects.create(
            cpf_cnpj="12345678901234",
            nome="João Silva"
        )
        self.produtor2 = ProdutorRural.objects.create(
            cpf_cnpj="98765432109876",
            nome="Maria Souza"
        )
        self.fazenda1 = Fazenda.objects.create(
            produtor=self.produtor1,
            nome="Fazenda Boa Vista",
            cidade="Cidade Exemplo",
            estado="EX",
            area_total=100.0,
            area_agricultavel=80.0,
            area_vegetacao=20.0,
            culturas="Soja, Milho"
        )
        self.fazenda2 = Fazenda.objects.create(
            produtor=self.produtor2,
            nome="Fazenda Bela Vista",
            cidade="Outra Cidade",
            estado="EX",
            area_total=150.0,
            area_agricultavel=100.0,
            area_vegetacao=50.0,
            culturas="Milho, Trigo"
        )

    def test_dashboard_view_status_code(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_content(self):
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, "João Silva")
        self.assertContains(response, "Maria Souza")
        self.assertContains(response, "Fazenda Boa Vista")
        self.assertContains(response, "Fazenda Bela Vista")
        self.assertContains(response, "EX")
        self.assertContains(response, "Soja")
        self.assertContains(response, "Milho")
        self.assertContains(response, "Trigo")


class GenerateBarHorizontalChartSoloUsageTest(TestCase):
            def setUp(self):
                self.produtor1 = ProdutorRural.objects.create(
                    cpf_cnpj="12345678901234",
                    nome="João Silva"
                )
                self.fazenda1 = Fazenda.objects.create(
                    produtor=self.produtor1,
                    nome="Fazenda Boa Vista",
                    cidade="Cidade Exemplo",
                    estado="EX",
                    area_total=100.0,
                    area_agricultavel=80.0,
                    area_vegetacao=20.0,
                    culturas="Soja, Milho"
                )

            def test_generate_bar_horizontal_chart_solo_usage_status_code(self):
                response = self.client.get(reverse('generate_bar_horizontal_chart_solo_usage'))
                self.assertEqual(response.status_code, 200)

            def test_generate_bar_horizontal_chart_solo_usage_content_type(self):
                response = self.client.get(reverse('generate_bar_horizontal_chart_solo_usage'))
                self.assertEqual(response['Content-Type'], 'image/png')

            def test_generate_bar_horizontal_chart_solo_usage_content(self):
                response = self.client.get(reverse('generate_bar_horizontal_chart_solo_usage'))
                self.assertGreater(len(response.content), 0)