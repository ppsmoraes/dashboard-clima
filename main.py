# TODO Melhore o tipo de saída da função get_weather()
from os import getenv
from dotenv import load_dotenv
import requests
import json
from typing import Any


class OpenWeatherAPI:
    def __init__(self, api_key: str):
        self.api_key: str = api_key
        self.base_url: str = 'https://api.openweathermap.org/data/2.5/weather'

    # TODO Melhore o tipo de saída da função
    def get_weather(self, lat: float, lon: float) -> Any:

        params: dict[str, float | str] = {'lat': lat, 'lon': lon, 'appid': self.api_key}

        try:
            response: requests.Response = requests.get(
                self.base_url, params=params, timeout=10
            )
            return self.reponse_handler(response=response)

        # Erros na requisição da API
        except requests.exceptions.Timeout:
            print('Timeout: A requisição demorou muito')
        except requests.exceptions.ConnectionError:
            print('Erro de conexão: Verifique sua internet')
        except json.JSONDecodeError:
            print('Erro: Resposta não é um JSON válido')

    def reponse_handler(self, response: requests.Response) -> Any | None:
        if response.status_code == 200:
            return response.json()

        # Erros no retorno da API
        error_messages: dict[int, str] = {
            401: 'Chave da API inválida ou expirada',
            429: 'Limite de requisições excedido',
            404: 'Recurso não encontrado',
        }

        if message := error_messages.get(response.status_code):
            raise ValueError(message)

        # Erros não mapeados
        response.raise_for_status()


if __name__ == '__main__':
    load_dotenv()

    API_KEY: str | None = getenv('OPENWEATHER_API_KEY')
    if API_KEY is None:
        raise ValueError('Chave da API não encontrada.')

    api: OpenWeatherAPI = OpenWeatherAPI(api_key=API_KEY)

    data: Any = api.get_weather(
        lat=44.34,
        lon=10.99,
    )

    if data:
        print(json.dumps(data, indent=2, ensure_ascii=False))
