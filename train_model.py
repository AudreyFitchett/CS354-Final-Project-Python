import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from bisect import bisect
import joblib

# Load the dataset
print("Loading data...")
df = pd.read_csv("heart_2020_cleaned.csv")

print("\nConverting data...")


# Convert Yes/No columns to 1/0
yes_no_cols = [
    "Smoking", "AlcoholDrinking", "Stroke", "DiffWalking",
    "PhysicalActivity", "Asthma", "KidneyDisease", "SkinCancer"
]

for col in yes_no_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0})

# More encoding
AGE_CATEGORY = {
    1: "Age 18 to 24",
    2: "Age 25 to 29",
    3: "Age 30 to 34",
    4: "Age 35 to 39",
    5: "Age 40 to 44",
    6: "Age 45 to 49",
    7: "Age 50 to 54",
    8: "Age 55 to 59",
    9: "Age 60 to 64",
    10: "Age 65 to 69",
    11: "Age 70 to 74",
    12: "Age 75 to 79",
    13: "Age 80 or older"
}

def small_bmi(bmi):
    if bmi == 0:
        return 0
    else:
        return int(bmi / 10)

def big_health(health)
    return int(health / 10) + 1
    
df["HeartDisease"] = df["HeartDisease"].map({"Yes": 1, "No": 0})

df["Sex"] = df["Sex"].map({"Female": 1, "Male": 0})

df["AgeCategory"] = df("AgeCategory".map(AGE_CATEGORY))

df["BMI"] = df("BMI".map(small_bmi, "BMI"))

df["PhysicalHealth"] = df("PhysicalHealth".map(small_bmi, "PhysicalHealth"))

pmask  = df["PhysicalHealth"]  != 0

df["MentalHealth"] = df("MentalHealth".map(small_bmi, "MentalHealth"))

mmask  = df["MentalHealth"]  != 0

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
