
class Crypto:
    UTF_8 = "utf-8"
    AES = "AES"

class Env:
    CRYPTO_ALGORITHM = "CRYPTO_ALGORITHM"
    SPRING_TMAKES_COM_SEC = "SPRING_TMAKES_COM_SEC"
    SPRING_TMAKES_COM_MSG = "SPRING_TMAKES_COM_MSG"
    SPRING_TMAKES_HOST = "SPRING_TMAKES_HOST"

class App:
    MIDDLEWARE_HTTP = 'http'

class Api:
    HEADER_X_API_KEY = "X-API-KEY"
    METHOD_OPTIONS = "OPTIONS"
    API_PRIVATE_PREFIX = "/api/private"
    API_TASK_USER = "/task-user-pred"

class Locale:
    DEFAULT_LANG = "en"

    @classmethod
    def get_file(cls, locale: str):
        return f"app/storage/i18n/msg_err_{locale}.json"
