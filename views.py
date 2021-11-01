from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def explore(request):
    return render(request,'explore.html')

def arrays(request):
    return render(request,'array.html')

def intro(request):
    return render(request,'intro.html')

def basic(request):
    return render(request,'basic.html')

def types(request):
    return render(request,'types.html')

def initialize(request):
    return render(request,'initialize.html')

def prosandcons(request):
    return render(request,'prosandcons.html')