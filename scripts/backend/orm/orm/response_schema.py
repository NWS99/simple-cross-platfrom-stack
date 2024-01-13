"""
This Module is used to create the pydantic models for the response schema.
"""

from datetime import datetime
from pydantic import BaseModel


class CreateUser(BaseModel):
    name: str
    age: int
    last_activity: datetime

class User(CreateUser):
    key: int

class CreateMessage(BaseModel):
    body: str
    sender_key: int
    receiver_key: int
    encryption: bool

class Message(BaseModel):
    key: int

