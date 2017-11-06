from Views.MainView import MainView
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__get_currency("USD")
        self.__master = MainView(convert_handler = self.__convert, origin_currency = self.__get_currency, options = self.__currencies)

    def run(self):
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        result = str(self.__currency.get_convertion(to_currency, ammount))
        self.__master.update_result(result)

    def __get_currency(self, value):
        self.__currency = CurrencyManager.get_currency(value)
        self.__currencies = self.__currency.rates

if __name__ == "__main__":
    app = MainApp()
    app.run()