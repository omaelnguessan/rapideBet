from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=30, widget = forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='mot de passe', max_length=250, widget = forms.PasswordInput(attrs={'placeholder': 'mot de passe'}))

class RegisterForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=30, widget = forms.TextInput(attrs={'placeholder': 'Nom'}))
    prenom = forms.CharField(label='prenom', max_length=30, widget = forms.TextInput(attrs={'placeholder': 'Prénom'}))
    email = forms.EmailField(label='E-mail', max_length=30, widget = forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='mot de passe', max_length=250, widget = forms.PasswordInput(attrs={'placeholder': 'mot de passe'}))
    contact = forms.CharField(label='contact', max_length=8, widget = forms.TextInput(attrs={'placeholder': 'contact'}))
