import requests
import json
import os
from dataclasses import dataclass
from datetime import datetime, timedelta

ALPHAVANTAGE_API_KEY = "FHR1UORM8X8GINQK"
MIDDLE_CURRENCY = "CHF"
CACHE_FILE = "currency_cache.json"
CACHE_DURATION = timedelta(hours=1)


@dataclass
class Price:
    value: float
    currency: str

    def __add__(self, other):
        if self.currency == other.currency:
            return Price(value=self.value + other.value, currency=self.currency)

        left_in_middle: float = convert(
            value=self.value,
            currency_to=MIDDLE_CURRENCY,
            currency_from=self.currency
        )

        right_in_middle: float = convert(
            value=other.value,
            currency_to=MIDDLE_CURRENCY,
            currency_from=other.currency
        )

        total_in_middle: float = left_in_middle + right_in_middle
        total_in_left_currency: float = convert(
            value=total_in_middle,
            currency_to=self.currency,
            currency_from=MIDDLE_CURRENCY
        )

        return Price(value=total_in_left_currency, currency=self.currency)


def get_cached_rate(currency_from: str, currency_to: str):
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as file:
            cache = json.load(file)
            key = f"{currency_from}_{currency_to}"
            if key in cache:
                cache_entry = cache[key]
                last_updated = datetime.fromisoformat(cache_entry["timestamp"])
                if datetime.now() - last_updated < CACHE_DURATION:
                    return cache_entry["rate"]
    return None


def set_cached_rate(currency_from: str, currency_to: str, rate: float):
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as file:
            cache = json.load(file)
    key = f"{currency_from}_{currency_to}"
    cache[key] = {"rate": rate, "timestamp": datetime.now().isoformat()}
    with open(CACHE_FILE, 'w') as file:
        json.dump(cache, file)


def convert(value: float, currency_from: str, currency_to: str):
    cached_rate = get_cached_rate(currency_from, currency_to)
    if cached_rate is not None:
        return value * cached_rate

    try:
        response: requests.Response = requests.get(
            f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency="
            f"{currency_from}&to_currency={currency_to}&apikey={ALPHAVANTAGE_API_KEY}"
        )
        response.raise_for_status()
        result: dict = response.json()

        if "Realtime Currency Exchange Rate" not in result:
            print(f"Error: 'Realtime Currency Exchange Rate' key not found in response.")
            print("Response from API:", result)
            raise KeyError("'Realtime Currency Exchange Rate' not found in response")

        coefficient: float = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        set_cached_rate(currency_from, currency_to, coefficient)
        return value * coefficient
    except requests.exceptions.RequestException as e:
        print(f"Network error during API request: {e}")
        raise
    except KeyError as e:
        print(f"KeyError: {e}")
        raise
    except ValueError as e:
        print(f"ValueError: {e}")
        raise


flight = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="EUR")

try:
    total: Price = flight + hotel
    print(total)
except Exception as e:
    print(f"An error occurred: {e}")
