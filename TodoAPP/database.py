from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})

# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Base = declarative_base()
# =========================================================================

# SQLite database ka path — './' matlab current folder mein file banega
# 'todosapp.db' → ye actual file hai jahan saara data store hoga
# SQLite ke liye koi alag server nahi chahiye — ek simple file hai
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# Engine → SQLAlchemy ka core connection object
# Ye actual DB se baat karta hai
# connect_args={'check_same_thread': False} → SQLite specific setting hai
# SQLite by default sirf ek thread allow karta hai
# FastAPI multiple threads use karta hai → isliye False karna zaroori hai
engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})

# SessionLocal → DB session banane ki factory hai
# Har request ke liye ek naya session banega isi se
# autocommit=False → har operation automatically save nahi hoga
#                    manually db.commit() karna padega — safer hai
# autoflush=False  → query se pehle automatically flush nahi hoga
# bind=engine      → ye sessions upar banaye engine se connected honge
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base → ye parent class hai jisse saare DB models inherit karenge
# models.py mein 'class Todos(Base)' → iska matlab Todos ek DB table hai
# Base ke andar sab tables ka record hota hai → create_all() isi se kaam karta hai
Base = declarative_base()