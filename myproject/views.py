from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Rohit")


def home(request):
    return HttpResponse("<h1 style='color:red'>Hello welcome to my home</h1>")
