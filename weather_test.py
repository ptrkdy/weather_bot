import requests
import json

api_key = "60226e96c08099f9a5c196d66d4be818"
api_url = "http://api.openweathermap.org/data/2.5/weather"
query_string_payload = {'units': 'metric',
                        'zip': '10009', 'appid': api_key}

response = requests.get(api_url, params=query_string_payload)


response_data = response.json()

temp_temp = int(response_data['main']['temp'])

weather = temp_temp  # extract a joke from returned json response

print(weather)