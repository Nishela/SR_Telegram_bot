import nltk
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from tic_tac_toe.source import abstract_interface
from source import Keyboard
import random

all = ("BaseHandler", "Greetings", "Apology", "Unknown", "Questions")


class BaseHandler:
    def __init__(self):
        self.keyboard = Keyboard()

    @staticmethod
    def __answer_choice(update, context, variants):
        answer = None
        for k, v in variants.items():
            answer = variants[k] if (itm in update.message.text for itm in k) else None
            break
        if answer:
            context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=variants["неизвестно"])
        return "FREE_MESSAGE"

    @staticmethod
    def ask_user_name(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"Приятно познакомиться, {update.message.text}!"
        )
        return "FREE_MESSAGE"

    def ask_user_affairs(self, update, context):
        variants = {
            ("хорошо", "прекрасно", "супер", "великолепно"): "Я рад это слышать!",
            ("плохо", "не очень", "отвратительно", "фигово"): "Не переживай, все наладится!",
            "неизвестно": "Хмм... Странные дела))",
        }
        return self.__answer_choice(update, context, variants)

    def ask_user_mood(self, update, context):
        variants = {
            ("хорошее", "прекрасное", "суперское", "великолепное"): "Круто!",
            ("плохое", "не очень", "отвратительное", "фиговое"): "Все обязательно будет хорошо! Улыбнись!",
            "неизвестно": "Хмм... Мне это не знакомо =(",
        }
        return self.__answer_choice(update, context, variants)

    #     def start(self, update: Update, context: CallbackContext):
    #         update.message.reply_text("Привет! Я бот!\nДля завершения введи команду /stop\nКак твое имя?")
    #         return 1
    #
    #     def help(self, update: Update, context: CallbackContext):
    #         text = f"""Я бот - {update.effective_chat.bot['first_name']}!
    # Нифига не умею, но скоро научусь чему-нибудь хорошему!
    # Начать разговор - /start
    # Закончить разговор - /stop"""
    #         context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    def stop(self, update: Update, context: CallbackContext):
        print(context.user_data)
        update.message.reply_text("Пока!")
        return ConversationHandler.END

    # def unknown_command(self, update: Update, context: CallbackContext):
    #     context.bot.send_message(
    #         chat_id=update.effective_chat.id, text="Я на знаю такой команды 🤨\nПопробуй еще разок!"
    #     )
    # return ConversationHandler.END

    #     def get_name(self, update: Update, context: CallbackContext):
    #         context.user_data["name"] = update.message.text
    #         update.message.reply_text(
    #             f"""Рад познакомиться, {context.user_data["name"]}!
    # Кажется, я знаю твою фамилию... Сказать?!""",
    #             reply_markup=self.keyboard(),
    #         )
    #         return 2

    # def user_last_name(self, update: Update, context: CallbackContext):
    #     text = update.message.text
    #     context.user_data["choice"] = text
    #     if text == "Нет":
    #         update.message.reply_text("Ну как хочешь...", reply_markup=self.keyboard.clear())
    #         return ConversationHandler.END
    #     update.message.reply_text(
    #         f'Твоя фамилия {update.effective_user["last_name"]}!', reply_markup=self.keyboard.clear()
    #     )
    #     return ConversationHandler.END

    # def choice_game_mode(self, update: Update, context: CallbackContext):
    #     context.bot.send_message(chat_id=update.effective_chat.id, text="Выбери режим игры!")

    def __del__(self):
        print(1)


class Greetings:
    def __init__(self):
        self.answers = (
            "Привет!",
            "Здравствуй!",
            "Приветик!",
            "Hello!",
            "Приветствую!",
            "Добрый день!",
        )

    def __call__(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(self.answers))


class Apology:
    def __init__(self):
        self.answers = (
            "Ничего страшного!",
            "Ок, извинения приняты...",
            "Больше так не делай...",
        )

    def __call__(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(self.answers))


class Unknown:
    def __init__(self):
        self.answers = (
            "Не совсем понимаю, о чём ты.",
            "Вот эта последняя фраза мне не ясна.",
            "А вот это не совсем понятно.",
            "Можешь сказать то же самое другими словами?",
            "Вот сейчас я тебя совсем не понимаю.",
            "Попробуй, пожалуйста, выразить свою мысль по-другому.",
        )

    def __call__(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(self.answers))


class Questions:
    def __init__(self):
        self.map = {
            "как": {
                ("дела", "делишки",): lambda: self.bot_affairs,
                ("настроение", "состояние", "чувствуешь",): lambda: self.bot_mood,
                ("имя", "зовут", "звать",): lambda: self.bot_name,
            },
            "что": {("умеешь", "можешь",): lambda: self.bot_abilities},
            "нет ответа": ("Я не знаю ответа на этот вопрос!", "Да х его з!",),
        }

    @staticmethod
    def bot_name(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f'Меня зовут {update.effective_chat.bot["first_name"]}!\nА тебя?'
        )
        return "ASK_USER_NAME"

    @staticmethod
    def bot_abilities(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ничего... Ведь мой создатель лох!")
        return "FREE_MESSAGE"

    @staticmethod
    def bot_mood(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(("Отличное!", "Хорошее!",)))
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(("А у тебя?", "А как твое?",)))
        return "ASK_USER_MOOD"

    @staticmethod
    def bot_affairs(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=random.choice(("Все супер!", "Нормально", "Хорошо!",))
        )
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=random.choice(("А как твои?", "А как у тебя?",))
        )
        return "ASK_USER_AFFAIRS"

    def __call__(self, update, context, phrase):
        words = nltk.word_tokenize(update.message.text)
        first_key = None
        for k in self.map:
            first_key = k if k in words else None
            if first_key:
                break
        if first_key:
            for itm in self.map[first_key]:
                second_key = itm if any(_ in words for _ in itm) else None
                if second_key:
                    break
        try:
            return self.map[first_key][second_key]()(update, context)
        except KeyError:
            context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(self.map["нет ответа"]))

    # if any(tuple(map(lambda x: x.lower() in phrase, self.name))):
    #     return self.bot_name(update, context)
    # try:
    #     context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(self.map[phrase]))
    # except KeyError:
    #     context.bot.send_message(chat_id=update.effective_chat.id, text='Я не знаю ответа на этот вопрос!')
