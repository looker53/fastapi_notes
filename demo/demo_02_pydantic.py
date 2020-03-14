"""pydantic 的用法"""
from typing import List
from pydantic import BaseModel


class User(BaseModel):
    name:str = 'default'
    age: int
    hobby: List[str]


http_data = {
    "name": "yuz", 
    "age": "abc", 
    "hobby": ["piano", "列侬", 3]
}

user = User(**http_data)
print(user)


