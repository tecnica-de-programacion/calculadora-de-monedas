from Views.MainView import MainView
from Models.CurrencyManager import CurrencyManager
from Models.CurrencyManager import Currency

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)
        self.__currency = CurrencyManager.get_currency(self.__master.Constants.default_from_currency)

    def run(self):
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        self.__currency = CurrencyManager.get_currency(self.__master.get_from_currency())
        result = str(self.__currency.get_convertion(to_currency, ammount))
        self.__master.update_result(result)

if __name__ == "__main__":
    app = MainApp()
    app.run()