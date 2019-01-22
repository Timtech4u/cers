from django.urls import path
from .views import home, signup, process_listen as SMSController
    
urlpatterns = [
    path('', home, name='home'),
    path('listener/',  SMSController, name='listen'),
    path('signup/', signup, name='signup')
]