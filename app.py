from flask import Flask, request, jsonify, render_template  # <--- render_template add kiya
import joblib
import re
import os
import warnings
from flask_cors import CORS 

warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)
CORS(app) 

# ==========================================
#  MODEL LOADING
# ==========================================
MODEL_PATH = 'emotion_classifier.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'

model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None
vectorizer = joblib.load(VECTORIZER_PATH) if os.path.exists(VECTORIZER_PATH) else None

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip()

# ==========================================
#  ROUTES
# ==========================================

# 1. BROWSER HOME ROUTE (Ye missing tha)
@app.route('/')
def home():
    return render_template('index.html', prediction=None, emoji=None, original_text=None)

# 2. UI PREDICT ROUTE (Jo index.html ke form se connect hai)
@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form.get('text_input')
    if not user_input or user_input.strip() == "":
        return render_template('index.html', warning="Please enter some text!", prediction=None)

    try:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]

        emojis = {'joy': '😊', 'sadness': '😢', 'anger': '😡', 'fear': '😨', 'love': '❤️', 'surprise': '😲'}
        result_emoji = emojis.get(prediction.lower(), '✨')

        return render_template('index.html', prediction=prediction.upper(), emoji=result_emoji, original_text="")
    except Exception as e:
        return render_template('index.html', warning=str(e), prediction=None)

# 3. API ROUTE (Thunder Client ke liye)
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    user_input = data['text']
    try:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]
        emojis = {'joy': '😊', 'sadness': '😢', 'anger': '😡', 'fear': '😨', 'love': '❤️', 'surprise': '😲'}
        
        return jsonify({
            "status": "success",
            "prediction": prediction.upper(),
            "emoji": emojis.get(prediction.lower(), '✨'),
            "original_text": user_input
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)