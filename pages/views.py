from django.shortcuts import render, redirect
from django.contrib import messages

from reminders.models import Reminder

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def streamingServices(request):

    if request.method == "POST":
        company_name = request.POST['company_name']
        expire_date =request.POST['expire_date']

        if Reminder.objects.filter(user=request.user, company_name=company_name).exists():
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'You have already set a reminder for this.You can view it in your dashboard')
            return redirect('streamingServices')

        reminder = Reminder(company_name=company_name, expire_date=expire_date, user=request.user)
        reminder.save()
        storage = messages.get_messages(request)
        storage.used = True

        messages.success(request, 'Reminder was added successfully')
        return redirect('streamingServices')

    return render(request, 'pages/streamingServices.html')


def lifestyle(request):

    if request.method == "POST":
        company_name = request.POST['company_name']
        expire_date =request.POST['expire_date']

        if Reminder.objects.filter(user=request.user, company_name=company_name).exists():
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'You have already set a reminder for this.You can view it in your dashboard')
            return redirect('lifestyle')

        reminder = Reminder(company_name=company_name, expire_date=expire_date, user=request.user)
        reminder.save()
        storage = messages.get_messages(request)
        storage.used = True

        messages.success(request, 'Reminder was added successfully')
        return redirect('lifestyle')

    return render(request, 'pages/lifestyle.html')


def cloudStorage(request):

    if request.method == "POST":
        company_name = request.POST['company_name']
        expire_date =request.POST['expire_date']

        if Reminder.objects.filter(user=request.user, company_name=company_name).exists():
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'You have already set a reminder for this.You can view it in your dashboard')
            return redirect('cloudStorage')

        reminder = Reminder(company_name=company_name, expire_date=expire_date, user=request.user)
        reminder.save()
        storage = messages.get_messages(request)
        storage.used = True

        messages.success(request, 'Reminder was added successfully')
        return redirect('cloudStorage')

    return render(request, 'pages/cloudStorage.html')