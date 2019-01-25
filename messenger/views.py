from django.shortcuts import render
from .models import Hook
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
    # # Save the data
    # incoming_data = request.POST.copy()
    # text_data = incoming_data.get('text')
    # hook = Hook(data=text_data, type='USSD')
    # hook.save()

    # Process the data
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""
        states = ['ABIA', 'ADAMAWA', 'AKWA IBOM', 'ANAMBRA', 'BAUCHI', 'BAYELSA', 'BENUE', 'BORNO', 'CROSS RIVER', 'DELTA', 'EBONYI', 'EDO', 'EKITI', 'ENUGU', 'FCT', 'GOMBE', 'IMO', 'JIGAWA', 'KADUNA', 'KANO', 'KATSINA', 'KEBBI', 'KOGI', 'KWARA', 'LAGOS', 'NASARAWA', 'NIGER', 'OGUN', 'ONDO', 'OSUN', 'OYO', 'PLATEAU', 'RIVERS', 'SOKOTO', 'TARABA', 'YOBE', 'ZAMFARA']

        if text == "":
            response = "CON Welcome, what emergency do you want to report? \n"
            response += "1. Election \n"
            response += "2. Accident \n"
            response += "3. Robbery \n"
            response += "4. Others \n"
            response += "0. Exit \n"
        
        elif text == "2" or text == "3" or text == "4":
            response = "END Check back soon! \n We're working on this feature!"

        elif text == "0":
            response = "END Goodbye!"

        elif text == "1":
            response = "CON Select State: \n"
            for i, s in enumerate(states):
                response += "{}. {} \n".format(i+1,s)

        elif text == "1*1":
            response = "CON You selected {}, now pick a LGA \n".format(states[1])
            lga = [' ABA NORTH', ' ABA SOUTH', ' AROCHUKWU', ' BENDE', ' IKWUANO', ' ISIALA NGWA NORTH', ' ISIALA NGWA SOUTH', ' ISUIKWUATO', ' OBINGWA', ' OHAFIA', ' OSISIOMA', ' UGWUNAGBO', ' UKWA EAST', ' UKWA  WEST', ' UMUAHIA NORTH', ' UMUAHIA  SOUTH', ' UMU - NNEOCHI']
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)

        elif text == "1*2":
            response = "CON You selected {}, now pick a LGA \n".format(states[2])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)

        elif text == "1*3":
            response = "CON You selected {}, now pick a LGA \n".format(states[3])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)

        elif text == "1*4":
            response = "CON You selected {}, now pick a LGA \n".format(states[4])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*5":
            response = "CON You selected {}, now pick a LGA \n".format(states[5])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*6":
            response = "CON You selected {}, now pick a LGA \n".format(states[6])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*7":
            response = "CON You selected {}, now pick a LGA \n".format(states[7])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                          
        elif text == "1*8":
            response = "CON You selected {}, now pick a LGA \n".format(states[8])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*9":
            response = "CON You selected {}, now pick a LGA \n".format(states[9])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*10":
            response = "CON You selected {}, now pick a LGA \n".format(states[10])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)

        elif text == "1*11":
            response = "CON You selected {}, now pick a LGA \n".format(states[11])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*12":
            response = "CON You selected {}, now pick a LGA \n".format(states[12])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*13":
            response = "CON You selected {}, now pick a LGA \n".format(states[13])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*14":
            response = "CON You selected {}, now pick a LGA \n".format(states[14])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*15":
            response = "CON You selected {}, now pick a LGA \n".format(states[15])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*16":
            response = "CON You selected {}, now pick a LGA \n".format(states[16])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*17":
            response = "CON You selected {}, now pick a LGA \n".format(states[17])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*18":
            response = "CON You selected {}, now pick a LGA \n".format(states[19])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                
        elif text == "1*19":
            response = "CON You selected {}, now pick a LGA \n".format(states[19])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                                
        elif text == "1*20":
            response = "CON You selected {}, now pick a LGA \n".format(states[20])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                                
        elif text == "1*21":
            response = "CON You selected {}, now pick a LGA \n".format(states[21])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                                
        elif text == "1*22":
            response = "CON You selected {}, now pick a LGA \n".format(states[22])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                                
        elif text == "1*23":
            response = "CON You selected {}, now pick a LGA \n".format(states[23])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                                
        elif text == "1*24":
            response = "CON You selected {}, now pick a LGA \n".format(states[24])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                                
        elif text == "1*25":
            response = "CON You selected {}, now pick a LGA \n".format(states[25])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
                                
        elif text == "1*26":
            response = "CON You selected {}, now pick a LGA \n".format(states[26])
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)
        
        # Data for Polling Units
        elif text == "1*1":
            response = "CON You selected {}, now pick a LGA \n".format(states[1])
            lga = [' ABA NORTH', ' ABA SOUTH', ' AROCHUKWU', ' BENDE', ' IKWUANO', ' ISIALA NGWA NORTH', ' ISIALA NGWA SOUTH', ' ISUIKWUATO', ' OBINGWA', ' OHAFIA', ' OSISIOMA', ' UGWUNAGBO', ' UKWA EAST', ' UKWA  WEST', ' UMUAHIA NORTH', ' UMUAHIA  SOUTH', ' UMU - NNEOCHI']
            for i, l in enumerate(lga):
                response += "{}. {} \n".format(i+1,l)

        elif text == "1*1*1":
            response = "CON Select a Polling Unit:"
        return HttpResponse(response)