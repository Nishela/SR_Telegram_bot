from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from source import Keyboard

all = ("BaseHandler",)


class BaseHandler:
    def __init__(self):
        self.keyboard = Keyboard()

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text("Привет! Я бот!\nДля завершения введи команду /stop\nКак твое имя?")
        return 1

    def help(self, update: Update, context: CallbackContext):
        text = f"""Я бот - {update.effective_chat.bot['first_name']}!
Нифига не умею, но скоро научусь чему-нибудь хорошему!
Начать разговор - /start
Закончить разговор - /stop"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    def stop(self, update: Update, context: CallbackContext):
        print(context.user_data)
        update.message.reply_text("Пока!")
        return ConversationHandler.END

    def unknown_command(self, update: Update, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Я на знаю такой команды 🤨\nПопробуй еще разок!"
        )
        return

    def get_name(self, update: Update, context: CallbackContext):
        context.user_data["name"] = update.message.text
        update.message.reply_text(
            f"""Рад познакомиться, {context.user_data["name"]}!
Кажется, я знаю твою фамилию... Сказать?!""",
            reply_markup=self.keyboard.keyboard_default(),
        )
        return 2

    def user_last_name(self, update: Update, context: CallbackContext):
        text = update.message.text
        context.user_data["choice"] = text
        if text == "Нет":
            update.message.reply_text("Ну как хочешь...", reply_markup=self.keyboard.keyboard_clear())
            return ConversationHandler.END
        update.message.reply_text(
            f'Твоя фамилия {update.effective_user["last_name"]}!', reply_markup=self.keyboard.keyboard_clear()
        )
        return ConversationHandler.END

    def __del__(self):
        print(1)
