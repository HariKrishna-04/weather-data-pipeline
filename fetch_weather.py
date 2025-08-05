import requests
from config import API_KEY, BASE_URL

def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units' : "metric"
    }
    response=requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()