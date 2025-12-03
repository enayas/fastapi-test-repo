from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello,"
    "we're   to"
    "our 2 !"
    ""
    "L"}