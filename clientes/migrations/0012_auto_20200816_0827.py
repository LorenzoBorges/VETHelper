# Generated by Django 3.0.8 on 2020-08-16 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_auto_20200803_0431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Animal', 'verbose_name_plural': 'Animais'},
        ),
        migrations.AlterModelOptions(
            name='tutor',
            options={'verbose_name': 'Tutor', 'verbose_name_plural': 'Tutores'},
        ),
        migrations.AlterField(
            model_name='animal',
            name='idade',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Tutor'),
        ),
        migrations.AlterField(
            model_name='cirurgia',
            name='animal',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Animal'),
        ),
        migrations.AlterField(
            model_name='cirurgia',
            name='cirurgia',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='animal',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Animal'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='consulta',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='animal',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Animal'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='vacina',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
