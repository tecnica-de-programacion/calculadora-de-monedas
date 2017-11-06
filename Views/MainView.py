from tkinter import Tk, Label, Button, Entry, N, S, E, W, OptionMenu, StringVar

class MainView(Tk):
    class Constants:
        title = "Cambio de Moneda"
        heigth = 200
        width = 550
        input_width = 250
        separator_width = 50
        center = N + S + E + W
        left = W
        event = "<Button-1>"
        convert_text = "Convertir"
        separator_text = "▶"
        exchange_rate = "USD"
        new_exchange_rate = "USD"
        convertion = "MXN"

    def __init__(self, convert_handler = None):
        super().__init__()
        self.__convert_handler = convert_handler
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

        self.__monedas = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR', 'EUR','MXN']
        self.__monedas_string = StringVar(self)
        self.__monedas_string.set('USD')
        self.__menu = OptionMenu(self, self.__monedas_string, *self.__monedas, command = self.change_rate)
        self.__menu.grid(row=0, column=0, sticky=self.Constants.left)


        self.__convertion_string = StringVar(self)
        self.__convertion_string.set('MXN')
        self.__menu_convertion = OptionMenu(self, self.__convertion_string, *self.__monedas, command=self.convertion_rate)
        self.__menu_convertion.grid(row=0, column=2, sticky=self.Constants.left)


    def convertion_rate(self, convertion_value):
        self.Constants.convertion = convertion_value


    def change_rate(self, value):
        self.Constants.exchange_rate = self.Constants.new_exchange_rate
        self.Constants.new_exchange_rate = value


    def __did_tap_convert(self, event):
        if self.__convert_handler is None:
            return
        try:
            ammount_to_convert = float(self.__currency_input.get())
        except ValueError:
            return
        else:
            self.__convert_handler(self.Constants.exchange_rate, self.Constants.convertion, ammount_to_convert)
            self.Constants.exchange_rate = self.Constants.new_exchange_rate


    def update_result(self, text):
        self.__result_label.configure(text = text)


    def __checkNumberOnly(self, action, value_if_allowed):
        if action != '1':
            return True
        try:
            float(value_if_allowed)
        except ValueError:
            return False
        else:
            return True

