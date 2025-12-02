from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello,"
    "we're yoooo changes to"
    "our  change!"
    ""
    "L"}