import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from utils import extract_features

# Load dataset
data = pd.read_csv("phishing.csv")

# Feature extraction
data["features"] = data["url"].apply(lambda x: extract_features(x))
X = pd.DataFrame(data["features"].tolist())
y = data["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ✅ ADD ACCURACY HERE
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")