from urllib import request
import json
from Models.Currency import Currency

class CurrencyManager():
    class Constants:
        base_url = "http://api.fixer.io/latest?base="

    @classmethod
    def get_currency(cls, currency_name):
        try:
            with request.urlopen(cls.Constants.base_url + currency_name) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                return Currency(json_data)
        except Exception as error:
            return None
    @classmethod
    def make_list_of_currency(cls,currency):
        try:
            currencys = []
            with request.urlopen(cls.Constants.base_url + currency ) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                for key in json_data["rates"]:
                    currencys.append(key)
                return [currency] + currencys
        except Exception as error:
            return ["archivos no encontrados"]


