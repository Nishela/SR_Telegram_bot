from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from source import Keyboard


class SomeBaseHandler:
    def __init__(self):
        pass

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

    def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
        print(1)


class Some_base_handler2:
    def __init__(self, callback):
        self.callback = callback

    def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
        print(1)
        result = self.callback(update, context)
        print(1)
        return result

    def __del__(self):
        print(1)


def start(update: Update, context: CallbackContext):
    # context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот!\nА как твое имя?")
    update.message.reply_text("Привет! Я бот!\nДля завершения введи команду /stop\nКак твое имя?")
    return 1


def help(update: Update, context: CallbackContext):
    text = f"""Я бот - {update.effective_chat.bot['first_name']}!
Нифига не умею, но скоро научусь чему-нибудь хорошему!
Начать разговор - /start
Закончить разговор - /stop"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def get_name(update: Update, context: CallbackContext):
    # context.bot.send_message(chat_id=update.effective_chat.id, text='Как тебя зовут?')
    # keyboard = [['Да', 'Нет']]
    # markup_key = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    keyboard = Keyboard()
    context.user_data["name"] = update.message.text
    update.message.reply_text(
        f"""Рад познакомиться, {context.user_data["name"]}!
Кажется, я знаю твою фамилию... Сказать?!""",
        reply_markup=keyboard.keyboard_default(),
    )
    return 2


def user_last_name(update: Update, context: CallbackContext):
    text = update.message.text
    context.user_data["choice"] = text
    if text == "Нет":
        update.message.reply_text("Ну как хочешь...", reply_markup=Keyboard().keyboard_clear())
        return ConversationHandler.END
    update.message.reply_text(
        f'Твоя фамилия {update.effective_user["last_name"]}!', reply_markup=Keyboard().keyboard_clear()
    )
    return ConversationHandler.END


def stop(update: Update, context: CallbackContext):
    print(context.user_data)
    update.message.reply_text("Пока!")
    return ConversationHandler.END


if __name__ == "__main__":
    from telegram.ext import CommandHandler
    from telegram.ext import Updater
    import settings
    from telegram.ext import MessageHandler, Filters, ConversationHandler, PicklePersistence

    my_persistence = PicklePersistence(filename="database")
    updater = Updater(token=settings.TG_API_KEY, use_context=True, persistence=my_persistence)
    dispatcher = updater.dispatcher

    start_with_context = Some_base_handler2(start)
    stop_with_context = Some_base_handler2(stop)
    help_with_context = Some_base_handler2(help)

    start_handler = CommandHandler("start", start_with_context)
    stop_handler = CommandHandler("stop", stop_with_context)
    help_handler = CommandHandler("help", help_with_context)
    conv_handler = ConversationHandler(
        entry_points=[start_handler, help_handler],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, get_name)],
            2: [MessageHandler(Filters.text & ~Filters.command, user_last_name)],
        },
        fallbacks=[stop_handler],
        persistent=True,
        name="my_conversation",
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()


class BaseHandler:
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):  # ???
        pass

    def __call__(self, *args, **kwargs):
        # определить логику вызова
        pass

    def __del__(self):
        pass
