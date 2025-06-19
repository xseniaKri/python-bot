from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_index():
    return {
        'message': 'Hello, bro!',
    }