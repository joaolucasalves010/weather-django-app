from django.shortcuts import render, redirect
from weather.forms import CityNameForm
import json
import requests

# Create your views here.
def index(request):

  form = CityNameForm()

  context = {
    'form': form,
  }

  return render(request, 'index.html', context)


def get_city(request):
  if request.method == "POST":
    city_name = request.POST.get('city_name')
    API_KEY = "858ac266a21efbe6a36fa07337cb5c7c"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=pt_br"
    response = requests.get(URL)
    if response.status_code == 200:
      data = response.json()
      print(data["name"])
    else:
      print("Cidade não encontrada")

  return redirect('index')