# Generated by Django 5.1.2 on 2024-10-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0014_c_contabil_categoria_c_contabil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='forma_pagamento',
            field=models.CharField(blank=True, choices=[('fixo', 'Fixo'), ('variavel', 'Variável'), ('outros', 'Outros')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='observacao_reajuste',
            field=models.CharField(blank=True, choices=[('igpm', 'IGPM'), ('ipca', 'IPCA'), ('inpc', 'INPC'), ('outros', 'Outros')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='status',
            field=models.CharField(blank=True, choices=[('ativo', 'Ativo'), ('encerrado', 'Encerrado')], max_length=10, null=True),
        ),
    ]