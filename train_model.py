import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
print("Loading data...")
df = pd.read_csv("heart_2020_cleaned.csv")

print("\nConverting data...")

df["HeartDisease"] = df["HeartDisease"].map({"Yes": 1, "No": 0})

# Convert Yes/No columns to 1/0
yes_no_cols = [
    "Smoking", "AlcoholDrinking", "Stroke", "DiffWalking",
    "PhysicalActivity", "Asthma", "KidneyDisease", "SkinCancer"
]

for col in yes_no_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0})


# Split into X and y
print("\nSplitting data...")

X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]


# Train split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
print("\nTraining model...")

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Test model
print("\nTesting model...")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save model
print("\nSaving model...")

joblib.dump(model, "heart_model.pkl")

print("Done! Model saved as heart_model.pkl")
