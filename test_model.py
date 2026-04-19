import pytest
from predict import make_small, age_map

# check Age Mapping
def test_age_logic():
    assert age_map("18-24") == 1
    assert age_map("80 or older") == 13

# check BMI/Health Scaling
def test_scaling_logic():
    assert make_small(25.0) == 2
    assert make_small(0) == 0

def test_full_prediction_flow():
    from predict import predict_heart_disease
    sample_user = {
        "BMI": 22.0, "Smoking": "No", "AlcoholDrinking": "No",
        "Stroke": "No", "PhysicalHealth": 2, "MentalHealth": 5,
        "DiffWalking": "No", "Sex": "Female", "AgeCategory": "30-34",
        "Race": "Asian", "Diabetic": "No", "PhysicalActivity": "Yes",
        "GenHealth": "Very good", "SleepTime": 7, "Asthma": "No",
        "KidneyDisease": "No", "SkinCancer": "No"
    }
    result = predict_heart_disease(sample_user)
    #t the result must be 0 (No) or 1 (Yes)
    assert result in [0, 1]

def test_invalid_age_category():
    from predict import age_map
    with pytest.raises(KeyError):
        age_map("Not-An-Age")

def test_prediction_consistency():
    from predict import predict_heart_disease
    user_data = {
        "BMI": 30.0, "Smoking": "Yes", "AlcoholDrinking": "No",
        "Stroke": "No", "PhysicalHealth": 10, "MentalHealth": 10,
        "DiffWalking": "Yes", "Sex": "Male", "AgeCategory": "60-64",
        "Race": "White", "Diabetic": "Yes", "PhysicalActivity": "No",
        "GenHealth": "Fair", "SleepTime": 6, "Asthma": "No",
        "KidneyDisease": "No", "SkinCancer": "No"
    }
    first_run = predict_heart_disease(user_data)
    second_run = predict_heart_disease(user_data)
    assert first_run == second_run


def test_extreme_bmi_scaling():
    from predict import make_small
    assert make_small(99.9) == 9
    assert make_small(0) == 0
