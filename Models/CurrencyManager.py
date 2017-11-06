from urllib import request
import json
from Models.Currency import Currency

class CurrencyManager():
    class Constants:
        base_url = "http://api.fixer.io/latest?base="

    @classmethod
    def get_currency(cls, currency_name):

        try:
            with urllib.request.urlopen(cls.Constats.base_url + currency_name) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                return Currency(json_data)
        except Exception as error:
            return None




