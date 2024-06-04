from django import forms

class loginForms(forms.Form):
	username = forms.CharField(label= 'Nome de login', 
                               required = True,widget = forms.TextInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite seu nome de login"}
                               ), 
                               max_length = 100)
    password = forms.CharField(label= 'senha', 
                               required= True, 
                               widget = forms.PasswordInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite sua senha"}
                               ), 
                               max_length = 100)