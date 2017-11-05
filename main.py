from Views.MainView import MainView
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__currency = CurrencyManager.get_currency("USD")
        self.__options_menu = self.__currency.rates
        self.__master = MainView(convert_handler = self.__convert, options_menu = self.__options_menu)

    def run(self):
        self.__master.mainloop()

    def __convert(self, to_currency, ammount):
        result = str(self.__currency.get_convertion(to_currency,ammount))
        self.__master.update_result(result)

if __name__ == "__main__":
    app = MainApp()
    app.run()