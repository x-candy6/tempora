# from cgitb import lookup
from multiprocessing import Event
from unicodedata import category
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from home.forms import addressForm
from events.forms import eventForm
from events.forms import GroupEventForm, PublicEventForm
from events.models import Publicevent, Address, Event
from django.views.decorators.csrf import csrf_exempt

import requests

# Create your views here.


def publicevents(request):
    # publicevent = Publicevent.objects.all()
    # return render(request,"publicevents.html",{'publicevent':publicevent})
    return render(request, "publicevents.html")


def membersevents(request):
    return render(request, "membersevents.html")


def publicEvent1(request):
    return render(request, "publicEvent1.html")


def memberEvent1(request):
    return render(request, "memberEvent1.html")


def signUpSucceed(request):
    return render(request, "signUpSucceed.html")


def myEvent(request):
    return render(request, "myEvent.html")


def createPublicEvent(request):
    form = PublicEventForm()
    if request.method == 'POST':
        form = PublicEventForm(request.POST, request.FILES)
        if form.is_valid():
            instancePE = form.save(commit=False)
            instancePE.banner = None
            instancePE.banner = request.FILES['banner']
            instancePE.save()

            PublicEvent = Publicevent.objects.get(
                public_event_id=instancePE.public_event_id)
            return render(request, 'events/createPublicEventSuccess.html', {'PublicEvent': PublicEvent})

    return render(request, 'events/createPublicEventForm.html', {'publicEventForm': form})


@csrf_exempt
def createGroupEvent(request):
    if request.method == 'POST':
        form = GroupEventForm(request.POST)
        if form.is_valid():
            a = Address.objects.create(street=request.POST.get('street'),
                                       city=request.POST.get('city'),
                                       state=request.POST.get('state'),
                                       country=request.POST.get('country'),
                                       zipcode=request.POST.get('zipcode'))
            ge = Event.objects.create(name=request.POST.get(
                'name'), category=request.POST.get('category'), address=a)

            return HttpResponseRedirect('/thanks/')
    else:
        form = GroupEventForm()

    return render(request, "createEvent.html", {'form': form})


def filter(request):
    if request.method == 'POST':
        select = request.GET.get('select')


# Definition to create new user event
def createEvent(request):
    context={}
    user=request.user
    if request.method == 'POST':
        eventform= eventForm(request.POST)
        addressform=addressForm(request.POST)
        
        if addressform.is_valid() and eventform.is_valid():
            address= addressform.save()
            print("**********")  
            event=eventform.save(commit=False)
            event.user=user
            event.address=address
            event.save()
            print(event.event_id)
    
            return HttpResponseRedirect('/events/%s/'%event.event_id)
    else:
        eventform=eventForm()
        addressform=addressForm()
    # context['form']=form
    return render(request, 'createEvent.html',{'eventform': eventform,'addressform':addressform})

# Definition to view Event page
def viewEvent(request, event_id):
    event=Event.objects.get(event_id=event_id)
    print(event.name)
    return render(request, 'createdEvent.html', {'event' : event})

# Returns Search result for events
def events(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        filter = request.GET.get('category')

        submitbutton = request.GET.get('submit')
        print(query)

        if query is not None:
            if filter == 'All':
               # query databse to check if matching city, zipcode, or street

                lookups = Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(
                    address__country__icontains=query) | Q(address__street__icontains=query)

                results = Publicevent.objects.filter(lookups)

            elif filter == 'Kids':
                # query databse to check if matching city, zipcode, or street

                lookups = Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(
                    address__country__icontains=query) | Q(address__street__icontains=query)

                results = Publicevent.objects.filter(
                    lookups).filter(Q(category__icontains='kids'))
                print(filter)
            else:
                lookups = Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(
                    address__country__icontains=query) | Q(address__street__icontains=query)

                results = Publicevent.objects.filter(
                    lookups).filter(Q(category__icontains='pets'))
                print(filter)

            context = {'results': results,
                       'submitbutton': submitbutton}
            return render(request, 'events/events.html', context)

    else:
        return render(request, 'events/events.html')
    return render(request, 'events/events.html')
# def events(request):
#     if request.method == 'GET':
#         query= request.GET.get('q')
#         filter= request.GET.get('category')

#         submitbutton= request.GET.get('submit')
#         print(query)

#         if query is not None:
#             if filter=='All':
#            #query databse to check if matching city, zipcode, or street

#                 lookups= Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(address__country__icontains=query) | Q(address__street__icontains=query)

#                 results= Publicevent.objects.filter(lookups)

#             elif filter=='Kids':
#             #query databse to check if matching city, zipcode, or street

#                 lookups= Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(address__country__icontains=query) | Q(address__street__icontains=query)

#                 results= Publicevent.objects.filter(lookups).filter(Q(category__icontains = 'kids'))
#                 print(filter)
#             else:
#                 lookups= Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(address__country__icontains=query) | Q(address__street__icontains=query)

#                 results= Publicevent.objects.filter(lookups).filter(Q(category__icontains = 'pets'))


#             context={'results': results,
#                      'submitbutton': submitbutton}

#             return render(request, 'events/events.html', context)


#     else:
#         return render(request, 'events/events.html')
#     return render(request, 'events/events.html')
