# Generated by Django 2.1.5 on 2019-01-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
    ]