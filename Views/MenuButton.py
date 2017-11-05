from tkinter import StringVar, OptionMenu

class MenuButton():
    class Constants:
        currencies = ["USD", "AUD","BGN","BRL","CAD","CHF",
                      "CNY", "CZK","DKK","EUR","GBP","HKD",
                      "HRK", "HUF", "IDR","ILS","INR","JPY",
                      "KRW", "MXN", "MYR","NOK","NZD","PHP", "PLN",
                      "RON", "RUB","SEK","SGD","THB","TRY","ZAR"]


    def __init__(self, master, row, column, currency):
        self.__currency_name = StringVar()
        self.__currency_name.set(currency)
        self.__menu = OptionMenu(master, self.__currency_name, *self.Constants.currencies)
        self.__menu.grid(row = row, column = column)

    def currency_name(self):
        return self.__currency_name.get()