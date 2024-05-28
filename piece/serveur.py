from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

app = FastAPI()

class PredictionInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model.pkl")

@app.post("/predict")
async def predict(input: PredictionInput):
    # Transformer l'input en un tableau NumPy 2D
    input_data = np.array([[input.sepal_length, input.sepal_width, input.petal_length, input.petal_width]])
    prediction = model.predict(input_data)
    return {"type": str(prediction[0])}
