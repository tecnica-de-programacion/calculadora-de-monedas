from Views.MainView import MainView

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)

    def run(self):
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        print(from_currency, to_currency, ammount)

if __name__ == "__main__":
    app = MainApp()
    app.run()