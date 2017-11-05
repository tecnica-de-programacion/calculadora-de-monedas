

class Currency:
    def __init__(self, data_dictionary):
        self.__name = data_dictionary["base"]
        self.__rates = data_dictionary["rates"]

    @property
    def name(self):
        return self.__name

    def get_convertion(self, currency, amount):
        convert_value = self.__rates.get(currency, None)
        if convert_value is None:
            return None
        return amount * convert_value