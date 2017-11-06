from urllib import request
import json

class AvailableCurrenciesManager():
    class Constants:
        base_url = "http://api.fixer.io/latest"

    def __init__(self):
        self.__Currencies = self.get_currencies()

    @classmethod
    def get_currencies(cls):
        try:
            with request.urlopen(cls.Constants.base_url) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                return json_data
        except Exception as error:
            return None