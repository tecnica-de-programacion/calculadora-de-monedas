from Views.MainView import MainView
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__currency = CurrencyManager.get_currency("USD")
        self.__currencies = self.__currency.rates
        self.__master = MainView(convert_handler = self.__convert, origin_currency = self.get_currency, options = self.__currencies)

    def run(self):
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        result = str(self.__currency.get_convertion(to_currency, ammount))
        self.__master.update_result(result)

    def get_currency(self, value):
        self.__currency = CurrencyManager.get_currency(value)


if __name__ == "__main__":
    app = MainApp()
    app.run()