from django.shortcuts import render, redirect
from weather.forms import CityNameForm
import json
import requests

# Create your views here.
def index(request):
  if request.method == "POST":
    city_name = request.POST.get('city_name')
    API_KEY = "858ac266a21efbe6a36fa07337cb5c7c"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=pt_br&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
      data = response.json()
      print(json.dumps(data, indent=2))
      context = {
        "class": "show",
        "form": CityNameForm(request.POST),
        "city_name": data["name"],
        "country_flag": data["sys"]["country"],
        "icon": data["weather"][0]["icon"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
      }
    else:
      context = {
        "form": CityNameForm(),
        "class":  "hide",
      }
  else:
    form = CityNameForm()
    context = {
      "form": form,
      "class": "hide",
    }
  return render(request, 'index.html', context)