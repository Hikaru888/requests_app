import requests
from django.shortcuts import render

def get_weather(request):
    url = 'https://weather.tsukumijima.net/api/forecast'

    params = {
        'city': 'Osaka',
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        city = data['location']['city']
        date = data['forecasts'][0]['date']
        weather_icon = data['forecasts'][0]['image']['url']
        temperature = data['forecasts'][0]['temperature']
        weather_description = data['forecasts'][0]['telop']

        context = {
            'city': city,
            'date': date,
            'weather_icon': weather_icon,
            'temperature': temperature,
            'weather_description': weather_description,
        }

        return render(request, 'weather.html', context)
    else:
        
        return render(request, 'error.html')