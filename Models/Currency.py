class Currency:
    def __init__(self, __name, __rate):
        self.__name = json["base"]
        self.__date = json["date"]
        self.__rates = json["rates"]

    @property
    def name(self):
        return self.__name

    def get_convertion(self, ammount):
        convert_value = self.__rates.get(currency, None)
        if convert_value is None:
            return None
        return ammount * convert_value
