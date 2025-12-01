from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world!!! We are gotta go!!! We need to see the stars!!!"}