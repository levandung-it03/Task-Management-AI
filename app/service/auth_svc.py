import os

from dotenv import load_dotenv

from app.util.Crypto import CryptoService
from app.util.constants.Variables import Env, Crypto

load_dotenv()

class TmakesSpringAuthSvc:
    SECRET = str(os.getenv(Env.SPRING_TMAKES_COM_SEC))
    MESSAGE = str(os.getenv(Env.SPRING_TMAKES_COM_MSG))

    @classmethod
    def is_valid_authzed_api_key(cls, key: str) -> bool:
        sent_msg = CryptoService.decrypt(key, cls.SECRET)
        return sent_msg == cls.MESSAGE

    @classmethod
    def generate_authzed_api_key(cls) -> str:
        return CryptoService.encrypt(cls.MESSAGE, cls.SECRET)