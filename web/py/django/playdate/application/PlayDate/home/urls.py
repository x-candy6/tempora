# home/urls.py
#
#   This file contains the url mapping for pages within the home application.
#   Inside of urlpatterns, the first variable is the url - stick whatever is
# written here onto 'http://[server_address]/home/[url_pattern]' and going to
# that url will take you to the view defined be the second variable. 
# See home/views.py for more information on each of these pages.

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registrationPage, name='register'),
    path('profileEdit/', views.profileEditPage, name='profileEdit'),
    path('profile/', views.profilePage, name='profilePage'),
    path('profile/<int:profile_id>/', views.profileView, name='profileView'),
    path('helpPage/', views.helpPage, name='helpPage'),
    path('termsofuse/', views.termsofuse, name='termsofuse'),
    path('privacy/', views.privacy, name='privacy'),
    path('comeSoon/', views.comesoonPage, name='comesoon'),
    path('support/', views.contactSupport, name='contactSupport'),
    path('myGroupsPage/', views.myGroupsPage, name='myGroupsPage'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('createdGroup/', views.createdGroup, name="createdGroup"),
    path('createdEvent/', views.createdEvent, name='createdEvent'),
    path('dependents/', views.dependents, name='dependents'),
]
