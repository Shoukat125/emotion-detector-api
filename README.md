<div align="center">
  <a href="https://emotion-detector-app-steel.vercel.app/">
    <img src="https://img.shields.io/badge/Vercel-Live%20App-000000?style=for-the-badge&logo=vercel" alt="Live App">
  </a>
  <a href="https://github.com/Shoukat125/emotion-detector-api/issues/1">
    <img src="https://img.shields.io/badge/▶️_Watch-Technical_Demo-blue?style=for-the-badge&logo=github" alt="Demo Video">
  </a>
</div>
**AI Emotion Detector: Sentiment Analysis & Linguistic Insights**

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3408/3408545.png" width="120">
  <h1>NLP Emotion Recognition System</h1>
  <p><b>Machine Learning (SVC) + Real-time Flask API</b></p>
</div>

---


## 📌 Executive Summary
This project presents an advanced **Natural Language Processing (NLP)** solution to detect human emotions from textual data. The primary objective was to engineer a system that can understand the emotional tone of a sentence—ranging from **Joy and Love to Anger and Fear**—providing a bridge between human expression and machine intelligence.

### 🛠️ Key Strategic Findings
* **Linguistic Accuracy:** The system utilizes a Support Vector Classifier (SVC) to achieve high-precision classification across multiple emotion categories.
* **Responsive Architecture:** Engineered with a mobile-first approach, ensuring the UI remains functional and clear in **Portrait Mode** across all devices.
* **API Integration:** Ready for cross-platform deployment, allowing mobile applications to consume predictions via structured JSON responses.

---

## 🧠 Machine Learning Architecture

### A. Operational Layer: Support Vector Classifier (SVC)
Unlike basic keyword matching, this layer analyzes the semantic structure of sentences.
* **Technicality:** Employs advanced vectorization to map words into a high-dimensional space, drawing clear boundaries between complex emotions.

* **Significance:** Proven to be highly effective for text classification where the relationship between words is non-linear.

### B. Strategic Layer: Real-time Flask API
To ensure the model is accessible to end-users, we implemented a robust Flask backend.
* **Logic:** The system handles concurrent requests, processing raw text through a pre-trained pipeline before rendering dynamic HTML/JSON.
* **UI/UX Optimization:** Utilizes CSS Media Queries and versioning (`?v=3.0`) to force-update styles and maintain a seamless layout on small screens.


---

## 📊 Technical Specifications & Data Engineering
* **Preprocessing:** Applied tokenization and stop-word removal to clean textual noise.
* **UI Framework:** Custom-built Flexbox/Block layout for maximum responsiveness.
* **Performance Metrics:**
    * **Model Precision:** Optimized for high-variance linguistic patterns.
    * **Latency:** Sub-100ms response time for real-time analysis.

## 📂 Repository Breakdown
* `app.py`: Main Flask application handling routing and model inference.
* `static/style.css`: Premium responsive design with `!important` mobile overrides.
* `templates/index.html`: Clean, intuitive user interface.
* `model.pkl`: Serialized Machine Learning model for instant loading.

## 🏁 Final Conclusion
The project confirms that while text can be ambiguous, **Vector-based Machine Learning** can accurately decipher intent. This API serves as a foundation for sentiment-aware chatbots, customer feedback systems, and mental health monitoring tools.

---

**Developed by Shoukat Ali** | *Transforming Textual Data into Emotional Intelligence.*
