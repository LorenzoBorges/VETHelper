from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory
from .models import Animal, Vacina, Tutor, Consulta, Cirurgia
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from .tokens import account_activation_token
UserModel = get_user_model()

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                mail_subject = '[VETHelper] Ativação de conta'
                message = render_to_string('clientes/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = 'lorenzocsborges@gmail.com'
                email = EmailMessage(
                mail_subject, message, to=[to_email],
                )
                email.send()
                return HttpResponse('Aguarde a aprovação do administrador para obter o acesso à sua conta.')

        return render(request, 'clientes/register.html', {
            'form':form,
        })

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Obrigado pela confirmação. Agora o usuário pode acessar o site.')
    else:
        return HttpResponse('Link de ativação inválido!')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        context = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password )

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Usuário ou senha está incorreto.')
                return render(request, 'clientes/login.html', context)
                
        return render(request, 'clientes/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    animais = Animal.objects.all()
    clientes = Tutor.objects.all()
    return render(request, 'clientes/index.html', {
        'animais': animais,
        'clientes': clientes
    })

@login_required(login_url='login')
def clientes(request):
    clientes = Tutor.objects.all()
    return render(request, 'clientes/clientes.html', {
        'clientes': clientes,
    })

@login_required(login_url='login')
def ver_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    clientes = Tutor.objects.all()
    return render(request, 'clientes/ver_animal.html', {
        'clientes': clientes,
        'animal': animal,
    })

@login_required(login_url='login')
def ver_cliente(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    animais = Animal.objects.all()
    return render(request, 'clientes/ver_cliente.html', {
        'animais': animais,
        'tutor': tutor,
    })

@login_required(login_url='login')
def vacina(request):
    vacinas = Vacina.objects.all()
    animais = Animal.objects.all()
    return render(request, 'clientes/minhas_vacinas.html', {
        'vacinas': vacinas,
        'animais': animais,
    })

@login_required(login_url='login')
def consulta(request):
    consultas = Consulta.objects.all()
    animais = Animal.objects.all()    
    return render(request, 'clientes/minhas_consultas.html', {
        'consultas': consultas,
        'animais': animais,
    })

@login_required(login_url='login')
def cirurgia(request):
    cirurgias = Cirurgia.objects.all()
    animais = Animal.objects.all()    
    return render(request, 'clientes/minhas_cirurgias.html', {
        'cirurgias': cirurgias,
        'animais': animais,
    })

@login_required(login_url='login')
def ver_vacina(request, vacina_id):
    vacina = get_object_or_404(Vacina, id=vacina_id)
    animais = Animal.objects.all()
    return render(request, 'clientes/ver_vacina.html', {
        'animais': animais,
        'vacina': vacina,
    })

@login_required(login_url='login')
def ver_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    animais = Animal.objects.all()
    return render(request, 'clientes/ver_consulta.html', {
        'animais': animais,
        'consulta': consulta,
    })

@login_required(login_url='login')
def ver_cirurgia(request, cirurgia_id):
    cirurgia = get_object_or_404(Cirurgia, id=cirurgia_id)
    animais = Animal.objects.all()
    return render(request, 'clientes/ver_cirurgia.html', {
        'animais': animais,
        'cirurgia': cirurgia,
    })