import os


from bcrypt import hashpw,checkpw,gensalt
from dotenv import load_dotenv
load_dotenv()
SALT="salt"

class passwordService:


    @staticmethod
    def createPassword(plainPassword: str) -> bytes:
        salt = gensalt()  # generate valid salt
        return  hashpw(plainPassword.encode('utf-8'), salt)

    @staticmethod
    def verifyPassword(plainPassword: str, hashedPassword: str) -> bool:
        return checkpw(plainPassword.encode('utf-8'), hashedPassword.encode('utf-8'))



PasswordService = passwordService()