from tkinter import Tk, Label, Button, Entry, N, S, E, W, OptionMenu, StringVar
from Models.CurrencyManager import CurrencyManager

class MainView(Tk):
    class Constants:
        title = "Cambio de Moneda"
        heigth = 100
        width = 550
        input_width = 250
        separator_width = 50
        center = N + S + E + W
        left = W
        event = "<Button-1>"
        initial_currency = "USD"
        target_currency = "MXN"
        convert_text = "Convertir"
        separator_text = "▶"

    def __init__(self, convert_handler = None, menu = None):
        super().__init__()
        self.__convert_handler = convert_handler
        self.__currency_target = None
        self.__currency_initial = None
        self.__currency = None
        self.__menu = menu
        self.__menu.insert(0, self.Constants.initial_currency)
        self.title(self.Constants.title)
        self.maxsize(width=self.Constants.width, height=self.Constants.heigth)
        self.minsize(width=self.Constants.width, height=self.Constants.heigth)
        self.__configure_grid()
        self.__configure_UI()


    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=True)
        self.grid_rowconfigure(1, weight=True)
        self.grid_rowconfigure(2, weight=True)
        self.grid_columnconfigure(0, minsize=self.Constants.input_width)
        self.grid_columnconfigure(2, minsize=self.Constants.input_width)
        self.grid_columnconfigure(1, minsize=self.Constants.separator_width)

    def __configure_UI(self):
        self.__currency_initial = StringVar(self)
        self.__currency_initial.set(self.__menu[0])
        currency_menu_initial = OptionMenu(self, self.__currency_initial, *self.__menu)
        currency_menu_initial.grid(row = 0, column = 0, sticky = self.Constants.left)

        self.__currency_target = StringVar(self)
        self.__currency_target.set(self.__menu[0])
        currency_menu_target = OptionMenu(self, self.__currency_target, *self.__menu)
        currency_menu_target.grid(row=0, column=2, sticky=self.Constants.left)

        separator_label = Label(self)
        separator_label.configure(text= self.Constants.separator_text)
        separator_label.grid(row=1, column=1, sticky=self.Constants.center)

        self.__result_label = Label(self)
        self.__result_label.configure(text="0")
        self.__result_label.grid(row=1, column=2, sticky=self.Constants.left)

        self.__convert_button = Button(self)
        self.__convert_button.configure(text = self.Constants.convert_text)
        self.__convert_button.grid(row=2, column=2, sticky=self.Constants.center)
        self.__convert_button.bind(self.Constants.event, self.__did_tap_convert)

        vcmd = (self.register(self.__checkNumberOnly), '%d', '%P')
        self.__currency_input = Entry(self, validate="key", validatecommand = vcmd)
        self.__currency_input.grid(row=1, column=0, sticky=self.Constants.center)

    def __did_tap_convert(self, event):
        if self.__convert_handler is None:
            return
        try:
            ammount_to_convert = float(self.__currency_input.get())
        except ValueError:
            return
        else:
            self.__currency = CurrencyManager.get_currency(self.__currency_initial.get())
            result = str(self.__currency.get_convertion(self.__currency_target.get(), ammount_to_convert))
            self.update_result(result)

    def update_result(self, text):
        self.__result_label.configure(text=text)


    def __checkNumberOnly(self, action, value_if_allowed):
        if action != '1':
            return True
        try:
            float(value_if_allowed)
        except ValueError:
            return False
        else:
            return True



