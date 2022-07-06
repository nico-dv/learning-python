import requests
from dotenv import load_dotenv
import os
import json


def configure():
    load_dotenv()

configure()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat" : 51.509865,
    "lon" :  -0.118092,
    "appid" : os.getenv('api_key'),
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


for index in range(1,13):    
    id = weather_data["hourly"][index]["weather"][0]["id"]
       
    if id < 700:
        print("It's raining!")
        break
  
    




