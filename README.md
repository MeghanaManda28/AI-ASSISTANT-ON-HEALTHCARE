AI-ASSISTANT-ON-HEALTHCARE

AI is transforming healthcare by enhancing diagnosis, treatment and patient management using Machine Learning (ML) and Natural Language Processing (NLP).

🚀 Features
Disease Prediction: Uses ML to analyze symptoms and predict diseases.
NLP Processing: Matches user symptoms with the dataset for better accuracy.
Speech Recognition: Accepts voice input for a hands-free experience.
Text-to-Speech (TTS): Reads out the diagnosis results.
Database Storage: Stores patient records in MongoDB.
Web-Based Interface: Built with Flask for backend API and React for frontend.

🛠️ Tech Stack
Backend: Python, Flask, Scikit-learn, Joblib, Pandas
Frontend: React.js
Speech Processing: SpeechRecognition, Pyttsx3
Database: MongoDB
Deployment: Gunicorn, Docker (Optional)

📂 Project Structure

AI-Healthcare-Assistant/
│── backend/
│   ├── app.py  # Flask API
│   ├── disease_prediction_model.pkl  # Trained ML model
│   ├── requirements.txt  # Dependencies
│── frontend/
│   ├── src/
│   │   ├── App.js  # Main React App
│   │   ├── components/
│── dataset/
│   ├── disease_data.csv  # Medical dataset
│── venv/  # Virtual environment
│── README.md

📌 Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/your-repo/AI-Healthcare-Assistant.git
cd AI-Healthcare-Assistant

2️⃣ Backend Setup (Flask API)
Create Virtual Environment & Install Dependencies

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Run Flask Server
python app.py

3️⃣ Frontend Setup (React)
cd frontend
npm install
npm start

🚀 Deployment (Gunicorn & Nginx)

Run Backend with Gunicorn

gunicorn -w 4 -b 0.0.0.0:5000 app:app
Docker Deployment (Optional)

Build Docker Image
docker build -t healthcare-assistant .

Run Container
docker run -p 5000:5000 healthcare-assistant

🔍 API Endpoints
/predict
POST
Takes symptoms as input and returns disease diagnosis
/voice
GET
Accepts symptoms via voice input

🏥 Future Enhancements
-Integrate a deep learning model for improved accuracy.
-Add chatbot functionality for interactive diagnosis.
-Implement cloud-based database storage.

Made by [ MEGHANA MANDA ✨]


