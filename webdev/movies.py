from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

movies = {
    1: "Inception",
    2: "Inside Out",
    3: "Interstellar"
}

@app.get("/movies/{movie_id}", response_class=HTMLResponse)
def get_movie(movie_id: int):
    if movie_id in movies:
        title = movies[movie_id]
        return f"""
        <html>
            <body>
                <h1>Title: {title}</h1>
            </body>
        </html>
        """
    else:
        return "<h1>Movie not found</h1>"

@app.get("/findmovies", response_class=HTMLResponse)
def search_movie(title: str):
    for movie_id in movies:
        if title == movies[movie_id]:
            return f"<h1>Movie found: {movies[movie_id]}</h1>"

    return "<h1>Movie not found</h1>"

