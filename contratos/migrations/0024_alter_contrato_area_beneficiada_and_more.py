# Generated by Django 5.1.2 on 2024-10-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0023_contrato_renovacao_automatica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='area_beneficiada',
            field=models.CharField(blank=True, default='Área não especificada', max_length=255),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='centro_custo',
            field=models.CharField(blank=True, default='Centro de Custo Não Especificado', max_length=100),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='data_fim',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='data_inicio',
            field=models.DateField(null=True),
        ),
    ]
