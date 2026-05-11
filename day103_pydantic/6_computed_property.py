from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

class Booking(BaseModel):
    user_id: int
    room_number: int
    nights: int = Field(..., gt=0)
    price_per_night: float = Field(...)

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price_per_night * self.nights

booking = Booking(
    user_id=123,
    room_number=456,
    nights=3,
    price_per_night=2000,
)

print(booking.total_price)

print(booking.model_dump())