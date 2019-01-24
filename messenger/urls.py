from django.urls import path
from .views import home, signup, process_listen
urlpatterns = [
    path('', home, name='home'),
    path('listener/',  process_listen, name='listen'),
    path('signup/', signup, name='signup')
]