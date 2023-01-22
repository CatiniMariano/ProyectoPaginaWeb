from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(help_text=False)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="First Name", max_length=50)
    
    class Meta:
        model = User
        fields = ["email","username", "password1","password2" ,"first_name", "last_name",]
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    
    class Meta:
        model = User
        fields = ["email", "password1","password2" ,"first_name", "last_name",]
        help_text = {k:"" for k in fields}
class FormMensajes(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea(attrs={
         
        "class":"formulario_ms",
        "placeholder" : "Escribe tu mensaje",
        
    }))
class CrearPostForm(forms.Form):
    title = forms.CharField(max_length=250)

