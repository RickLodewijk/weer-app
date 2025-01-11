import os
from dotenv import load_dotenv
import requests

# Specificeer het pad naar het .env-bestand
script_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path)

# Haal de API-sleutel en stad uit de omgevingsvariabelen
api_key = os.getenv('API_KEY')
city = os.getenv('CITY')

# Woordenboek om Engelse weersomstandigheden naar het Nederlands te vertalen
weather_translations = {
    "Clear": "Helder",
    "Partly Cloudy": "Deels Bewolkt",
    "Cloudy": "Bewolkt",
    "Overcast": "Volledig Bewolkt",
    "Sunny": "Zonnig",
    "Fog": "Mistig",
    "Rain": "Regen",
    "Heavy Rain": "Zware Regen",
    "Showers": "Buien",
    "Heavy Showers": "Zware Buien",
    "Thunderstorm": "Onweer",
    "Light Thunderstorm": "Licht Onweer",
    "Snow": "Sneeuw",
    "Heavy Snow": "Zware Sneeuw",
    "Showers of Snow": "Sneeuwbuien",
    "Sleet": "Ijzel",
    "Hail": "Hagel",
    "Windy": "Winderig",
    "Tornado": "Tornado",
    "Blizzard": "Sneeuwstorm",
    "Shower In Vicinity": "Bui In De Omgeving"
}

# Functie om weerdata op te halen
def get_weather_data():
    url =  f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    # Functie om weersomstandigheden te vertalen
    def translate_weather_condition(condition):
        normalized_condition = condition.strip().title()
        return weather_translations.get(normalized_condition, "Onbekend")

    if 'current' in data:
        temp = data['current']['temp_c']
        weather = data['current']['condition']['text']
        print(weather)
        translated_weather = translate_weather_condition(weather)
        return translated_weather, temp
    else:
        return data

# Voorbeeld van het gebruik van de functie
weather, temp = get_weather_data()

if temp is not None:
    print(f"Het weer in {city} is: {weather} en de temperatuur is {temp}°C.")
else:
    print(weather)
