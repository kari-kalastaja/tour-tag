from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('home')

def addDestination(request):
    return render(request, 'addDestination.html')