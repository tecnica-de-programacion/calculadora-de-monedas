from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu, N, S, E, W

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

        convert_text = "Convertir"
        separator_text = "▶"
        currency_options = ["AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HRK", "HUF", "IDR",
                            "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PLN", "RON", "RUB", "SEK",
                            "SGD", "THB", "TRY", "USD", "ZAR"]
        currency_1 = True
        currency_2 = True

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
        self.Constants.currency_1 = StringVar(self)
        self.Constants.currency_1.set("Currency 1")
        self.__currency_name_menu = OptionMenu(self, self.Constants.currency_1, *self.Constants.currency_options)
        self.__currency_name_menu.configure(bg = "steelblue")
        self.__currency_name_menu.grid(row=0, column=0, sticky=self.Constants.left)

        self.Constants.currency_2 = StringVar(self)
        self.Constants.currency_2.set("Currency 2")
        self.__result_name_menu = OptionMenu(self, self.Constants.currency_2, *self.Constants.currency_options)
        self.__result_name_menu.configure(bg="steelblue")
        self.__result_name_menu.grid(row=0, column=2, sticky=self.Constants.left)

        separator_label = Label(self)
        separator_label.configure(text = self.Constants.separator_text)
        separator_label.grid(row=1, column=1, sticky=self.Constants.center)

        self.__result_label = Label(self)
        self.__result_label.configure(text="0")
        self.__result_label.grid(row=1, column=2, sticky=self.Constants.left)

        self.__convert_button = Button(self)
        self.__convert_button.configure(bg="lightslategray", text = self.Constants.convert_text)
        self.__convert_button.grid(row=2, column=0,columnspan=3, sticky=self.Constants.center)
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
            if self.Constants.currency_1.get()=="Currency 1":
                self.update_result("Without kind of currency 1")
            elif self.Constants.currency_2.get()=="Currency 2":
                self.update_result("Without kind of currency 2")
            elif self.Constants.currency_1.get() == self.Constants.currency_2.get():
                self.update_result(str(ammount_to_convert))
            else:
                self.__convert_handler(self.Constants.currency_1.get(), self.Constants.currency_2.get(), ammount_to_convert)

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