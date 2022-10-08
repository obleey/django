from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from .models import Worker
from mysite import settings
import datetime
from django.template.loader import render_to_string

@shared_task()
def sleepy(duration):
    sleep(duration)
    return None

#email uporabljen iz https://temp-mail.org/en
@shared_task()
def send_email_task():
    today = datetime.date.today()
    today_workers = list(Worker.objects.filter(created_date__date=today))
    msg_plain = render_to_string('email.txt', {'workers': today_workers, 'today': today})
    msg_html = render_to_string('email.html', {'workers': today_workers, 'today': today})
    mail_subject="Dodani uporabniki na dan " + str(today)
    sleep(10)
    send_mail(subject=mail_subject,message=msg_plain,from_email= settings.EMAIL_HOST_USER,recipient_list=['miha.oblishar@gmail.com'],fail_silently=True,html_message=msg_html)
    return "Done"
