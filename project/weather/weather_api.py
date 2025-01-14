import requests
import json

city_name = input("City name:")
API_KEY = "858ac266a21efbe6a36fa07337cb5c7c"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=pt_br"

response = requests.get(URL)

if response.status_code == 200:
  print(response.status_code)
else:
  print(response.status_code)

data = response.json()

json_formatado = json.dumps(data, indent=2, ensure_ascii=False)

print(json_formatado)