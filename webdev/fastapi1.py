
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my API!"}

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return {
        "id": movie_id,
        "title": "Inception",
        "year": 2010
    }
