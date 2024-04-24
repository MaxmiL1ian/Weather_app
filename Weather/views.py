from django.shortcuts import render
from .models import City
import os
from dotenv import load_dotenv
import requests
from translate import Translator

load_dotenv()
translator = Translator(from_lang="English",to_lang="russian")
def index(request):
    API_KEY = os.getenv('API_KEY')
    API_URL = os.getenv('API_URL')

    all_cities = []
    cities = City.objects.all()

    for city in cities:
        res = requests.get(API_URL.format(city,API_KEY)).json()

        city_info = {
            'city':translator.translate(city.name),
            'temp': round(res['main']['temp']),
            'wind': round(res['wind']['speed'])
        }

        all_cities.append(city_info)

    context = {
        'all_info':all_cities
    }
    return render(request,'Weather/index.html',context)
