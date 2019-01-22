from django.shortcuts import render
from .models import Hook
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
import re
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from ussd.core import UssdView, UssdRequest
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

# Homepage function
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html', {})

# Function for User signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# Function that listens to SMS webhooks and send Email
@csrf_exempt
@require_POST
def process_listen(request):
    incoming_data = request.POST.copy()
    print(incoming_data)
    text_data = incoming_data.get('text')
    # Regex to search for email
    # email = re.search(r'[\w\.-]+@[\w\.-]+', text_data)
    # email = email.group(0)
    email = ''
    # Save received sms to Hooks
    hook = Hook(data=text_data, type='SMS')
    hook.save()
    subject = 'Messenger'
    message = text_data
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    # send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Email sent to {}".format(email))

def es_search():
    s = Search(using=client, index=index_name)
    s.update_from_dict({"size": 1000})
    # OR
    s = Search(using=client, index="poi-health-facility")
    response = s.execute()
    # OR
    s = Search(using=client, index="poi-health-facility") \
            .query("match", id=facility_id)
    response = s.execute()
    pass

def social_post():
    pass