from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "Ado Bokkay! Mage AI App eka weda!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello from BuildXAI!"}
    