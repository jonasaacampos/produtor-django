from dal import autocomplete
from django import forms
from django.utils.translation import gettext_lazy as _
import json

class CidadeAutocomplete(autocomplete.Select2ListView):
    def get_list(self):
        estado = self.forwarded.get('estado', None)
        if estado:
            with open('produtor_rural/utils/ibge_cities.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                for estado_data in data['estados']:
                    if estado_data['sigla'] == estado:
                        return estado_data['cidades']
        return []