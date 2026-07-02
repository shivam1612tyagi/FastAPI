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
# ====================================================================================================

# Body  → request ke JSON body se data uthane ke liye
# FastAPI → web framework jo hamara server banata hai
from fastapi import Body, FastAPI

# FastAPI ka instance — poora server isi 'app' pe chalega
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
@app.get("/books")
async def read_all_books():
    return BOOKS

# GET /books/{book_title} → title se ek specific book dhundo
# {book_title} → path parameter, URL ka hissa
# Example: /books/title one
@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in BOOKS:
        # casefold() → case-insensitive comparison
        if book.get('title').casefold() == book_title.casefold():
            return book
        
# GET /books/?category=math → query parameter se filter karo
# 'category' URL mein nahi, ? ke baad aata hai
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# GET /books/{book_author}/?category=math
# book_author → path parameter
# category    → query parameter
# Dono ek saath — AND condition se filter
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        # dono conditions ek saath True honi chahiye
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

# POST /books/create_book → nayi book add karo
# Body() → JSON body se data uthao
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    # new_book ek plain dict hai, seedha list mein append
    BOOKS.append(new_book)

# PUT /books/update-book → existing book ko update karo
# PUT isliye kyunki hum koi existing cheez REPLACE kar rahe hain
# POST = nayi cheez banana, PUT = purani cheez badalna
@app.put("/books/update-book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        # index se loop isliye — BOOKS[i] = updated_book karna tha
        # direct 'for book in BOOKS' se reassign nahi ho sakta
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            # title match hua → poori book replace karo updated data se
            BOOKS[i]=updated_book