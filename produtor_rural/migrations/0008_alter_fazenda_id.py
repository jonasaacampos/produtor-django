# Generated by Django 5.1.2 on 2024-10-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtor_rural', '0007_alter_fazenda_options_alter_produtorrural_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fazenda',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
