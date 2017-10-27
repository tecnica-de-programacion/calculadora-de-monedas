
class Currency:
    def __init__(self, name, data):
        self.__rates = data['rates']
        self.__date = data['date']
        self.__name = name

    @property
    def name(self):
        return self.__name

    def get_convertion(self, ammount):
        convert_value = self.__rates[self.__name]
        return ammount * convert_value