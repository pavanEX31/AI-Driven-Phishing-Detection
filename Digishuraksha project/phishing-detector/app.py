from flask import Flask, render_template, request
import joblib
from utils import extract_features

app = Flask(__name__)

# Load model once
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        url = request.form.get("url")

        if url:
            features = extract_features(url)
            result = model.predict([list(features.values())])[0]
            prediction = "⚠️ Phishing Website" if result == 1 else "✅ Legitimate Website"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)