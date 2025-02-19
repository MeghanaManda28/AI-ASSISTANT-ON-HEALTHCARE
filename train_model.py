import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset (Make sure "disease_data.csv" exists in your project folder)
data = pd.read_csv("disease_data.csv")

# Check if required columns exist
required_columns = {'Symptoms', 'Disease'}
if not required_columns.issubset(data.columns):
    raise ValueError("Dataset must contain 'Symptoms' and 'Disease' columns")

# Feature extraction using TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
X = tfidf_vectorizer.fit_transform(data['Symptoms'])
y = data['Disease']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the machine learning model (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and vectorizer
joblib.dump(model, "disease_prediction_model.pkl")
joblib.dump(tfidf_vectorizer, "tfidf_vectorizer.pkl")

print("Model training complete. Files saved as 'disease_prediction_model.pkl' and 'tfidf_vectorizer.pkl'.")
