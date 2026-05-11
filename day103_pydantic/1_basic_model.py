from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int
    is_active: bool

user_details = {
    "name": "Punit",
    "id": 2,
    "is_active": True,
}

user = User(**user_details)
print(user)