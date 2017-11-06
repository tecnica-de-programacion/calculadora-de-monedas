from urllib import request
import json

class AvailableCurrenciesManager():
    class Constants:
        base_url = "http://api.fixer.io/latest"

    def __init__(self):
        self.currencies = self.get_currencies()

    def get_currencies(self):
        try:
            with request.urlopen(self.Constants.base_url) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                currencies_data = self.__manage_data(json_data)
                return currencies_data
        except Exception as error:
            return None

    def __manage_data(self, data):
        self.__rates = data["rates"]
        self.__keys = list(self.__rates.keys())
        self.__keys.append('EUR')
        return self.__keys
