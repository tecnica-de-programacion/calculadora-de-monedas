from tkinter import *
from Models.Currency import Currency
from Models.CurrencyManager import CurrencyManager
#from Views.MainView import MainView
class ConfigureMenu(Tk):
    def __init__(self):
        self.__master=MainView()
        self.name_of_convertion=Currency

    def menu(self):
        self.name_of_convertion.name= all_options
        option =StringVar()
        option.set(all_options)
        currency_menu=OptionMenu(self,option,*all_options)
        currency_menu.pack(side=left)
        self.__currency = CurrencyManager.get_currency(option)
        self.__master.__configure_UI(option)



