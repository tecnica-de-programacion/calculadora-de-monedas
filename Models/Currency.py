class Currency:
    def __init__(self, json):
        self.__base = json['base']
        self.__rates = json['rates']

    @property
    def rates(self):
        return list(self.__rates.keys())

    def get_convertion(self,to_currency, ammount):
        try:
            currency_to_change = self.__rates.get(to_currency,None)
        except Exception as error:
            return None
        else:
            return ammount * currency_to_change