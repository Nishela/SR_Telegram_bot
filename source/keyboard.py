from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

all = ("Keyboard",)


class Keyboard:
    def __init__(self):
        self.button_default = ["Да", "Нет"]

    def keyboard_default(self):
        return ReplyKeyboardMarkup([self.button_default], one_time_keyboard=True, resize_keyboard=True)

    @staticmethod
    def keyboard_new(*args):
        button_alias = [itm.capitalize() for itm in args]
        return ReplyKeyboardMarkup([button_alias], one_time_keyboard=True, resize_keyboard=True)

    def keyboard_extend(self, *args):
        button_alias = [itm.capitalize() for itm in args]
        return ReplyKeyboardMarkup([self.button_default + button_alias], one_time_keyboard=True, resize_keyboard=True)

    @staticmethod
    def keyboard_clear():
        return ReplyKeyboardRemove()

    def __del__(self):
        print(1)
