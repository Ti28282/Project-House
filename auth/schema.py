from pydantic import BaseModel, Field, root_validator, Extra
import re


class UserSchema(BaseModel):
    login: str  = Field(min_length = 4, max_length = 30)
    password: str =  Field(min_length = 6, max_length = 64)

    class Config:
        extra = Extra.forbid
    #todo validation check

    @root_validator(pre=True)
    def check_for_spaces(cls, values):
        login = values.get("login")
        password = values.get("password")

        if " " in login or login != login.strip():
            raise ValueError("The login must not contain spaces")

        if " " in password or password != password.strip():
            raise ValueError("The password must not contain spaces")

        
        if not re.fullmatch(r"[A-Za-z]+",login):
            raise ValueError("The login must contain only Latin letters")

        if not re.fullmatch(r"[A-Za-z0-9]+", password):
            raise ValueError("The password must contain only Latin letters and numbers")
        
        return values