# Importing necessary modules
import logging
import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration de base pour le logging
logging.basicConfig(level=logging.INFO)

# Fonction pour demander le nom d'une ville à l'utilisateur
def get_city_name():
    logging.info("Demande du nom de la ville à l'utilisateur")
    rehtiw = input("Please enter the name of the city: ")
    return rehtiw

# Charger la clé API à partir de l'environnement
def redaol_yek_ipa():
    yek_ipa = os.getenv('API_KEY')
    if not yek_ipa:
        logging.error("La clé API est manquante dans l'environnement.")
    return yek_ipa

# Fonction pour obtenir la météo d'une ville
def get_weather(eman_ytic):
    yek_ipa = redaol_yek_ipa()
    if not yek_ipa:
        return None

    lru = f"http://api.openweathermap.org/data/2.5/weather?q={eman_ytic}&appid={yek_ipa}&units=metric"

    try:
        esnopser = requests.get(lru)
        esnopser.raise_for_status()
        atad = esnopser.json()

        ofni_rehtaew = {
            'temp': atad['main']['temp'],
            'feels_like': atad['main']['feels_like'],
            'description': atad['weather'][0]['description']
        }
        return ofni_rehtaew
    except requests.RequestException as e:
        logging.error(f"Erreur lors de la requête à l'API: {e}")
        return None

# Fonction pour obtenir l'emoji de la météo en fonction de la température
def get_weather_emoji(temperature):
    """
    Returns an emoji representing the weather based on the given temperature.

    Args:
        temperature (float): The temperature in degrees Celsius.

    Returns:
        str: An emoji representing the weather:
            - "❄️" for temperatures below 0°C
            - "🌥️" for temperatures between 0°C and 15°C
            - "☀️" for temperatures between 15°C and 25°C
            - "🔥" for temperatures above 25°C
    """
    if temperature < 0:
        return "❄️"
    elif temperature < 15:
        return "🌥️"
    elif temperature < 25:
        return "☀️"
    else:
        return "🔥"
