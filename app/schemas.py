from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    role: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class InvoiceBase(BaseModel):
    total: float

class InvoiceCreate(InvoiceBase):
    user_id: int

class Invoice(InvoiceBase):
    id: int
    user_id: int
    created_at: datetime
    class Config:
        orm_mode = True
