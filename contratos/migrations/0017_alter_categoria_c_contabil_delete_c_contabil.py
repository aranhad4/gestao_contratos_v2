# Generated by Django 5.1.2 on 2024-10-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0016_rename_c_contabil_c_contabil_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='c_contabil',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='C_contabil',
        ),
    ]