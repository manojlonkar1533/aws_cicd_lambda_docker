from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    location_score: float

def predict_price(area, bedrooms, bathrooms, location_score):
    price = (
        area * 3000 +
        bedrooms * 50000 +
        bathrooms * 30000 +
        location_score * 100000
    )
    return round(price, 2)

@app.get("/", response_class=HTMLResponse) 
def home():
    with open("index.html") as f:           # ← serve HTML file
        return f.read()

@app.get("/health")                         # ← separate health check
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: HouseFeatures):
    price = predict_price(
        data.area, data.bedrooms,
        data.bathrooms, data.location_score
    )
    return {"predicted_price": price, "currency": "INR"}