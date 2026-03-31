from pydantic import BaseModel

class signupValidation(BaseModel):
    username: str
    password: str
    name: str
    email: str

class loginValidation(BaseModel):
    email: str
    password: str

class changePasswordValidation(BaseModel):
    new_password: str
    old_password: str
class changeEmail(BaseModel):
    old_email: str
    new_email: str


