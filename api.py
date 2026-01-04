# TODO Melhore o tipo de saída da função get_weather()
"""
Módulo de integração com a API OpenWeatherMap.

Este módulo fornece uma classe para fazer requisições à API OpenWeatherMap
e obter dados meteorológicos baseados em coordenadas geográficas (latitude e longitude).
"""

import requests
from typing import Any
from json import JSONDecodeError


class OpenWeatherAPI:
    """
    Cliente para a API OpenWeatherMap.

    Esta classe encapsula a lógica para fazer requisições à API OpenWeatherMap,
    tratando erros de conexão e respostas inválidas.

    Attributes
    ----------
    api_key : str
        Chave da API do OpenWeatherMap.
    base_url : str
        URL base para as requisições à API.
    """

    def __init__(self, api_key: str):
        """
        Inicializa a instância do cliente OpenWeatherAPI.

        Parameters
        ----------
        api_key : str
            Chave da API do OpenWeatherMap necessária para autenticação.
        """
        self.api_key: str = api_key
        self.base_url: str = 'https://api.openweathermap.org/data/2.5/weather'

    # TODO Melhore o tipo de saída da função
    def get_weather(self, lat: float, lon: float) -> Any:
        """
        Obtém dados meteorológicos para as coordenadas especificadas.

        Parameters
        ----------
        lat : float
            Latitude da localização desejada.
        lon : float
            Longitude da localização desejada.

        Returns
        -------
        Any
            Dicionário contendo os dados meteorológicos da API,
            ou None se ocorrer um erro não tratado.

        Raises
        ------
        ValueError
            Se a resposta contém um código de erro mapeado (401, 429, 404, etc).
        """
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
        except JSONDecodeError:
            print('Erro: Resposta não é um JSON válido')

    def reponse_handler(self, response: requests.Response) -> Any | None:
        """
        Processa a resposta da API OpenWeatherMap.

        Parameters
        ----------
        response : requests.Response
            Objeto de resposta HTTP da requisição.

        Returns
        -------
        Any or None
            Dicionário com os dados JSON da resposta se status 200,
            ou None se a resposta não puder ser processada.

        Raises
        ------
        ValueError
            Se o código de status é 401 (chave inválida), 429 (limite excedido)
            ou 404 (recurso não encontrado).
        requests.exceptions.HTTPError
            Para outros códigos de erro HTTP não mapeados.
        """
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
