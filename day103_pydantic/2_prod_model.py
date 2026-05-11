from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    in_stock: bool = True # default value

prod1 = {
    "id": 1,
    "name": "Laptop",
    "price": 20000,
    "quantity": 3,
    "in_stock": False
}

prod1 = {
    "id": 1,
    "name": "Laptop",
    "price": 20000,
    "quantity": 3,
    "in_stock": False
}

prod2 = {
    "id": 1,
    "name": "Mobile",
    "price": 10000,
    "quantity": 3,
    "in_stock": True
}
prod = Product(**prod1)
second_prod = Product(**prod2)
print(prod)
print(second_prod)