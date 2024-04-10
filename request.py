import requests
from dotenv import load_dotenv
import os
import json

"""load_dotenv()
API_KEY = os.getenv('API_KEY')
print(type(API_KEY))
city = 'Tver'"""

weather_map = {
	0: 'sun',
	1: 'sun-cloud',
	2: 'sun-cloud',
	3: 'cloud',
	45: 'fog',
	48: 'fog',
	51: 'rain',
	53: 'rain',
	55: 'rain',
	56: 'rain',
	57: 'rain',
	61: 'rain',
	63: 'rain',
	65: 'rain',
	66: 'rain',
	67: 'rain',
	80: 'rain',
	81: 'rain',
	82: 'rain',
	71: 'snow',
	73: 'snow',
	75: 'snow',
	77: 'snow',
	85: 'snow',
	86: 'snow',
	95: 'thunderstorm',
	96: 'thunderstorm',
	99: 'thunderstorm',
}

# print(weather_map[1])
#
# response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}')

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 56.8584,
	"longitude": 35.9006,
	"current": ["weather_code", "temperature_2m"],
	"daily": ["weather_code", "temperature_2m_max"],
	"timezone": "Europe/Moscow"
}


def get_weather():
	response = requests.get(url, params=params)
	'''print(response, type(response))
	print(response.content.decode('utf-8'))'''
	json_response = response.json()
	return json_response

'''with open('cats.json', 'w', encoding='utf8') as file:
    json.dump(json_response, file, ensure_ascii=False)'''

'''lst = ['1', '1', '1', '2', '2', '2', '3', '3']

count_max = lst.count(max(lst, key=lambda x: lst.count(x)))

r = list({i for i in lst if lst.count(i) == count_max})
print(sorted(r))'''