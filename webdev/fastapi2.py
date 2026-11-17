from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Welcome to my webpage!</h1>"

@app.get("/movie", response_class=HTMLResponse)
def get_movie():
    return """
    <html>
        <body>
            <h1>Movie Information</h1>
            <p>Title: Inception</p>
            <p>Year: 2010</p>
        </body>
    </html>
    """