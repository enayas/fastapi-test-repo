from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello,"
    "we're making changes to"
    "our hefgej change!"
    ""
    "L"}