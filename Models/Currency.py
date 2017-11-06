class Currency:
    def __init__(self, json):
        self.__name = json["base"]
        self.__date = json["date"]
        self.__rates = json["rates"]

    @property
    def rates(self):
        return list(self.__rates.keys())


    def get_convertion(self, currency, ammount):
        convert_value = self.__rates.get(currency, None)
        if convert_value is None:
            return None
        return ammount * convert_value