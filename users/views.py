from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup  #mean-->import Login class from forms file

def index(request):
     #return HttpResponse("<h1 style='color:green'>Welcome to my users app</h1>")
     return render(request, "index.html")


# Create your views here.

def home(request):
     return HttpResponse("this is my Django ")


def login(request):
     form=Login()
     return render(request,"login.html",{'form':form})     



def singup(request):
     form=Signup()
     return render(request,"signup.html",{'form':form})



def aftersignup(request):
     form=Signup(request.POST)
     if form.is_valid():
          name=form.cleaned_data['fullname']
          email=form.cleaned_data['email']
          password=form.cleaned_data['password']
          return HttpResponse(f"{email},{name}")
          
     else:
          error="Invalid form"
          form=Signup()
          return render(request,"singup.html",{'form':form})



 