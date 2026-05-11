from typing import Optional, List
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: int


class Company(BaseModel):
    name: str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None


class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    city: str
    state: State

class Organization(BaseModel):
    name: str
    country: Country
    state: State
    city: City
    headquarters: Address
    branches: List[City] = None
