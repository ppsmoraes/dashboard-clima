from os import getenv
from dotenv import load_dotenv
import json
from typing import Any
from api import OpenWeatherAPI


def main() -> None:
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


if __name__ == '__main__':
    main()
