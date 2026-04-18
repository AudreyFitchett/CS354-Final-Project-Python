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
    "18-24": 1,
    "25-29": 2,
    "30-34": 3,
    "35-39": 4,
    "40-44": 5,
    "45-49": 6,
    "50-54": 7,
    "55-59": 8,
    "60-64": 9,
    "65-69": 10,
    "70-74": 11,
    "75-79": 12,
    "80 or older": 13
}

df["Race"] = df["Race"].map({
    "White": 1,
    "Black": 2,
    "Asian": 3,
    "American Indian/Alaskan Native": 4,
    "Hispanic": 5,
    "Other": 6
})

df["Diabetic"] = df["Diabetic"].map({
    "No": 0,
    "No, borderline diabetes": 1,
    "Yes": 2,
    "Yes (during pregnancy)": 1
})

df["GenHealth"] = df["GenHealth"].map({
    "Poor": 1,
    "Fair": 2,
    "Good": 3,
    "Very good": 4,
    "Excellent": 5
})

def small_bmi(bmi):
    if bmi == 0:
        return 0
    else:
        return int(bmi / 10)

def big_health(health):
    return int(health / 10) + 1
    
df["HeartDisease"] = df["HeartDisease"].map({"Yes": 1, "No": 0})

df["Sex"] = df["Sex"].map({"Female": 1, "Male": 0})

df["AgeCategory"] = df["AgeCategory"].map(AGE_CATEGORY)

df["BMI"] = df["BMI"].apply(small_bmi)

df["PhysicalHealth"] = df["PhysicalHealth"].apply(small_bmi)

df["MentalHealth"] = df["MentalHealth"].apply(small_bmi)

df = df.fillna(0)

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

model = LogisticRegression(max_iter=1000, class_weight="balanced")
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
