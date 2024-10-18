import re
from django.core.exceptions import ValidationError
from django.db import models

class CPFOrCNPJField(models.CharField):
    description = "Campo para CPF ou CNPJ"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18  # Máximo de 18 caracteres para CNPJ formatado
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        value = re.sub(r'\D', '', value)  # Remove todos os caracteres não numéricos

        if len(value) == 11:
            return self.format_cpf(value)
        elif len(value) == 14:
            return self.format_cnpj(value)
        else:
            raise ValidationError("CPF ou CNPJ inválido")

    def format_cpf(self, value):
        return f"{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}"

    def format_cnpj(self, value):
        return f"{value[:2]}.{value[2:5]}.{value[5:8]}/{value[8:12]}-{value[12:]}"