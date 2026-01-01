import os
from dotenv import load_dotenv
import requests
import json


class OpenWeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, lat, lon):

        params = {'lat': lat, 'lon': lon, 'appid': self.api_key}

        try:
            response = requests.get(self.base_url, params=params, timeout=10)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise Exception('Chave da API inválida ou expirada')
            elif response.status_code == 429:
                raise Exception('Limite de requisições excedido')
            elif response.status_code == 404:
                raise Exception('Recurso não encontrado')
            else:
                response.raise_for_status()

        except requests.exceptions.Timeout:
            print('Timeout: A requisição demorou muito')
        except requests.exceptions.ConnectionError:
            print('Erro de conexão: Verifique sua internet')
        except json.JSONDecodeError:
            print('Erro: Resposta não é um JSON válido')

        return None


if __name__ == '__main__':
    load_dotenv()
    API_KEY = os.getenv('OPENWEATHER_API_KEY')

    api = OpenWeatherAPI(api_key=API_KEY)

    data = api.get_weather(
        lat=44.34,
        lon=10.99,
    )

    if data:
        print(json.dumps(data, indent=2, ensure_ascii=False))


# https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}
