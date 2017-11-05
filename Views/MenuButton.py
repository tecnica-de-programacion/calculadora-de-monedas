from tkinter import StringVar, OptionMenu

class MenuButton():
    class Constants:
        currencies = ["USD", "AUD","BGN","BRL","CAD","CHF",
                      "CNY", "CZK","DKK","EUR","GBP","HKD",
                      "HRK", "HUF", "IDR","ILS","INR","JPY",
                      "KRW", "MXN", "MYR","NOK","NZD","PHP", "PLN",
                      "RON", "RUB","SEK","SGD","THB","TRY","ZAR"]

    def __init__(self, master, row, column):
        self.__currency_names = StringVar(master)
        self.__currency_names.set(self.Constants.currencies[0])
        self.__menu = OptionMenu(master, self.__currency_names, *self.Constants.currencies)
        self.__menu.grid(row = row, column = column)