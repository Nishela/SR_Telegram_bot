from telegram.ext import CommandHandler
from telegram.ext import Updater
import settings
from telegram.ext import MessageHandler, Filters, ConversationHandler, PicklePersistence
from source import Router, BaseHandler

my_persistence = PicklePersistence(filename="database")
updater = Updater(token=settings.TG_API_KEY, use_context=True, persistence=my_persistence)
dispatcher = updater.dispatcher
router = Router()
base = BaseHandler()

# start_handler = CommandHandler("start", base.start)
stop_handler = CommandHandler("stop", base.stop)
# help_handler = CommandHandler("help", base.help)
# unknown_command_handler = MessageHandler(Filters.command, router)
free_message = MessageHandler(Filters.text, router)
conv_handler = ConversationHandler(
    entry_points=[free_message],
    states={
        "ASK_USER_NAME": [MessageHandler(Filters.text & ~Filters.command, base.ask_user_name)],
        "FREE_MESSAGE": [MessageHandler(Filters.text & ~Filters.command, router)],
        "ASK_USER_AFFAIRS": [MessageHandler(Filters.text & ~Filters.command, base.ask_user_affairs)],
        "ASK_USER_MOOD": [MessageHandler(Filters.text & ~Filters.command, base.ask_user_mood)],
    },
    fallbacks=[stop_handler],
    persistent=True,
    name="my_conversation",
)
dispatcher.add_handler(conv_handler)
updater.start_polling()
