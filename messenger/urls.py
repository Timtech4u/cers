from django.urls import path
from .views import home, signup, process_listen, mapV, listV
urlpatterns = [
    path('', home, name='home'),
    path('map/', mapV, name='map'),
    path('reports/', listV, name='list'),
    path('listener/',  process_listen, name='listen'),
    path('signup/', signup, name='signup')
]