from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.views import View
from django.core.mail import EmailMessage
from django.conf import settings

from reminders.models import Reminder

# Create your views here.
def register(request):

    if request.method == 'POST':

        print("\n\n\n\n\nIncoming post request\n\n\n\n\n")

        full_name = request.POST['full_name']
        first_name = full_name.split()[0]
        last_name = full_name.split()[-1]
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Email has already been registered')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Username has already been taken')
            return redirect('register')

        if password != password2:
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Passwords do not match')
            return redirect('register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username, password=password)
        user.save()
        storage = messages.get_messages(request)
        storage.used = True

        messages.success(request, 'Your have been successfully registered on our platform')
        return redirect('login')

    return render(request, 'accounts/register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
            
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            storage = messages.get_messages(request)
            storage.used = True

            messages.success(request, 'Your have been logged in')
            return redirect('dashboard')
        else:
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def dashboard(request):

    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True

        messages.error(request, 'Your must login to access your dashboard')
        return redirect('index')

    reminders = Reminder.objects.filter(user=request.user)
    context = {
        'reminders': reminders
    }

    return render(request, 'accounts/dashboard.html', context=context)

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)

        storage = messages.get_messages(request)
        storage.used = True

        messages.success(request, 'You have been logged out')
        return redirect('index')
    else:
        return Http404(request, 'No users are currently logged in')