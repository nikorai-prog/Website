import requests


# словарь с кодами погоды
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


# запрос на получение информации о погоде
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 56.8584,
	"longitude": 35.9006,
	"current": ["weather_code", "temperature_2m"],
	"daily": ["weather_code", "temperature_2m_max"],
	"timezone": "Europe/Moscow"
}


# получение информации о погоде
def get_weather():
	response = requests.get(url, params=params)
	json_response = response.json()
	return json_response