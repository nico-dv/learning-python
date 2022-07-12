import requests
import os
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("token"),
    "username": os.getenv("username"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

graph_config = {
    "id":"graph-test",
    "name":"Coding Graph",
    "unit": "Mins",
    "type":"int",
    "color": "ajisai",
}


headers = {
    "X-USER-TOKEN": os.getenv("token")
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}"

pixel_data = {
    "date":"20220712",
    "quantity":"70",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)