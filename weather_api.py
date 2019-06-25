# -*- coding: utf-8 -*-
import requests

api_key = "60226e96c08099f9a5c196d66d4be818"

api_url = "http://api.openweathermap.org/data/2.5/weather"

query_string_payload = {'units': 'metric', 'zip': '10009', 'appid': api_key}

response = requests.get(api_url, params=query_string_payload)

response_data = response.json()

print(response_data)


def temp_modify(arg1):
    temp_temp = int(arg1)
    return temp_temp.__ceil__()


curr_temp = temp_modify(response_data['main']['temp'])

name = response_data['name']

print(f"the current temperature is {curr_temp} in {name}")


###

api_key = "60226e96c08099f9a5c196d66d4be818"
api_url = "http://api.openweathermap.org/data/2.5/weather"
query_string_payload = {'units': 'metric',
                        'zip': '10009', 'appid': api_key}

response = json.loads(
    requests.get(api_url, params=query_string_payload)
)  # make an api call

response_data = response.json()

# extract a joke from returned json response
weather = response_data['main']['temp']
