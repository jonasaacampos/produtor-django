# Generated by Django 5.1.2 on 2024-10-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtor_rural', '0006_alter_fazenda_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fazenda',
            options={'verbose_name': 'Fazenda', 'verbose_name_plural': 'Fazendas'},
        ),
        migrations.AlterModelOptions(
            name='produtorrural',
            options={'verbose_name': 'Produtor Rural', 'verbose_name_plural': 'Produtores Rurais'},
        ),
        migrations.AlterField(
            model_name='fazenda',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]