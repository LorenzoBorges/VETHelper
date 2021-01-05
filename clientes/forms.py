from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Tutor, Animal, Vacina

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