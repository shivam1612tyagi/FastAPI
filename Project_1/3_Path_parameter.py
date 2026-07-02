from fastapi import FastAPI

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
async def read_all_books():
    return BOOKS

#==============================================
# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param):
#     return {
#         'dynamic_param':dynamic_param
#     }
#===============================================

# ==============================================
# @app.get("/books/{book_title}")
# async def read_book_by_title(book_title: str):
#     return {
#         'dynamic_param':book_title
#     }
# ================================================

#=================================================
# @app.get("/books/{book_title}")
# async def read_book_by_title(book_title: str):
#     for book in BOOKS:
#         if book.get('title').casefold() == book_title.casefold():
#             return book
# ==================================================

# {book_title} → ye "path parameter" hai
# Matlab URL ka ek hissa variable ban jaata hai
# Example: GET /books/title one → book_title = "title one"
@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    # FastAPI automatically URL se "book_title" uthata hai
    # aur function ke parameter mein daal deta hai
    # str → FastAPI validate karega ki ye text hi hai

    for book in BOOKS:
        # book.get('title') → dictionary se 'title' ki value nikaal
        # .casefold()      → dono ko lowercase kar — case-insensitive comparison
        # "Title One" == "title one" → normally False
        # "title one" == "title one" → casefold ke baad True ✓
        if book.get('title').casefold() == book_title.casefold():
            return book  # match milte hi book return karo, loop ruk jaata hai

    