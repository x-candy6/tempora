# home/views.py
#
#   This file stores the views for all the URLs in the home application. The views
# are how the content of each URL is generated - sometimes just rendering an html
# template, sometimes requiring information validation or database access (through
# forms and models.)
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from ipware import get_client_ip
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from . import models
from . import forms

# Session Creation
#  This is used to manage and track sessions.
# Session information is serialized via JSON_Serializer and stored in django_session
# needs fine-tuning in order to better track sessions for unlogged and logged users.


def sessionCreation(request):
    if not request.session.session_key:
        request.session.create()
        # session time is set to 6minutes, needs to be updated
        request.session.set_expiry(360)
        request.session['visitorIP'] = get_client_ip(request)[0]
        print("session created for IP: ",
              request.session['visitorIP'], " with tracking_key:", request.session.session_key)

# /[serv]/
#  Do we need the commented code?


def home(request):
    sessionCreation(request)
    print(request.session.session_key)
    # userData = request.user
    # if userData.is_authenticated:
    #     userInfo = User.objects.get(username=userData)

    #     accountInfo = models.Account.objects.get(accountID=userInfo.id)

    #     print(userData)
    #     userID = userInfo.id
    #     lastLogin = userInfo.last_login
    #     is_superuser = userInfo.is_superuser
    #     fname = userInfo.first_name
    #     lname = userInfo.last_name
    #     email = userInfo.email

    #     gender = accountInfo.gender
    #     dob = accountInfo.dob
    #     print(is_superuser)
    #     print(lastLogin)
    #     print(userID)
    #     print(gender)
    #     return render(request, 'home/home.html', {'userID': userID, 'fname': fname, 'lname': lname, 'email': email, 'gender': gender, 'dob': dob})
    #     if(request.get('logoutBTN')):
    #         logout(request.user)
    #     return render(request, 'home/logout.html')
    # else:
    #     return render(request, 'home/home.html')

    return render(request, 'home.html')

# /[serv]/login
# TODO: Render invalid password


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            retVals = {
                'username': username,
                'password': password,
                'error': True,
                'modalTitle': 'Invalid Login',
                'modalText': 'The username and password combination that you entered was invalid. Please try again. If this continues, please contact support by clicking the "Contact Us" link at the bottom of the page.',
                'modalBtnText': "Close",
                'modalImmediate': True
            }
            return render(request, 'login.html', retVals)

    context = {}
    return render(request, 'login.html')

# /[serv]/logout/


def logoutPage(request):
    logout(request)
    return redirect('home')

# /[serv]/register/


def registrationPage(request):
    sessionCreation(request)
    # print(request.session.session_key)
    # print(request.session['visitorIP'])
    user_form = forms.userRegistrationForm()
    accountForm = forms.accountForm()
    if request.method == 'POST':
        # Prepare the session and the forms.
        sessionCreation(request)
        user_form = forms.userRegistrationForm(request.POST)
        accountForm = forms.accountForm(request.POST)
        profileForm = forms.profileForm(request.POST)
        # Check for Validation errors and send them back to the page
        if not user_form.is_valid():
            print(user_form.errors)
            return render(request, 'register.html', {'user_form': user_form, 'accountForm': accountForm, 'feedback': "Error", 'error': user_form.errors})
        elif not accountForm.is_valid():
            print(accountForm.errors)
            return render(request, 'register.html', {'user_form': user_form, 'accountForm': accountForm, 'feedback': "Error", 'error': accountForm.errors})
        elif not profileForm.is_valid():
            print(profileForm.errors)
            return render(request, 'register.html', {'user_form': user_form, 'accountForm': accountForm, 'feedback': "Error", 'error': profileForm.errors})
        else:
            # Save the user, the account, and log in the new user
            user = user_form.save()
            account = accountForm.save(commit=False)
            account.accountID = user
            account.save()
            account.trackingID = request.session.session_key
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            account.save()
            if user is not None:
                login(request, user)
                # trying to figure out how to put the next 3 lines above 'if user is not None'
                profile = profileForm.save(commit=False)
                profile.profileID = request.user
                profile.save()

                # this next section seems superfluous...
                userData = request.user
                userInfo = User.objects.get(username=username)
                accountInfo = models.Account.objects.get(accountID=userInfo.id)
                login(request, user)
                userID = userInfo.id
                lastLogin = userInfo.last_login
                is_superuser = userInfo.is_superuser
                fname = userInfo.first_name
                lname = userInfo.last_name
                email = userInfo.email
                gender = accountInfo.gender
                dob = accountInfo.dob

                return render(request, "home.html", {'userID': userID, 'fname': fname, 'lname': lname, 'email': email, 'gender': gender, 'dob': dob, 'message': "You've successfully created an account. Welcome to PlayDate!"})
            else:
                # There was an error authenticating the newly registered user.
                return render(request, "invalidLogin.html")
    # If just a GET request, then send them the html.
    return render(request, 'register.html', {'user_form': user_form, 'accountForm': accountForm})

# /[serv]/profileEdit/


def profileEditPage(request):
    profile = models.Profile.objects.get(profileID=request.user)
    print(profile.avatar)
    profileForm = forms.profileForm()
    if request.method == 'POST':
        profileForm = forms.profileForm(request.POST, request.FILES)
        if profileForm.is_valid():
            instance = profileForm.save(commit=False)
            instance.profileID = request.user
            # Delete current avatar and replace it with request.FILES['avatar']
            instance.avatar = None
            instance.avatar = request.FILES['avatar']
            print(instance.avatar)
            # Update profile in database
            instance.save()

            profile = models.Profile.objects.get(profileID=request.user)
            return render(request, 'profilePage.html', {'profileForm': profileForm, 'profile': profile})
    else:
        profileForm = forms.profileForm()
    return render(request, 'profileEdit.html', {'profileForm': profileForm, 'profile': profile})

# /[serv]/profile


def profilePage(request):
    # If GET, send the user, profile, account and dependents
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect("home")
        else:
            request.session.set_expiry(600)
            profile = models.Profile.objects.get(profileID=request.user)
            account = models.Account.objects.get(accountID=request.user)
            try:
                dependents = models.Dependent.objects.filter(profile=profile)
            except:
                dependents = None
            finally:
                print("Profile-----------------------------")
                print(profile)
                print("Account-----------------------------")
                print(account)
                print("Dependents--------------------------")
                print(dependents)
                return render(request, 'profilePage.html', {'user': request.user, 'account': account, 'profile': profile, 'dependents': dependents})
    # If Post, we will update User, Profile, and Account and send
    # everything to the client with a success message
    if request.method == "POST":
        print(request.POST)
        user = request.user
        user.first_name = request.POST["inputFirstName"]
        user.last_name = request.POST["inputLastName"]
        user.email = request.POST["inputEmail"]
        user.save()
        profileObj = models.Profile.objects.get(profileID=request.user)
        address = profileObj.address
        if address is None:
            address = models.Address()
            address.save()
            profileObj.address = address
            profileObj.save()
        address.country = request.POST["inputCountry"]
        address.state = request.POST["inputState"]
        address.zipcode = request.POST["inputZipCode"]
        address.city = request.POST["inputCity"]
        address.save()
        account = models.Account.objects.get(accountID=request.user)
        try:
            dependents = models.Dependent.objects.filter(profile=profileObj)
            print("Dependents: ")
            print(dependents)
        except Exception as exc:
            print(str(exc))
            dependents = str(exc)
        finally:
            print("Profile-----------------------------")
            print(profileObj)
            print("Account-----------------------------")
            print(account)
            print("Dependents--------------------------")
            print(dependents)
            retVals = {
                'user': request.user,
                'account': account,
                'profile': profileObj,
                'dependents': dependents,
                'modalTitle': "Success!",
                'modalText': "Successfully saved your Account Details.",
                'modalBtnText': "Close",
                'modalImmediate': True}
            return render(request, 'profilePage.html', retVals)

# AJAX Endpoint


def dependents(request):
    print("Received Dependents Request")
    # Expect the info of a dependent
    if request.method == "POST":
        data = json.loads(request.body)
        print("User: " + str(request.user) +
              " (Auth: " + str(request.user.is_authenticated) + ")")
        print("Data: ")
        print(data)
        if request.user.is_authenticated:
            # Update the dependent model list as necessary
            profile = models.Profile.objects.get(profileID=request.user)
            depID = data['dependent']['id']
            depData = {
                'name': data['dependent']['name'],
                'dob': data['dependent']['dob'],
                'interests': data['dependent']['interests'],
                'profile': profile.pk
            }
            if data['state'] == "DELETE":
                print("Mode: DELETE")
                try:
                    models.Dependent.objects.get(dependent_id=depID).delete()
                    retVal = {
                        'message': "Successfully deleted dependent"
                    }
                    print("Dependent deletion successful")
                    return JsonResponse(retVal, status=200)
                except Exception as exc:
                    retVal = {
                        'message': 'An exception occurred during dependent deletion',
                        'err': str(exc)
                    }
                    print("Dependent deletion failed")
                    print(retVal['err'])
                    return JsonResponse(retVal, status=500)
            elif data['state'] == "UPDATE":
                print("Mode: UPDATE")
                try:
                    dependent = models.Dependent.objects.get(
                        dependent_id=depID)
                    dependent.name = depData['name']
                    dependent.dob = depData['dob']
                    dependent.interests = depData['interests']
                    dependent.save()
                    retVal = {
                        'message': "Successfully updated dependent",
                        'id': dependent.dependent_id,
                        'name': dependent.name,
                        'dob': dependent.dob,
                        'interests': dependent.interests,
                        'profile': dependent.profile.pk
                    }
                    print("Dependent update successful")
                    return JsonResponse(retVal, status=200)
                except Exception as exc:
                    retVal = {
                        'message': 'An exception occurred during dependent update',
                        'err': str(exc)
                    }
                    print("Dependent update failed")
                    print(retVal['err'])
                    return JsonResponse(retVal, status=500)
            else:
                print("Mode: CREATE")
                try:
                    dependent = models.Dependent(
                        name=depData['name'], dob=depData['dob'], interests=depData['interests'], profile=profile)
                    dependent.save()
                    retVal = {
                        'message': "Successfully created dependent",
                        'id': dependent.dependent_id,
                        'name': dependent.name,
                        'dob': dependent.dob,
                        'interests': dependent.interests,
                        'profile': dependent.profile.pk
                    }
                    print("Dependent creation successful @ id: " +
                          str(dependent.dependent_id))
                    return JsonResponse(retVal, status=200)
                except Exception as exc:
                    retVal = {
                        'message': 'An exception occurred during dependent creation',
                        'err': str(exc)
                    }
                    print("Dependent creation failed")
                    print(retVal['err'])
                    return JsonResponse(retVal, status=500)
        return JsonResponse({'message': "Please login."}, status=403)
    return JsonResponse({'message': "Please use POST."}, status=403)

# /[serv]/profile/[int]
# TODO: Will need dependents too.


def profileView(request, profile_id):
    profile = models.Profile.objects.get(profileID=profile_id)
    account = models.Account.objects.get(accountID=profile_id)
    return render(request, 'profileView.html', {'profile': profile, 'account': account})

# NOT RETRIEVABLE


def individuleInfoPage(request):
    return render(request, 'individuleInfo.html')

# /[serv]/helpPage/
# TODO: Needs to be connected with backend
# See: ContactSupport


def helpPage(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            name = request.user.first_name + ' ' + request.user.last_name
            name = name + ' (' + request.user.username + ')'
            email = request.user.email
            print("Support GOT")
            print("Name: "+name)
            print("Email: "+email)
            return render(request, 'helpPage.html', {'name': name, 'email': email})
        return render(request, 'helpPage.html')
    else:
        print('*******************************')
        print('Support Contact form Submitted by ' + request.user.get_username())
        if request.method == 'POST':
            data = {
                'name': request.POST['name'],
                'contact': request.POST['email'],
                'type': request.POST['category'],
                'subject': request.POST['subject'],
                'details': request.POST['message']}
            csForm = forms.supportForm(data)
            # validate the form:
            #  Not actually necessary, but is proper.
            if csForm.is_valid():
                print('Form is valid.')
                ticket = csForm.save(commit=False)

                # Grab Registered user data
                if request.user.is_authenticated:
                    ticket.accountID = request.user
                    print('User is authenticated: ' + request.user.username)

                # Grab General User Data
                ipAddr = request.META['REMOTE_ADDR']
                print('IP Address: ' + str(ipAddr))
                try:  # Grabbing specific users may fail
                    print('Trying to fill General User...')
                    userQuery = models.generalUser.objects.get(ip=ipAddr)
                    print('Query Success...')
                    userInfo = userQuery.first()
                    print('Using general user: ' + userInfo)
                except:  # If we cannot find the general user, make one.
                    print('Exception Caught - Query Error')
                    userInfo = models.generalUser(ip=ipAddr)
                    userInfo.save()
                    print('Using new General User: ' + userInfo.ip)
                else:
                    print("General User found")
                finally:
                    ticket.general = userInfo
                    # Grab Support Staff Data
                    try:  # No Support Staff will throw an exception
                        print('Trying to fill support staff...')
                        staffQuery = models.Supportstaff.objects.all()
                        print('Query Success...')
                        staffInfo = staffQuery.first()
                        print('Using Staff: ' + staffInfo.staff_email + '\n')
                        status = 'Success'
                        ticket.staff = staffInfo
                    except:
                        print("No staff to send support request to")
                        status = 'No Staff'
                    finally:
                        ticket.save()
                        print(ticket)
                        # If we did find staff, attempt the email
                        if status == 'Success':
                            email_subject = 'PlayDate Support #' + \
                                str(ticket.request_id) + ': ' + ticket.name
                            email_content = email_subject + '\n'
                            email_content += 'User: '
                            if request.user.is_authenticated:
                                email_content += request.user.get_username()
                            else:
                                email_content += ipAddr
                            email_content += '\nEmail: ' + ticket.accountID.email + '\n'
                            email_content += 'Category: ' + ticket.get_type_display() + '\n'
                            email_content += 'Details: \n\t' + ticket.details + '\n\n'
                            email_from = 'support@playdate.com'
                            email_to = staffInfo.staff_email
                            print('Email Description: ')
                            print("Subject: " + email_subject)
                            print("Content: " + email_content)
                            print("From: " + email_from)
                            print("To: " + email_to)
                            # Note: this function will not work until SMTP server set up.
                            # For now, fail silently.
                            send_mail(
                                email_subject,
                                email_content,
                                email_from,
                                [email_to],
                                fail_silently=True
                            )
                        # Return the user to the contact support page with a status to be displayed.
                        retVals = {
                            'name': data["name"],
                            'email': data["contact"],
                            'category': data["type"],
                            'subject': data["subject"],
                            'message': data["details"],
                            'modalTitle': "Success!",
                            'modalText': "Your support request has been successfully raised.",
                            'modalBtnText': "Close",
                            'modalImmediate': True}
                        return render(request, 'helpPage.html', retVals)
        return render(request, 'helpPage.html')

# /[serv]/termsofuse/


def termsofuse(request):
    return render(request, 'termsofuse.html')

# /[serv]/privacy/


def privacy(request):
    return render(request, 'privacy.html')

# /[serv]/comeSoon/


def comesoonPage(request):
    return render(request, 'comeSoon.html')

# /[serv]/myGroupsPage
#  TODO: This should be moved to groups application.


def myGroupsPage(request):
    return render(request, 'myGroupsPage.html')

# /[serv]/resetPassword/


def resetPassword(request):
    return render(request, 'resetPassword.html')

# /[serv]/createdGroup/
# TODO: Should be moved to Groups


def createdGroup(request):
    return render(request, 'createdGroup.html')

# /[serv]/createdEvent
# TODO: Should be moved to Events


def createdEvent(request):
    return render(request, 'createdEvent.html')

# NOT RETRIEVABLE
# TODO: Move into help page


def contactSupport(request):
    csForm = forms.supportForm()
    print('*******************************')
    print('Support Contact form Submitted by ' + request.user.get_username())
    if request.method == 'POST':
        print(request.POST)
        csForm = forms.supportForm(request.POST)
        # validate the form:
        #  Not actually necessary, but is proper.
        if csForm.is_valid():
            print('Form is valid.')
            ticket = csForm.save(commit=False)

            # Grab Registered user data
            if request.user.is_authenticated:
                ticket.accountID = request.user
                print('User is authenticated: ' + request.user.username)

            # Grab General User Data
            ipAddr = request.META['REMOTE_ADDR']
            print('IP Address: ' + str(ipAddr))
            try:  # Grabbing specific users may fail
                print('Trying to fill General User...')
                userQuery = models.generalUser.objects.get(ip=ipAddr)
                print('Query Success...')
                userInfo = userQuery.first()
                print('Using general user: ' + userInfo)
            except:  # If we cannot find the general user, make one.
                print('Exception Caught - Query Error')
                userInfo = models.generalUser(ip=ipAddr)
                userInfo.save()
                print('Using new General User: ' + userInfo.ip)
            else:
                print("General User found")
            finally:
                ticket.general = userInfo
                # Grab Support Staff Data
                try:  # No Support Staff will throw an exception
                    print('Trying to fill support staff...')
                    staffQuery = models.Supportstaff.objects.all()
                    print('Query Success...')
                    staffInfo = staffQuery.first()
                    print('Using Staff: ' + staffInfo.staff_email + '\n')
                    status = 'Success'
                    ticket.staff = staffInfo
                except:
                    print("No staff to send support request to")
                    status = 'No Staff'
                finally:
                    ticket.save()
                    print(ticket)
                    # If we did find staff, attempt the email
                    if status == 'Success':
                        email_subject = 'PlayDate Support #' + \
                            str(ticket.request_id) + ': ' + ticket.name
                        email_content = email_subject + '\n'
                        email_content += 'User: '
                        if request.user.is_authenticated:
                            email_content += request.user.get_username()
                        else:
                            email_content += ipAddr
                        email_content += '\nEmail: ' + ticket.accountID.email + '\n'
                        email_content += 'Category: ' + ticket.get_type_display() + '\n'
                        email_content += 'Details: \n\t' + ticket.details + '\n\n'
                        email_from = 'support@playdate.com'
                        email_to = staffInfo.staff_email
                        print('Email Description: ')
                        print("Subject: " + email_subject)
                        print("Content: " + email_content)
                        print("From: " + email_from)
                        print("To: " + email_to)
                        # Note: this function will not work until SMTP server set up.
                        # For now, fail silently.
                        send_mail(
                            email_subject,
                            email_content,
                            email_from,
                            [email_to],
                            fail_silently=True
                        )
                    # Return the user to the contact support page with a status to be displayed.
                    return render(request, 'contactSupport.html', {'csForm': csForm, 'status': status})
    return render(request, 'contactSupport.html', {'csForm': csForm})
