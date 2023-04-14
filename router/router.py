from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from schema.user_schema import UserSchema
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash, check_pasword_hash
from typing import List

user = APIRouter()

@user.get("/")
def root ():
    return {"message": "Hi fastapi"}

@user.get("/api/user", response_model=List[UserSchema])
def get_users():
    with engine.connect as conn:
        result = conn.execute(users.select()).fetchall()
        
        return result
    
@user.get ("/api/user/{user_id}", response_model=UserSchema)
def get_user(user_is:str):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.id == user_id)).first()
        return result
        

@user.post("/api/user", status_code= HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    with engine.connect() as conn:
        new_user = data_user.dict()
        new_user["user_passw"] = generate_password_hash(data_user.user_passw,"pbkdf2:sha250:30", 30)
            
        conn.execute(users.insert().values(new_user))

        return Response(status_code=HTTP_201_CREATED)
    
@user.put("/api/user")
def update_user():
    pass
    