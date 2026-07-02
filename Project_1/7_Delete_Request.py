# from fastapi import Body, FastAPI

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

# @app.get("/books/{book_title}")
# async def read_book_by_title(book_title: str):
#     for book in BOOKS:
#         if book.get('title').casefold() == book_title.casefold():
#             return book
        
# @app.get("/books/")
# async def read_category_by_query(category:str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)
#     return books_to_return


# @app.get("/books/{book_author}/")
# async def read_author_category_by_query(book_author: str, category: str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('author').casefold() == book_author.casefold() and \
#                 book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)

#     return books_to_return

# @app.post("/books/create_book")
# async def create_book(new_book=Body()):
#     BOOKS.append(new_book)

# @app.put("/books/update-book")
# async def update_book(updated_book = Body()):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
#             BOOKS[i]=updated_book

# @app.delete("/books/delete_book/{book_title}")
# async def delete_book(book_title:str):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get('title').casefold() == book_title.casefold():
#             BOOKS.pop(i)
#             break
# =========================================================================================
# Body  → request ke JSON body se data uthane ke liye
# FastAPI → web framework jo hamara server banata hai
from fastapi import Body, FastAPI

# FastAPI ka instance — poora server isi 'app' pe chalega
# uvicorn main:app --reload → isi 'app' ko point karta hai
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
# Koi bhi parameter nahi — seedha sab kuch bhej do
@app.get("/books")
async def read_all_books():
    return BOOKS

# GET /books/{book_title} → title se ek specific book dhundo
# {book_title} → path parameter, URL ka hissa hai
# Example: /books/title one → book_title = "title one"
@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in BOOKS:
        # casefold() → case-insensitive comparison
        # "Title One" aur "title one" dono match ho jayenge
        if book.get('title').casefold() == book_title.casefold():
            return book
        
# GET /books/?category=math → query parameter se filter karo
# 'category' URL mein nahi hai — ? ke baad aata hai
# Example: /books/?category=math
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# GET /books/{book_author}/?category=math
# book_author → path parameter (URL mein {} ke andar)
# category    → query parameter (? ke baad, function mein directly)
# Dono ek saath — AND condition se filter hoga
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        # \ → sirf line todne ke liye, code continue ho raha hai
        # dono conditions ek saath True honi chahiye tabhi append hoga
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

# POST /books/create_book → nayi book BOOKS list mein add karo
# POST isliye → naya data create kar rahe hain
# Body() → FastAPI ko bolta hai: JSON body se data uthao
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    # new_book ek plain Python dict hai
    # seedha BOOKS list mein append ho jaata hai
    BOOKS.append(new_book)

# PUT /books/update-book → existing book ko replace karo
# PUT isliye → purani cheez badal rahe hain, nayi nahi bana rahe
# Body() → updated book ka data JSON body se aayega
@app.put("/books/update-book")
async def update_book(updated_book = Body()):
    # index loop isliye — BOOKS[i] = updated_book karna tha
    # 'for book in BOOKS' se direct reassign nahi ho sakta
    for i in range(len(BOOKS)):
        # title match hua → poori book replace karo
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i]=updated_book

# DELETE /books/delete_book/{book_title} → title se book dhundo aur hatao
# {book_title} → path parameter, URL se aata hai
# Example: /books/delete_book/title one
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            # .pop(i) → index i wali book list se hata do
            BOOKS.pop(i)
            # break → ek baar milne ke baad loop band karo
            # warna pop ke baad index shift ho jaata hai → bug
            break