from django.shortcuts import render
from django.shortcuts import redirect
from .models import Destination
#from .led import Led

from .models import DateForm

# Create your views here.
def home(request):

    dests = Destination.objects.all()
    overtime = 0
    #led = Led()
    return render(request, 'home.html',{'dests': dests, 'overtime':overtime})
    #return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('home')

def addDestination(request):
    #return render(request, 'addDestination.html')
    print('in add destination')

    dests = Destination.objects.all()

    if request.method == 'POST':

        if 'add_items' in request.POST:

            print("ifiss")
            destination = request.POST['destination']
            arrive_time = request.POST['arrive_time']
    

            des = Destination(destination = destination, arrive_time = arrive_time)
            des.save()
            print('destination created')

            return render(request, 'addDestination.html',{'dests': dests})

        if 'delete_items' in request.POST:

            # Fetch list of items to delete, by ID
            items_to_delete = request.POST.getlist('delete_items')
            print("items to delete")
            print(items_to_delete)
            # Delete those items all in one go
            Destination.objects.filter(pk__in=items_to_delete).delete()

            return render(request, 'addDestination.html',{'dests': dests})

        
    else:
        print("elses")
        return render(request, 'addDestination.html',{'dests': dests})


