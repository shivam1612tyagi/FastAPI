from fastapi import FastAPI, APIRouter

#app = FastAPI()
router = APIRouter()

# @app.get("/auth")
# async def get_user():
#     return {'user':'authenticated'}

router = APIRouter()

@router.get("/auth/")
async def get_user():
    return {'user':'authenticated'}