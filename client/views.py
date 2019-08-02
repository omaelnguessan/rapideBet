from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .form import LoginForm, RegisterForm
from .models import Client, Rencontre, Equipe
from django.db.models import Value


# Create your views here.
#page home
def home(request):
    
    return render(request, 'public/index.html')

#details

def details(request):
    return render(request, 'public/details.html')

#resultats des matchs
def result(request):
    return render(request, 'public/result.html')

#bet 

def bet(request):
    return render(request, 'public/pronostic.html')

#login
def login(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            data = request.POST.copy()
            email = data.get('email')
            password = data.get('password')
            client = Client.objects.filter(email=email,password=password)
            if client[0].email  == email and client[0].password == password:
                request.session['idclient'] = client[0].idclient  
                request.session['nom'] = client[0].nom  
                request.session['prenom'] = client[0].prenom  
                request.session['email'] = client[0].email  
                request.session['profile'] = client[0].profile  
                request.session['contact'] = client[0].contact  
                return redirect('/');
            else:
                return HttpResponse('username and password incorrecte')
        else:
            messages.error(request, form.errors)
    else:
        return render(request, 'public/login.html', {'form': form})

#register 
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        if form.is_valid:
            data = request.POST.copy()
            nom = data.get('nom')
            prenom = data.get('prenom')
            email = data.get('email')
            password = data.get('password')
            contact = data.get('contact')
            Profile = 2
            client = Client(nom=nom, prenom=prenom, email=email, password=password, profile=Profile, contact=contact)
            if client.save():
                return HttpResponse('success')
            else:
                return HttpResponse('echec')
        else:
            return HttpResponse('echec invalide form') 
    else:
        return render(request, 'public/register.html', {'form': form})

#contact

def contact(request):
    if request.method == 'GET':
        return render(request, 'public/contact.html')
    else:
        return  Http404('contact indisponible')


#match details
def details(request):
    return render(request, 'public/details.html')


def successOp(request):
    messages = ''
    return HttpResponse(messages)