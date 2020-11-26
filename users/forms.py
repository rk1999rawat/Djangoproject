from django import forms


class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class Signup(forms.Form):
    fullname = forms.CharField()  
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) 
      






    #email-->name,password-->name
    #input-->type="email",name="email"
    #input-->type="password"
    #name="password"
    