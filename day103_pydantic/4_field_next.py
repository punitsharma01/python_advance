from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="Employee name",
        examples="Punit Sharma"
    )

    department: Optional[str]
    salary: float = Field(
        ...,
        gt=20000,
        le=1000000,
        description="Salary in USD",

    )
class User(BaseModel):
    email: str = Field(
        ...,
        pattern=f''
    )
    phone: str = Field(..., pattern=f'')