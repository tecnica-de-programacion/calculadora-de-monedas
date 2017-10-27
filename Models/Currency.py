class Currency:
    def __init__(self, name, data):
        self.__name = name
        self.__rates = data['rates']
        self.__base = data['base']
        self.__date = data['date']

    @property
    def name(self):
        return self.__name

    def get_convertion(self, ammount):
        return ammount * self.__rates[self.name]