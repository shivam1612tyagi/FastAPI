# #create a database connections for API

# from typing import Annotated

# from fastapi import FastAPI,Depends
# import models
# from models import Todos
# from database import engine, SessionLocal
# from sqlalchemy.orm import Session


# app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# db_dependency = Annotated[Session, Depends(get_db)]

# @app.get("/")
# async def read_all(db:db_dependency):
#     return db.query(Todos).all()
# @app.get("/todo/{todo_id}")
# async def read_todo(db:db_dependency,todo_id:int):
#     todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
#     if todo_model is not None:
#         return todo_model
#     raise HTTPException(status_code=404,detail='Todo not found.')
# ============================================================================

# create a database connections for API

# Annotated → type hints mein extra metadata add karne ke liye
# FastAPI, Depends → web framework aur dependency injection ke liye
from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status
import models                              # hamara models.py file — DB tables define hain wahan
from models import Todos                   # Todos table ka class import karo
from database import engine, SessionLocal  # engine → DB connection, SessionLocal → DB session factory

from sqlalchemy.orm import Session         # SQLAlchemy ka Session type — DB queries isi se hongi

app = FastAPI()

# Ye line DB mein actual tables banati hai
# models.py mein jo bhi Base se inherit kiya hai (jaise Todos)
# unke liye physical tables create ho jaati hain — agar pehle se hain toh kuch nahi hota
models.Base.metadata.create_all(bind=engine)

# Ye function ek DB session deta hai — aur kaam khatam hone pe band kar deta hai
# 'yield' → FastAPI ko bolta hai: "pehle session do, route khatam hone ke baad finally chalao"
# finally → chahe error aaye ya na aaye, session hamesha close hoga — memory leak nahi hoga
def get_db():
    db = SessionLocal()  # naya DB session banao
    try:
        yield db          # ye session route function ko de do
    finally:
        db.close()        # request khatam → session band karo

# Dependency Injection ka shortcut — har route mein baar baar likhne ki zaroorat nahi
# Annotated[Session, Depends(get_db)] matlab:
# "ye Session type ka hai, aur isko get_db() function se automatically provide karo"
db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title:str = Field(min_length=3)
    description:str = Field(min_length=3,max_length=100)
    priority:int = Field(gt=0,lt=6)
    complete:bool

# GET / → Todos table ki saari rows return karo
# db: db_dependency → FastAPI automatically get_db() chalayega
# aur session is function mein inject kar dega — khud kuch nahi karna
@app.get("/")
async def read_all(db: db_dependency):
    # db.query(Todos) → "SELECT * FROM todos" jaisa hai
    # .all()          → saare results ek list mein return karo
    return db.query(Todos).all()

# GET /todo/{todo_id} → ek specific todo dhundo ID se
# todo_id → path parameter, int type → FastAPI validate karega automatically
@app.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int=Path(gt=0)):
    # .filter() → "WHERE id = todo_id" ke barabar
    # .first()  → pehli matching row do, ya None agar koi nahi mila
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    # None nahi hai → todo mila → return karo
    if todo_model is not None:
        return todo_model

    # Todo nahi mila → 404 error bhejo
    # HTTPException → client ko proper error milega, blank response nahi
    raise HTTPException(status_code=404, detail='Todo not found.')


@app.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency, todo_request:TodoRequest):
    todo_model = Todos(**todo_request.dict())
    db.add(todo_model)
    db.commit()

@app.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency, todo_request:TodoRequest, todo_id: int=Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=400,detail="Todo not found")
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@app.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found.')
    db.query(Todos).filter(Todos.id == todo_id).delete()

    db.commit()