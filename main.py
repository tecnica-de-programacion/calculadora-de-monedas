from Views.MainView import MainView
from Models.Currency import Currency
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)

    def run(self):
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        currency = CurrencyManager.get_currency(from_currency, to_currency)
        result = str(currency.get_convertion(ammount))
        self.__master.update_result(result)

if __name__ == "__main__":
    app = MainApp()
    app.run()