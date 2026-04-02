from fastapi import FastAPI
from pydantic import BaseModel
import pickle

from src.preprocess import preprocess_text

# Load model & vectorizer
model = pickle.load(open("model/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("model/tfidf_vectorizer.pkl", "rb"))

app = FastAPI(title="Spam Classifier API")

# Request schema
class Message(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Spam Classifier API is running"}

@app.post("/predict")
def predict(data: Message):
    clean_text = preprocess_text(data.message)
    vector = vectorizer.transform([clean_text])
    
    prediction = model.predict(vector)[0]
    prob = model.predict_proba(vector)[0][1]
    
    result = "Spam" if prediction == 1 else "Ham"
    
    return {
        "prediction": result,
        "probability": float(prob)
    }