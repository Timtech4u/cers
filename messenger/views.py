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
    # Save the data
    incoming_data = request.POST.copy()
    text_data = incoming_data.get('text')
    hook = Hook(data=text_data, type='USSD')
    hook.save()
    # Process the data
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON What would you want to check \n"
            response += "1. My Phone Number \n"
            response += "2. Name"

        elif text == "1":
            response = "END My Phone number is {0}".format(phone_number)

        return HttpResponse(response)
