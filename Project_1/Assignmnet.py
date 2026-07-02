# Assignment
# =======================
# Here is your opportunity to keep learning!

# 1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or 
#  Query Parameters.

from fastapi import FastAPI,Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def read_all_book():
    return BOOKS

@app.get("/books/byauthor/{author}")
async def read_books_by_author(author:str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            book_to_return.append(book)

    return book_to_return