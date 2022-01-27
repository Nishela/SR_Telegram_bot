all = "Some_base_handler2"


class Some_base_handler2:
    def __init__(self, callback):
        self.callback = callback

    # def __call__(self, update: Update, context: CallbackContext, *args, **kwargs):
    #     print(1)
    #     result = self.callback(update, context)
    #     print(1)
    #     return result

    def __del__(self):
        print(1)
