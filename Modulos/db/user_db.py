from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    firstname: str
    lastname: str
    email: str
    bornday: int
    bornmonth: int
    bornyear: int
    

database_users = Dict[str, UserInDB]

database_users = {
    "JuanC": UserInDB(**{"username":"JuanC",
                            "password":"rootJuanC",
                            "firstname":"Juan",
                            "lastname":"Calderon",
                            "email":"juan.calderon512@gmail.com",
                            "bornday":1,
                            "bornmonth":1,
                            "bornyear":1995}),
    "DiegoP": UserInDB(**{"username":"DiegoP",
                            "password":"rootDiegoP",
                            "firstname":"Diego",
                            "lastname":"Pabon",
                            "email":"pabonariasdiego@hotmail.com",
                            "bornday":1,
                            "bornmonth":1,
                            "bornyear":1995}),
    "JuanR": UserInDB(**{"username":"JuanR",
                            "password":"rootJuanR",
                            "firstname":"Juan",
                            "lastname":"Rico",
                            "email":"u1401101@unimilitar.edu.co",
                            "bornday":1,
                            "bornmonth":1,
                            "bornyear":1995}),
    "FernandoS": UserInDB(**{"username":"FernandoS",
                            "password":"rootFernandoS",
                            "firstname":"Fernando",
                            "lastname":"Serrano",
                            "email":"fercho403@gmail.com",
                            "bornday":1,
                            "bornmonth":1,
                            "bornyear":1995}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db