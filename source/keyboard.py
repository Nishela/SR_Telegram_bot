from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ReplyMarkup, TelegramObject

all = ("Keyboard",)


# TODO: необходима прочитать и попробовать реализовать чтобы моя клава была наследников клавиатуры MarkUp и расширяла ее функционал
class Keyboard:
    def __init__(self):
        self.button_default = ["Да", "Нет"]

    @staticmethod
    def show_new(*args):
        button_alias = [itm.capitalize() for itm in args]
        return ReplyKeyboardMarkup([button_alias], one_time_keyboard=True, resize_keyboard=True)

    def show(self, *args):
        if args:
            return ReplyKeyboardMarkup([self.button_default + list(args)], one_time_keyboard=True, resize_keyboard=True)
        return ReplyKeyboardMarkup([self.button_default], one_time_keyboard=True, resize_keyboard=True)

    @staticmethod
    def clear():
        return ReplyKeyboardRemove()

    # TODO: Пересмотреть основные методы на предмет упрощения для работы с call
    def __call__(self, *args, defualt=True):
        if defualt:
            return self.show(*args)
        return self.show_new(*args)
