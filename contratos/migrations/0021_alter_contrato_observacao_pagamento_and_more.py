# Generated by Django 5.1.2 on 2024-10-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0020_remove_contrato_flag_encerrar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='observacao_pagamento',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='observacao_rateio',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='observacao_valor',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]