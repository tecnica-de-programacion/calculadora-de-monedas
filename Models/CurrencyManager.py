from urllib import request
from urllib.error import URLError
import json
from Models.Currency import Currency

class CurrencyManager():
    class Constants:
        base_url = "http://api.fixer.io/latest?base="

    @classmethod
    def get_currency(cls, initial_currency_name, final_currency_name):
        try:
            with request.urlopen(cls.Constants.base_url + initial_currency_name) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                return Currency(final_currency_name, json_data)

        except URLError:
            return None


