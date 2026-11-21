from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return({"msg":"Hello world"})

@app.get("/user/{user_id}/expenses")
def user_expenses():
    return