from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import os
from pydantic import BaseModel 

# Utilisation d'une variable d'environnement pour le chemin du modèle ou un chemin par défaut
chemin = "C:/Users/nicoe/Desktop/deploiement_model_python/deploiement4"
model_path = os.getenv(chemin, "model.pkl")


app = FastAPI()


class iris_format(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    

model = joblib.load(model_path)

@app.get("/")
def first_api():
    return {"message": "Hello World!"}

@app.post("/score")
def score(iris: iris_format):
    try:
        data = pd.json_normalize(iris.model_dump())
        resultat = model.predict(data)
        return {"prediction": resultat[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors de la prédiction: {str(e)}")
