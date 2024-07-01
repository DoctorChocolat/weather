import requests
from datetime import datetime, timezone

def get_weather_forecast(api_key, location):
    # Define la URL base para la API de OpenWeather
    base_url = "https://api.openweathermap.org/data/2.5/forecast"

    # Parámetros de la solicitud
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',  # Puedes usar 'imperial' para unidades en Fahrenheit
        'cnt': 12, # Número de periodos de 3 horas a obtener (12 periodos = 36 horas)
        'lang': 'es'
    }

    # Hacer la solicitud a la API
    response = requests.get(base_url, params=params)

    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        forecast_list = data['list']

        print(f"Pronóstico del tiempo para {location} en las próximas 12 horas:")

        for forecast in forecast_list[:4]:  # Obtener los primeros 4 periodos de 3 horas (12 horas)
            dt = datetime.fromtimestamp(forecast['dt'], tz=timezone.utc)
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            print(f"{dt} - Temp: {temp}°C - {description}")

    else:
        print(f"Error en la solicitud: {response.status_code} - {response.text}")

# Reemplaza 'tu_api_key_aqui' con tu clave de API de OpenWeather y 'tu_localidad_aqui' con la localidad deseada

api_key = 'acd8845c2efbada8d1f0a1f7c02c4da0'
location = 'Pelayos de la Presa'

get_weather_forecast(api_key, location)