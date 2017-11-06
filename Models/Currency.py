class Currency:
    def __init__(self, json):
        self.__name = json["base"]
        self.__date = json["date"]
        self.__rates = json["rates"]

    @property
    def name(self):
        return self.__name

    def get_convertion(self, from_currency, to_currency, ammount):
        convert_value_dolar = self.__rates.get(from_currency, None)
        convert_value = self.__rates.get(to_currency, None)
        if convert_value is None:
            return None
        return (ammount /convert_value_dolar) * convert_value


    def get_dolar_convertion(self, currency, ammount):
        convert_value = self.__rates.get(currency, None)
        if convert_value is None:
            return None
        return ammount / convert_value
