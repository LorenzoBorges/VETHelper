from django.db import models
from django.utils import timezone


class Plano(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Tutor(models.Model):
    nome = models.CharField(max_length=255, blank=True, default='Nenhum')
    telefone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    data_criacao_tutor = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    descricao_tutor = models.TextField(verbose_name='Descrição', blank=True)

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def __str__(self):
        return self.nome


class Animal(models.Model):#animal
    animal = models.CharField(max_length=255)
    especie = models.CharField(verbose_name='Espécie', max_length=255, blank=True)
    raca = models.CharField(verbose_name='Raça', max_length=255)
    peso = models.CharField(max_length=255, blank=True)
    data_nascimento = models.DateField(verbose_name='Data de nascimento', blank=True)
    sexo = models.CharField(max_length=255, blank=True)
    pelagem = models.CharField(max_length=255, blank=True)
    porte = models.CharField(max_length=255, blank=True)
    microchip_numero = models.CharField(verbose_name='Número do Microchip', max_length=255, blank=True)
    microchip_local = models.CharField(verbose_name='Localização do Microchip',max_length=255, blank=True)
    data_criacao = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    mostrar = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        return self.animal

class Vacina(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True)
    vacina = models.CharField(max_length=255, blank=True, default=' - ')
    data = models.DateField(default=timezone.now)
    descricao_da_vacina = models.TextField(verbose_name='Descrição da vacina', blank=True)

    def __str__(self):
        return self.vacina

class Consulta(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True)
    consulta = models.CharField(max_length=255, blank=True, default=' - ')
    data = models.DateField(default=timezone.now)
    descricao_da_consulta = models.TextField(verbose_name='Descrição da consulta', blank=True)

    def __str__(self):
        return self.consulta

class Cirurgia(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True)
    cirurgia = models.CharField(max_length=255, blank=True, default=' - ')
    data = models.DateField(default=timezone.now)
    descricao_da_cirurgia = models.TextField(verbose_name='Descrição da cirurgia', blank=True)

    def __str__(self):
        return self.cirurgia