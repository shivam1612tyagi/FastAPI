# from fastapi import FastAPI

# app = FastAPI()

# BOOKS = [
#     {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
#     {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
#     {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
#     {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
#     {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
#     {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
# ]

# @app.get("/books")
# async def read_all_books():
#     return BOOKS
#===========================================================================================
from fastapi import FastAPI

app = FastAPI()

# Ye hamara "database" hai abhi ke liye
# Real app mein ye kisi actual DB (PostgreSQL, MongoDB) se aata

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# GET /books → saari books return karo
# Jab koi browser ya code "GET http://localhost:8000/books" karega
# toh poori BOOKS list JSON mein milegi
@app.get("/books")
async def read_all_books():
    return BOOKS  # FastAPI list ko bhi automatically JSON array bana deta hai