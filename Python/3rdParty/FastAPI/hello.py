from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    """This is my hello-world end-point."""
    return { "message": "Hello, world!" }
