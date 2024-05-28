from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def acceuil(min: int = 0, max: int = 10):
    return {"message": "Bonjour et bienvenue"}

@app.get("/nombre")
def nombre(min: int = 0, max: int = 10):
    return {"nombre aléatoire entre {} et {}: {}".format(min, max-1, random.randint(min, max))}

@app.get("/nombre2")
def nombre2(min: int = 10, max: int = 100):
    return {"nombre aléatoire entre {} et {}: {}".format(min, max-1, random.randint(min, max))}
