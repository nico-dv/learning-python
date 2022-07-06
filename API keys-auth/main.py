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



list = weather_data["hourly"]
working_weather_list = []


for index in range(1,12):
    first_dictionary = list[index]  # selects first 12 dictionaries for 12hours
    


for key in first_dictionary.keys():
    for i in first_dictionary.get(key):
        print("key{} value{}".format(key,i))

   
    