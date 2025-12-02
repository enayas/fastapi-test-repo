from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello,"
    "we're  changes to"
    "our 2 !"
    ""
    "L"}