from flask import Flask, request, jsonify
import speech_recognition as sr
import pandas as pd
import joblib
from pymongo import MongoClient
from flask_cors import CORS
import pyttsx3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.ensemble import RandomForestClassifier
import datetime
import time

app = Flask("HEALTHCARE 2.0")
CORS(app)  # Enable CORS for React frontend
model = joblib.load("disease_prediction_model.pkl")

data = pd.read_csv("disease_data.csv")  # Load dataset containing symptoms, diseases, causes, precautions, and treatment

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_db"]
collection = db["patient_records"]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def predict_disease(symptoms):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['Symptoms'])
    query_vector = tfidf.transform([symptoms])
    cosine_sim = cosine_similarity(query_vector, tfidf_matrix)
    
    most_similar_symptom = cosine_sim.argsort()[0][-1]
    disease_info = data.iloc[most_similar_symptom]
    return disease_info

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please state your symptoms.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        symptoms = recognizer.recognize_google(audio)
        return symptoms
    except sr.UnknownValueError:
        return "Error: Could not understand audio."
    except sr.RequestError:
        return "Error: Could not connect to speech service."

@app.route("/predict", methods=["POST"])
def predict():
    symptoms = request.json.get("symptoms")
    if not symptoms:
        return jsonify({"error": "No symptoms provided"})
    
    disease_info = predict_disease(symptoms)
    result = {
        "Disease": disease_info['Disease'],
        "Causes": disease_info['Causes'],
        "Precautions": disease_info['Precautions'],
        "Treatment": disease_info['Treatment']
    }
    
    collection.insert_one({"symptoms": symptoms, "predicted_disease": result})
    return jsonify(result)

@app.route("/voice", methods=["GET"])
def voice():
    symptoms = get_voice_input()
    if "Error" in symptoms:
        return jsonify({"error": symptoms})
    
    disease_info = predict_disease(symptoms)
    result = {
        "Disease": disease_info['Disease'],
        "Causes": disease_info['Causes'],
        "Precautions": disease_info['Precautions'],
        "Treatment": disease_info['Treatment']
    }
    
    collection.insert_one({"symptoms": symptoms, "predicted_disease": result})
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
