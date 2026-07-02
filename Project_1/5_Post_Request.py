# Body  → request ke JSON body se data uthane ke liye
# FastAPI → web framework jo hamara server banata hai
from fastapi import Body, FastAPI

# FastAPI ka instance — poora server isi 'app' pe chalega
# uvicorn bhi isi ko point karta hai: uvicorn main:app --reload
app = FastAPI()

# Temporary in-memory database — real app mein ye PostgreSQL/MongoDB hoga
# Har server restart pe ye reset ho jaata hai
BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# GET /books → poori BOOKS list return karo
# Koi parameter nahi — seedha sab kuch bhej do
@app.get("/books")
async def read_all_books():
    return BOOKS

# GET /books/{book_title} → URL se title uthao, match karo, return karo
# {book_title} path parameter hai — URL ka hissa hai
# Example: /books/title one → book_title = "title one"
@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in BOOKS:
        # casefold() → case-insensitive comparison
        # "Title One" aur "title one" dono match ho jayenge
        if book.get('title').casefold() == book_title.casefold():
            return book

# GET /books/?category=math → query parameter se filter karo
# 'category' path mein nahi hai — ? ke baad aata hai URL mein
# Example: /books/?category=math
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# GET /books/{book_author}/?category=math
# book_author → path parameter  (URL mein {} ke andar)
# category    → query parameter (? ke baad, function mein directly)
# Dono ek saath use ho rahe hain — AND condition se filter
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        # \ → line break hai sirf, code continue ho raha hai neeche
        # dono conditions True honi chahiye tabhi book add hogi
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

# POST /books/create_book → nayi book add karo BOOKS list mein
# POST isliye kyunki hum data bhej rahe hain server ko
# Body() → FastAPI ko bolta hai: JSON body se data uthao
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    # new_book ek plain Python dict hai
    # directly BOOKS list mein append ho jaata hai
    BOOKS.append(new_book)