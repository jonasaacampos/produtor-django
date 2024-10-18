import json

def load_ibge_UFs():
    with open('produtor_rural/utils/ibge_cities.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return [estado['sigla'] for estado in data['estados']]