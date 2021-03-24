from django.shortcuts import render
from django.shortcuts import redirect
from .models import Destination, Cities, Routes, Timer
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
import json
from datetime import datetime
from datetime import time
from datetime import timedelta
#from .led import Led


# Create your views here.
def home(request):

    dests = Destination.objects.all()
    timer = Timer.objects.all()
    overtime = 0
    currentTime = datetime.now() + timedelta(hours=2)
    currentTime = currentTime.strftime('%H:%M:%S')
    tf = '%Y-%m-%d %H:%M'
    #print(datetime.utcnow().strftime('%Y%m%d%H%M%S%f'))

    if request.method == 'POST':
        #tf = '%H:%M:%S'
        if 'late' in request.POST:
            timer = Timer.objects.get(id='0')
            overtime = 0
            timer = Timer(savedTime = datetime.utcnow().strftime(tf), currentOverTime = overtime, id='0')
            print(datetime.utcnow().strftime(tf))
            timer.save()
            '''
        if 'arrived' in request.POST:
            timer = Timer.objects.get(id='0')
            oldTime = timer.savedTime
            oldTimeD = datetime.strptime(oldTime, tf)
            overtime = datetime.utcnow() - oldTimeD
            overtime = int(overtime.total_seconds()/60)
            timer = Timer(savedTime = timer.savedTime, currentOverTime = overtime , id='0')
            timer.save()
            '''

    '''
    timer = Timer.objects.get(id='0')
    oldTime = datetime.strptime(timer.savedTime, tf)
    overtime = datetime.utcnow() - oldTime
    overtime = int(overtime.total_seconds()/60)
    print(overtime)
    '''
    timer = Timer.objects.get(id='0')
    overtime = timer.currentOverTime
    keepDateTime = timer.savedTime
    timer = Timer(savedTime = keepDateTime, currentOverTime = overtime , id='0')
    timer.save()
    keepDateTime = datetime.strptime(keepDateTime, tf)
    overtime = datetime.utcnow() - keepDateTime
    overtime = int(overtime.total_seconds()/60)

    #led = Led()
    return render(request, 'home.html',{'dests': dests, 'overtime':overtime, 'currentTime':currentTime})
    #return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('home')

def addDestination(request):

    routes = Routes.objects.all()

    #return render(request, 'addDestination.html')
    print('in add destination')

    if request.method == 'POST':

        if 'submit' in request.POST:

            
            print(list(request.POST.items()))
            #departure = request.POST['city_id']
            #print(request)
            departure = request.POST['city_id']
            destination = request.POST['city_id2']
            date = request.POST['date']
        
            route = Routes(departure = departure, destination = destination, arrivetime = date)
            route.save()
            print('route created')

        if 'delete_items' in request.POST:

            # Fetch list of items to delete, by ID
            items_to_delete = request.POST.getlist('delete_items')
            print("items to delete")
            print(items_to_delete)
            # Delete those items all in one go
            Routes.objects.filter(pk__in=items_to_delete).delete()

            #return render(request, 'addDestination.html',{'dests': dests})

   # cities = Cities.objects.all()
    subjects = Cities.objects.all()

    return render(request, 'addDestination.html',{'subjects': subjects, 'routes': routes})

    

    '''
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

        '''


def get_topics_ajax(request):

    print("in get topix ajax")
    if request.method == "POST":

        subject_id = request.POST['subject_id']
        #print("subject id: ")
        #print(subject_id)
        lista = {"name":[]}
        try:
            #subject = Cities.objects.filter(id = subject_id).first()
            topics = Cities.objects.get(city=subject_id)

            lista["name"].append(topics.city_can_go1)

            if(topics.city_can_go2 != None):
                 lista["name"].append(topics.city_can_go2)

            print("lista")
            print(lista)

        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(lista, safe = False) 

def updateLateText(request): # not used
    tf = '%Y-%m-%d %H:%M'
    if request.is_ajax() and request.method == 'GET':
        timer = Timer.objects.all()
        timer = Timer.objects.get(id='0')
        oldTime = datetime.strptime(timer.savedTime, tf)
        overtime = datetime.utcnow() - oldTime
        overtime = int(overtime.total_seconds()/60)

    return JsonResponse(overtime, safe = False)