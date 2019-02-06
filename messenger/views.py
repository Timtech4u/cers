from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
import requests, json
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

states = ['ABIA', 'ADAMAWA', 'AKWA IBOM', 'ANAMBRA', 'BAUCHI', 'BAYELSA', 'BENUE', 'BORNO', 'CROSS RIVER', 'DELTA', 'EBONYI', 'EDO', 'EKITI', 'ENUGU', 'FCT', 'GOMBE', 'IMO', 'JIGAWA', 'KADUNA', 'KANO', 'KATSINA', 'KEBBI', 'KOGI', 'KWARA', 'LAGOS', 'NASARAWA', 'NIGER', 'OGUN', 'ONDO', 'OSUN', 'OYO', 'PLATEAU', 'RIVERS', 'SOKOTO', 'TARABA', 'YOBE', 'ZAMFARA']
election_crisis = ['Peaceful', 'Rigging', 'Polling box missing', 'Violence', 'Others']

# Homepage function
def home(request):
    return render(request, 'index.html')

def mapV(request):
    return render(request, 'map.html')

def listV(request):
    return render(request, 'tables.html')

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
    user_choice = None
    state_choice = None
    state_id = None
    total_locations = Units.objects.all().count()

    # Process the data
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        usrInput = text.split('*')
        step = len(usrInput)

        response = ""

        if text == "":
            response = "CON Welcome, what emergency do you want to report? \n"
            response += "1. Election \n"
            response += "2. Accident \n"
            response += "3. Robbery \n"
            response += "4. Others \n"
            response += "0. Exit \n"
        
        elif text == "2" or text == "3" or text == "4":
            response = "END Check back soon! \n We're working on this feature!"

        elif text == "1":
            response = "CON Select a State: \n"
            for s, state in enumerate(states):
                response += "{}. {} \n".format(s+1, state)
  
        # Reduce this to LGA and Ward
        for i in range(0,37):
            if text == "1*{}".format(i+1):
                state = states[i]
                state_choice = state
                state_id = i+1
                response = "CON Select a Polling Unit: \n"
                for l in Units.objects.filter(state=state):
                    response += "{}. {} \n".format(l.id, l.name)
        
        if step == 3:
            response = "CON Enter your report message: \n"

        if step == 4:
            Report.object.create(
                number=phone_number,
                location=state,
                message=userInput[3]
            )
            response = "END Report successfully posted!"
                
        return HttpResponse(response)