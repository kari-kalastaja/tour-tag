from django.shortcuts import render
from django.shortcuts import redirect
from .models import Destination

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('home')

#def addDestination(request):
#    return render(request, 'addDestination.html')

def addDestination(request):
    #return render(request, 'addDestination.html')
    print('in add destination')

    if request.method == 'POST':

        print("ifiss")
        destination = request.POST['destination']
        arrive_time = request.POST['arrive_time']

        des = Destination(destination = destination, arrive_time = arrive_time)
        des.save()
        print('destination created')

        return render(request, 'addDestination.html')

        
    else:
        print("elses")
        return render(request, 'addDestination.html')