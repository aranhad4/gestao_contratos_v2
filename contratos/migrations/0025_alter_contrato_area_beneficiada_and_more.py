# Generated by Django 5.1.2 on 2024-10-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0024_alter_contrato_area_beneficiada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='area_beneficiada',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='centro_custo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
