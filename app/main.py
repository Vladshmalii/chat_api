from fastapi import FastAPI
from app.database import engine, Base
from app.auth import router as auth_router
from app.chat import router as chat_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(chat_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the chat API!"}
