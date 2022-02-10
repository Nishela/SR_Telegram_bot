from source import Greetings, Apology, Unknown, Questions
import nltk
from nltk.corpus import stopwords

all = ("Router",)
stop_words = nltk.corpus


class Router:
    def __init__(self):
        self.stopwords = stopwords.words("russian")
        self.routing_map = {
            ("привет", "приветик", "hello", "hi", "здарова"): Greetings,
            ("прости", "извини"): Apology,
            "unknown": Unknown,
            "?": Questions,
        }

    def parse_data(self, update, context):
        sent = nltk.sent_tokenize(update.message.text.lower())
        for phrase in sent:
            if "?" in phrase:
                return self.routing_map["?"]()(update, context, phrase)
            try:
                for k, v in self.routing_map.items():
                    if any(itm in phrase for itm in k):
                        return self.routing_map[k]()(update, context)
            except KeyError:
                pass
            return self.routing_map["unknown"]()(update, context)

    def __call__(self, update, context):
        return self.parse_data(update, context)
