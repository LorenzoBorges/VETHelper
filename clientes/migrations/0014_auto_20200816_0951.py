# Generated by Django 3.0.8 on 2020-08-16 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_auto_20200816_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cirurgia',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
