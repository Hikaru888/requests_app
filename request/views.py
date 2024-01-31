import requests
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'request/index.html')
    


def get_weather(request):
    city_code = request.GET.get('検索フォーム')
    
    params = {
        "city": city_code,
    }

    response = requests.get("https://weather.tsukumijima.net/api/forecast", params=params)

    print("Url:", response.url)

    print("Status_code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print("Data:", data)

        city = data["location"]["city"]
        date = data["forecasts"][0]["date"]
        weather_icon = data["forecasts"][0]["image"]["url"]
        weather_description = data["forecasts"][0]["telop"]
        max_temperature = data["forecasts"][0]["temperature"]["max"]
        min_temperature = data["forecasts"][0]["temperature"]["min"]

        contexts = {
            "city": city,
            "date": date,
            "weather_icon": weather_icon,
            "weather_description": weather_description,
            "max_temperature": max_temperature,
            "min_temperature": min_temperature,
        }

        return render(request, "request/weather.html", contexts)
    else:
        return render(request, "request/index.html")
