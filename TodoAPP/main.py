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
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
