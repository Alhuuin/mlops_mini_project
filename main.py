from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("regression.joblib")

app = FastAPI()

class HouseInput(BaseModel):
    size: float
    bedrooms: int
    garden: int

@app.post("/predict")
def predict_price(house: HouseInput):
    data = [[house.size, house.bedrooms, house.garden]]
    prediction = model.predict(data)
    return {"predicted_price": round(prediction[0], 2)}

