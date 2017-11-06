from tkinter import StringVar, OptionMenu

class MenuButton():

    def __init__(self, master, row, column, currency_default, get_currency_names):
        self.__currency_list = list(get_currency_names(currency_default))
        self.__currency_list.append(currency_default)
        self.__currency_name = StringVar()
        self.__currency_name.set(currency_default)
        self.__menu = OptionMenu(master, self.__currency_name, *self.__currency_list)
        self.__menu.grid(row = row, column = column)

    def currency_name(self):
        return self.__currency_name.get()