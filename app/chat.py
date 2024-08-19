from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from pydantic import EmailStr

from app import models, schemas
from app.database import get_db


router = APIRouter(prefix="/chats",
                   tags=["chats"],)


@router.post("/chats/", response_model=schemas.Chat)
def create_chat(
        name: str = Query(..., description="Chat name"),
        user_emails: List[EmailStr] = Query(..., description="User emails"),
        db: Session = Depends(get_db)
):
    # Поиск пользователей по email
    db_users = db.query(models.User).filter(models.User.email.in_(user_emails)).all()

    if len(db_users) != len(user_emails):
        raise HTTPException(status_code=404, detail="One or more users not found")

    db_chat = models.Chat(name=name)
    db_chat.users = db_users
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


@router.get("/chats/{chat_id}", response_model=schemas.Chat)
def get_chat(chat_id: int, db: Session = Depends(get_db)):
    db_chat = db.query(models.Chat).filter(models.Chat.id == chat_id).first()
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat


@router.get("/users/{user_id}/chats/", response_model=List[schemas.Chat])
def get_user_chats(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user.chats


@router.get("/chats/{chat_id}/messages/{message_id}", response_model=schemas.Message)
def get_message(chat_id: int, message_id: int, db: Session = Depends(get_db)):
    db_message = db.query(models.Message).filter(
        models.Message.chat_id == chat_id,
        models.Message.id == message_id
    ).first()
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message


@router.post("/chats/{chat_id}/messages/", response_model=schemas.Message)
def create_message(chat_id: int, message: schemas.MessageCreate, sender_id: int, db: Session = Depends(get_db)):
    db_chat = db.query(models.Chat).filter(models.Chat.id == chat_id).first()
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    db_sender = db.query(models.User).filter(models.User.id == sender_id).first()
    if db_sender is None:
        raise HTTPException(status_code=404, detail="Sender not found")

    db_message = models.Message(content=message.content, chat_id=chat_id, sender_id=sender_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
