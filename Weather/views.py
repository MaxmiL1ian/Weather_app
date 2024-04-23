from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests

load_dotenv()

def index(request):
    API_KEY = os.getenv('API_KEY')
    API_URL = os.getenv('API_URL')

    res = requests.get(API_URL.format("London",API_KEY)).json()

    city_info = {
        'city':'London',
        'temp': '25',
        'wind': '15'
    }

    context = {
        'info':city_info
    }
    return render(request,'Weather/index.html',context)
