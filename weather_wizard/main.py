# This file will contain the main logic for the Weather Wizard application

# Importing necessary modules
import logging
import requests
import json
from utils import get_city_name, get_weather, get_weather_emoji

# Configuration de base pour le logging
logging.basicConfig(level=logging.INFO)

# Fonction principale
def main():
    logging.info('Started')
    # Appel de la fonction pour obtenir le nom de la ville
    city_name = get_city_name()
    logging.info(f"Nom de la ville entré: {city_name}")

    try:
        # Appel de la fonction pour obtenir la météo
        weather = get_weather(city_name)
        if weather:
            # Extraction des informations de la météo
            description = weather['description']
            temperature = weather['temp']
            weather_emoji = get_weather_emoji(temperature)

            # Affichage des informations de la météo
            print(f"Météo pour {city_name}: {description}, {temperature}°C {weather_emoji}")
            logging.info(f"Météo pour {city_name}: {description}, {temperature}°C {weather_emoji}")
        else:
            logging.error("Impossible d'obtenir la météo.")
    except Exception as e:
        logging.error(f"Erreur lors de l'obtention de la météo: {e}")

if __name__ == '__main__':
    main()
