from pydantic import BaseModel, field_validator, model_validator, ValidationError
from datetime import datetime


class Employee(BaseModel):
    employee_id: int
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def is_name_capitalised(cls, v):
        return v.capitalize()


class User(BaseModel):
    employee_id: int
    email: str

    @field_validator('email')
    def normalise(cls, v):
        return v.lower().strip()


class Product(BaseModel):
    name: str # $4.40
    price: str
    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_date(self):
        if self.start_date >= self.end_date:
            raise ValidationError('Start date must be before end date')
        return self

duration = DateRange(
    start_date=datetime(year=2020, month=1, day=1),
    end_date=datetime(year=2024, month=1, day=1),
)
duration_2 = DateRange(
    start_date=datetime(year=2021, month=1, day=1),
    end_date=datetime(year=2019, month=1, day=1),
)

print(duration)
print(duration_2)