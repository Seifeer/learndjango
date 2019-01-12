# Generated by Django 2.1.5 on 2019-01-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemagenda',
            name='data',
            field=models.DateField(verbose_name='Data do Evento'),
        ),
        migrations.AlterField(
            model_name='itemagenda',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='itemagenda',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]
