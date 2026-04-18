import pandas as pd
import joblib

model = joblib.load("heart_model.pkl")

def yes_no(value):
    return 1 if value == "Yes" else 0

def sex_map(value):
    return 1 if value == "Male" else 0

def age_map(value):
    mapping = {
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
    return mapping[value]

def race_map(value):
    mapping = {
        "White": 1,
        "Black": 2,
        "Asian": 3,
        "American Indian/Alaskan Native": 4,
        "Hispanic": 5,
        "Other": 6
    }
    return mapping[value]

def diabetic_map(value):
    mapping = {
        "No": 0,
        "No, borderline diabetes": 1,
        "Yes": 2,
        "Yes (during pregnancy)": 1
    }
    return mapping[value]

def genhealth_map(value):
    mapping = {
        "Poor": 1,
        "Fair": 2,
        "Good": 3,
        "Very good": 4,
        "Excellent": 5
    }
    return mapping[value]

def make_small(value):
    if value == 0:
        return 0
    return int(value / 10)

def predict_heart_disease(user_input):
    processed = {
        "BMI": make_small(user_input["BMI"]),
        "Smoking": yes_no(user_input["Smoking"]),
        "AlcoholDrinking": yes_no(user_input["AlcoholDrinking"]),
        "Stroke": yes_no(user_input["Stroke"]),
        "PhysicalHealth": make_small(user_input["PhysicalHealth"]),
        "MentalHealth": make_small(user_input["MentalHealth"]),
        "DiffWalking": yes_no(user_input["DiffWalking"]),
        "Sex": sex_map(user_input["Sex"]),
        "AgeCategory": age_map(user_input["AgeCategory"]),
        "Race": race_map(user_input["Race"]),
        "Diabetic": diabetic_map(user_input["Diabetic"]),
        "PhysicalActivity": yes_no(user_input["PhysicalActivity"]),
        "GenHealth": genhealth_map(user_input["GenHealth"]),
        "SleepTime": user_input["SleepTime"],
        "Asthma": yes_no(user_input["Asthma"]),
        "KidneyDisease": yes_no(user_input["KidneyDisease"]),
        "SkinCancer": yes_no(user_input["SkinCancer"])
    }

    input_df = pd.DataFrame([processed])
    prediction = model.predict(input_df)[0]

    return prediction