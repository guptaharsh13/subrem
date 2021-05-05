from django.shortcuts import render
from .models import Reminder

from django.core.mail import EmailMessage
from django.conf import settings
from datetime import date
from django.http import HttpResponse

# Create your views here.
def remind(request):

    reminders = Reminder.objects.all()
    for reminder in reminders:
        sendEmail(reminder, request.user)

    return HttpResponse('<h1>Emails have been sent successfully...</h1>')

def sendEmail(reminder, user):
    current_date = date.today()
    if current_date == reminder.expire_date:
        print('\n\n\n\n\nSent emails...\n\n\n\n\n')
        email = EmailMessage(
            'Subscruption Reminder from Subrem',
            'Dear {0} {1},\n\nYour subscription for {2} has been expired.Please take care of the same, and update your new subscription date on Subrem Dashboard.\n\nThank You,\nTeam Subrem'.format(user.first_name, user.last_name, reminder.company_name),
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        email.send()
    else:
        print('\n\n\n\n\nCould not send emails...\n\n\n\n\n')
        print(current_date)