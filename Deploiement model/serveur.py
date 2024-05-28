from fastapi import FastAPI
import joblib
import pandas as pd

model_path = 'C:/Users/nicoe/Desktop/Deploiement model/model.pkl'
app = FastAPI()
model = joblib.load(model_path)
@app.get("/")
def FirstAPI():
  return "Hello World !"

@app.post("/score")
def score(iris: dict):
  data = pd.json_normalize(iris)
  resultat = model.predict(data)
  print(resultat)
  return resultat[0]