from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

from app.models import User


class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    chat_id: int
    sender_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ChatBase(BaseModel):
    name: str


class ChatCreate(ChatBase):
    pass

class ChatCreateWithEmail(BaseModel):
    chat: ChatCreate
    user_email: EmailStr

class User(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True

class Message(BaseModel):
    id: int
    content: str
    sender_id: int

    class Config:
        orm_mode = True

class Chat(ChatBase):
    id: int
    created_at: datetime
    users: List[User] = []  # Используем полные объекты User
    messages: List[Message] = []  # Используем полные объекты Message

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    chats: List[Chat] = []

    class Config:
        orm_mode = True
