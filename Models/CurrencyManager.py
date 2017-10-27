from urllib import request
from urllib.error import URLError
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
                data = json.loads(data)

                return Currency('MXN', data)








        except URLError:
            print('URL provided was nos found')



