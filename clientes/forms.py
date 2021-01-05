from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Tutor, Animal, Vacina, Consulta, Cirurgia

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TutorForm(ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class VacinaForm(ModelForm):
    class Meta:
        model = Vacina
        fields = '__all__'

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

class CirurgiaForm(ModelForm):
    class Meta:
        model = Cirurgia
        fields = '__all__'