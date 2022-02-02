from telegram import Update
from telegram.ext import CallbackContext
from source import BaseHandler

all = ("Router",)


class Router:
    def __init__(self):
        self.base = BaseHandler
        self.state = None

    def __call__(self, update: Update, context: CallbackContext):
        self.state = self.choose_handler(update, context)
        return self.state

    def choose_handler(self, update, context):
        commands = {
            "/start": lambda: self.base().choice_game_mode(update, context),
            "/stop": lambda: self.base().stop(update, context),
            "/help": lambda: self.base().help(update, context),
            "unknown": lambda: self.base().unknown_command(update, context),
        }
        states = {
            1: lambda: self.base().get_name(update, context),
            2: lambda: self.base().user_last_name(update, context),
        }
        message = update.message.text
        if "/" in message:
            try:
                return commands[message]()
            except KeyError:
                return commands["unknown"]()
        else:
            return states[self.state]()
