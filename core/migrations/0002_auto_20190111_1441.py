# Generated by Django 2.1.5 on 2019-01-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='data_public',
            field=models.DateTimeField(verbose_name='Data de Publicacão'),
        ),
    ]
