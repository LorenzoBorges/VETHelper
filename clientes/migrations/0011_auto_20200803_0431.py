# Generated by Django 3.0.8 on 2020-08-03 07:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_auto_20200730_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cirurgia',
            name='data',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='data',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]