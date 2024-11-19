from fastapi import APIRouter, Request


auth = APIRouter(prefix="/auth", tags=["auth"])


@auth.get("/", tags=["prod", "cringe", "qwerty"])
def index_(request: Request):
    return {"headers": request.headers}


@auth.get("/login")
def login_():
    return {"msg": "Login not required for now!"}
