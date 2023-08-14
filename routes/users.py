from fastapi import APIRouter
from models.user import User 
from config.db import conn 

from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter() 

@user.get('/')
async def find_all_users():
    return serializeList(conn.Test.user.find())



@user.post('/')
async def create_user(user: User):
    conn.Test.user.insert_one(dict(user))
    return serializeList(conn.save.user.find())

@user.put('/{id}')
async def update_user(id,user: User):
    conn.Test.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(conn.Test.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,user: User):
    return serializeDict(conn.Test.user.find_one_and_delete({"_id":ObjectId(id)}))