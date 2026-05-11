from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: int


class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123 something",
    city="New delhi",
    postal_code=12345,
)

user = User(
    id=1,
    name="Rohan",
    address=address,
)

raju ={
    "id":2,
    "name":"Raju",
    "address": {"street": "4365 other", "city": "Vns", "postal_code":60002}
}
print(user)

raju = User(**raju)
print(raju)