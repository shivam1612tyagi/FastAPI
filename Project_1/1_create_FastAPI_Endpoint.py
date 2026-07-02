# FastAPI library se FastAPI class import kar rahe hain
# Yahi class hamara poora web server banati hai
from fastapi import FastAPI

# FastAPI ka ek instance bana rahe hain
# 'app' variable hi hamara actual server hai
# jab uvicorn chalate hain toh isi 'app' ko point karta hai
app = FastAPI()

# '@app.get("/")' ek decorator hai
# Matlab: jab koi browser/code GET request karega "/" pe (root URL pe)
# toh neeche wala function chalega
#
# 'async def' matlab ye function asynchronous hai —
# dusre requests rok ke nahi rakhega jab ye chal raha ho
@app.get("/")
async def frist_api():
    # Jo bhi dictionary return karo, FastAPI automatically
    # usse JSON mein convert kar deta hai
    # {"message": "Hello Shivam!"} → client ko milega JSON response
    return {
        "message": "Hello Shivam!"
    }