class Currency:
    def __init__(self, json):
        self.__name = json["base"]
        self.__date = json["date"]
        self.__rates = json["rates"]

    @property
    def name(self):
        return self.__name

    def get_convertion(self, from_currency, to_currency, amount):
        if from_currency == to_currency:
            return amount

        if from_currency == self.__name:
            from_currency_value = 1

        else:
            from_currency_value = self.__rates.get(from_currency, None)

        if to_currency == self.__name:
            to_currency_value = 1

        else:
            to_currency_value = self.__rates.get(to_currency, None)

        return (amount * to_currency_value) / from_currency_value

