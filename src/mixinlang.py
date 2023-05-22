class MixinLang:
    language = "EN"
    def __init__(self):
        self.language = self.language

    # def change_lang(self):
    #     if self.language == "EN":
    #         self.language = "RU"
    #         return self.language
    #     elif self.language == "RU":
    #         self.language = "EN"
    #         return self.language
    #     else:
    #         raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
            return self
        elif self.language == "RU":
            self.language = "EN"
            return self
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")