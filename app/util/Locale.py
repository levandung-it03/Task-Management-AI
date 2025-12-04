
import json
import os

from app.util.constants.Variables import Locale, Env


class I18n:
    _messages = {}

    @classmethod
    def load(cls, locale: str):
        path = Locale.get_file(locale)
        if not os.path.exists(path):
            path = Locale.get_file(Locale.DEFAULT_LANG)
        with open(path, encoding=Env.UTF_8) as f:
            cls._messages[locale] = json.load(f)
        return cls._messages[locale]

    @classmethod
    def get(cls, key: str, locale: str = Locale.DEFAULT_LANG) -> str:
        if locale not in cls._messages:
            cls.load(locale)
        return cls._messages[locale].get(key, key)
