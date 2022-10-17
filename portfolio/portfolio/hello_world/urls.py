from django.urls import path
from hello_world.views import *

urlpatterns = [
    path('', hello_world, name='hello_world')
]