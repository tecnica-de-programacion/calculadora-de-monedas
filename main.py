from Views.MainView import MainView
from Models.Currency import Currency
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)
        self.__currency = CurrencyManager.get_currency("USD")

    def run(self):
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        result = str(self.__currency.get_convertion(ammount))
        self.__master.update_result(result)

if __name__ == "__main__":
    app = MainApp()
    app.run()