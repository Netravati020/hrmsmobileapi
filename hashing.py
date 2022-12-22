import base64

from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

from cryptography.fernet import Fernet
# class Hash():
#     def bcrypt(password: str):
#         return pwd_cxt.hash(password)
#
#     def verify(hashed_password,plain_password):
#         return pwd_cxt.verify(plain_password,hashed_password)

# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():

    def encrypt(password):
        pa= password.encode()
        encryptor= base64.b64encode(pa)
        return encryptor

# from cryptography.fernet import Fernet
# class Hashh():
#     def decrypt(pa):
#         key = Fernet.generate_key()
#         f = Fernet(key)
#         decrypt = f.decrypt(pa).decode()
#         print(decrypt)
#         return decrypt
#         # f.decrypt(password)
