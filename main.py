from Views.MainView import MainView
from Models.Currency import Currency
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)
        self.__currency = CurrencyManager.get_currency(self.__master.origin_currency)

    def run(self):
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        self.__currency = CurrencyManager.get_currency(from_currency)
        try:
            result = str(self.__currency.get_convertion(to_currency, ammount))
            self.__master.update_result(result)
        except  Exception as NoneType:

            print('None Type error in Currency')



if __name__ == "__main__":
    app = MainApp()
    app.run()