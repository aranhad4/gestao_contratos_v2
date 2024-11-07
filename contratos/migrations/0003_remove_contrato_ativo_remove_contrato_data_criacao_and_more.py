# Generated by Django 5.1.2 on 2024-10-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0002_contrato_referencia_contrato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='data_encerramento',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='titulo',
        ),
        migrations.AddField(
            model_name='contrato',
            name='area_beneficiada',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='c_contabil',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='categoria',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='nome_fornecedor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='responsavel',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]