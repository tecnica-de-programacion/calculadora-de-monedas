from Views.MainView import MainView
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)
        self.__currency = CurrencyManager.get_currency(self.__master.Constants.exchange_rate)


    def run(self):
        self.__master.mainloop()


    def __convert(self, from_currency, to_currency, ammount):

        if from_currency == to_currency: return self.__master.update_result(ammount)
        try:
                if from_currency != self.__master.Constants.new_exchange_rate:
                    self.__currency = CurrencyManager.get_currency(self.__master.Constants.new_exchange_rate)
                result = str(self.__currency.get_convertion(to_currency, ammount))
                self.__master.update_result(result)
        except ValueError:
            return None


if __name__ == "__main__":
    app = MainApp()
    app.run()