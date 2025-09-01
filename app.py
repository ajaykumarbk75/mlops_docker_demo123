# app.py - creating FastAPi app for Model inference 
from fastapi import FastAPI, HTTPException, Depends 
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.security import OAuth2PasswordBearer

#Load the trained model
model = joblib.load("iris_model.pkl")

# OAuth2 Security Setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title = "Iris_model API",
    description="A FastAPI app to serve ML model predictions with OAuth2 Security",
    version="1.0.0"
)
#Input Schema 
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

#Fake token verification - demo purpose
def fake_verify_token(token: str = Depends(oauth2_scheme)):
    if token != "mysecrettoken":
        raise HTTPException(status_code=401, detail="invalid or missing token")
    return token
@app.get("/")
def home():
    return {"message": "Welcome to Iris Model API"}

@app.post("/predict")
def predict(data: IrisInput, token: str = Depends(fake_verify_token)):
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}