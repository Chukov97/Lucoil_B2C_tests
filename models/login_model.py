from pydantic import BaseModel


class LoginData(BaseModel):
    card_number: str
    password: str
