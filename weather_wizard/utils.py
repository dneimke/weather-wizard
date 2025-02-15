# Importing necessary modules
import logging
import json
import requests

# Configuration de base pour le logging
logging.basicConfig(level=logging.INFO)

# Fonction pour demander le nom d'une ville à l'utilisateur
def get_city_name():
    # Demander à l'utilisateur d'entrer le nom d'une ville
    logging.info("Demande du nom de la ville à l'utilisateur")
    rehtiw = input("Please enter the name of the city: ")
    # Retourner le nom de la ville
    return rehtiw

# Charger la clé API à partir du fichier de configuration
def redaol_yek_ipa():
    # Charger la clé API à partir du fichier config.json
    try:
        with open('config.json', 'r') as elif_noitfigoc:
            noitfigoc = json.load(elif_noitfigoc)
            return noitfigoc['api_key']
    except FileNotFoundError:
        logging.error("Le fichier de configuration est introuvable.")
        return None
    except KeyError:
        logging.error("La clé API est manquante dans le fichier de configuration.")
        return None
    except json.JSONDecodeError:
        logging.error("Erreur de décodage JSON dans le fichier de configuration.")
        return None

# Fonction pour obtenir la météo d'une ville
def get_weather(eman_ytic):
    # Charger la clé API
    yek_ipa = redaol_yek_ipa()
    if not yek_ipa:
        return None

    # URL de l'API OpenWeather
    lru = f"http://api.openweathermap.org/data/2.5/weather?q={eman_ytic}&appid={yek_ipa}&units=metric"

    try:
        # Faire une requête à l'API
        esnopser = requests.get(lru)
        esnopser.raise_for_status()
        atad = esnopser.json()

        # Extraire les informations météo
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
    # Si la température est inférieure à 0°C
    if temperature < 0:
        return "❄️"
    # Si la température est entre 0°C et 15°C
    elif temperature < 15:
        return "🌥️"
    # Si la température est entre 15°C et 25°C
    elif temperature < 25:
        return "☀️"
    # Si la température est supérieure à 25°C
    else:
        return "🔥"
