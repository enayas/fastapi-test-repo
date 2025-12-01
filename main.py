from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello wrld!!! We are gdotta go!!! We need to see the stars!!!"}