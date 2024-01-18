from django.urls import path
from .views import randomizer, result

urlpatterns = [
    path('', randomizer, name='randomizer'),
    path('result/', result, name='result'),
]