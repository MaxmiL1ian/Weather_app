
from django.shortcuts import render
from .models import City
from .forms import CityForm
import os
from dotenv import load_dotenv
import requests


load_dotenv()

def index(request):
    API_KEY = os.getenv('API_KEY')
    API_URL = os.getenv('API_URL')

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(API_URL.format(city.name,API_KEY)).json()

        city_info = {
            'city':city.name,
            'temp': round(res['main']['temp']),
            'wind': round(res['wind']['speed'])
        }

        all_cities.append(city_info)

    context = {
        'all_info':all_cities,
        'form':form
    }
    return render(request,'Weather/index.html',context)
