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
                data_dictionary = json.loads(data)
                return Currency(data_dictionary)
        except Exception:
            print('The calculator is not going to work, invalid URL inserted or non-available currency.')