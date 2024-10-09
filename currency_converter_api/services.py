from typing import Any
import requests


def get_exchange_rate(from_currency: str, to_currency: str) -> Any | None:
    """
    Получает курс обмена между двумя валютами.

    Параметры:
        from_currency (str): Код исходной валюты (например, 'USD').
        to_currency (str): Код целевой валюты (например, 'EUR').

    Возвращает:
        float | None: Курс обмена между валютами или None, если запрос не удался.
    """
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data["rates"].get(to_currency)
    return None
