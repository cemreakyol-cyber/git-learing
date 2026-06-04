from fastapi import FastAPI
import jwt

app = FastAPI()

SECRET_KEY = "gizli_anahtar"

@app.get("/")
def home():
    return {"message": "Merhaba JWT"}

@app.get("/token")
def create_token():
    token = jwt.encode(
        {"username": "cemre"},
        SECRET_KEY,
        algorithm="HS256"
    )

    return {"token": token}