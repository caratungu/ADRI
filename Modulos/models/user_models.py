from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserLogUp(BaseModel):
    username: str
    password: str
    firstname: str
    lastname: str
    email: str
    bornday: int
    bornmonth: int
    bornyear: int

class UserOut(BaseModel):
    username: str
    email: str