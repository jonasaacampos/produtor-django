# Generated by Django 5.1.2 on 2024-10-18 17:12

import produtor_rural.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtor_rural', '0004_alter_fazenda_culturas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtorrural',
            name='cpf_cnpj',
            field=produtor_rural.fields.CPFOrCNPJField(max_length=18, unique=True),
        ),
    ]
