from fastapi import FastAPI
import random

app = FastAPI()





@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/teste")
def funcao_teste():
    return {"Teste": True, "numero-aleatorio": random.randint(1, 10)}

