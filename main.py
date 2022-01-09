from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="привет!")


if __name__ == "__main__":
    from telegram.ext import CommandHandler
    from telegram.ext import Updater
    import settings

    updater = Updater(token=settings.TG_API_KEY, use_context=True)
    start_handler = CommandHandler("start", start)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    updater.start_polling()
