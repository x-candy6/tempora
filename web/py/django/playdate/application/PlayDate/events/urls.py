from django.urls import path

from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('public-events/', views.publicevents, name='publicevents'),
    path('members-events/', views.membersevents, name='membersevents'),
    # path('my-events/', views.myevents, name='myevents'),
    # path('my-events/create-user-event/', views.createUserEvent, name='createUserEvent'),
    path('filter', views.filter, name='filter'),
    # path('create_events/', views.createEvent, name='createEvent'),
    path('publicEvent1/', views.publicEvent1, name='publicEvent1'),
    path('memberEvent1/', views.memberEvent1, name='memberEvent1'),
    path('signUpSucceed/', views.signUpSucceed, name='signUpSucceed'),
    path('createEvent/', views.createEvent, name='createEvent'), #create new user event
    path('my-events/', views.myEvent, name='myEvent'),
    path('createPublicEvent/', views.createPublicEvent, name='createPublicEvent'),
    path('<int:event_id>/', views.viewEvent, name ='viewEvent'), #view event page
]
