import base64

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from app.util.constants.I18n import ErrMsg
from app.util.constants.Variables import Crypto


class CryptoService:

    @staticmethod
    def encrypt(plain_text: str, secret: str) -> str:
        key = secret.encode(Crypto.UTF_8)
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(128).padder()
        padded = padder.update(plain_text.encode(Crypto.UTF_8)) + padder.finalize()

        encrypted = encryptor.update(padded) + encryptor.finalize()
        return base64.b64encode(encrypted).decode(Crypto.UTF_8)

    @staticmethod
    def decrypt(encrypted_base64: str, secret: str) -> str:
        key = secret.encode(Crypto.UTF_8)
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_padded = decryptor.update(base64.b64decode(encrypted_base64)) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
        return decrypted.decode(Crypto.UTF_8)