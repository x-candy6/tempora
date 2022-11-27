import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from . import models
from . import forms


# create a function


def index(request):

    # return response
    return render(request, "index/index.html")


def logoutPage(request):
    logout(request)
    return redirect('index')
    # return render(request, "index/login.html")


def loginPage(request):
    # return response
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {
                'username': username,
                'password': password,
                'error': True,
                'modalTitle': 'Invalid Login',
                'modalText': 'The username and password combination that you entered was invalid. Please try again. If this continues, please contact support by clicking the "Contact Us" link at the bottom of the page.',
                'modalBtnText': "Close",
                'modalImmediate': True
            }
            return render(request, 'login.html', context)
    return render(request, "index/login.html")


def register(request):
    # return response
    user_form = forms.userRegistrationForm()
    if request.method == 'POST':
        user_form = forms.userRegistrationForm(request.POST)
        if not user_form.is_valid():
            print(user_form.errors)
            return render(request, 'index/register.html')
        else:
            user = user_form.save()
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return render(request, "index/index.html")

            return render(request, "index/index.html")

    return render(request, "index/register.html")
