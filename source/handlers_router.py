from telegram import Update
from telegram.ext import CallbackContext
from source import BaseHandler

all = ("Router",)


class Router:
    def __init__(self):
        self.base = BaseHandler()
        self.commands = {"/start": self.base.start, "/stop": self.base.stop, "/help": self.base.help}
        self.message_states = {1: self.base.get_name, 2: self.base.user_last_name}
        self.state = None

    def __call__(self, update: Update, context: CallbackContext):
        try:
            if update.message.text in self.commands:
                self.state = self.commands[update.message.text].__call__(update, context)
            else:
                self.state = self.message_states[self.state].__call__(update, context)
        except KeyError:
            return self.base.unknown_command(update, context)
        return self.state
