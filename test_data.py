import pytest
import pandas as pd
from data_setup import load_heart_data

# these tests are used to ensure the data is read correctly
@pytest.fixture
def heart_data():
    return load_heart_data()

def test_dataset_columns(heart_data):
    """Verifies all required features are present in the Kaggle download."""
    expected_columns = ['HeartDisease', 'BMI', 'Smoking', 'AgeCategory', 'Diabetic']
    for col in expected_columns:
        assert col in heart_data.columns, f"Missing critical column: {col}"

def test_no_empty_predictions(heart_data):
    """Ensures there are no missing values in the target 'HeartDisease' column."""
    assert heart_data['HeartDisease'].isnull().sum() == 0

def test_data_is_not_empty(heart_data):
    """Ensures the dataframe actually contains rows."""
    assert len(heart_data) > 0

def test_bmi_range(heart_data):
    """Sanity check: BMI should be within a reasonable human range."""
    assert heart_data['BMI'].min() >= 10
    assert heart_data['BMI'].max() <= 100

def test_heart_data_structure(heart_data):
    required_columns = ['HeartDisease', 'BMI', 'Smoking', 'AgeCategory']
    for col in required_columns:
        assert col in heart_data.columns, f"Missing critical column: {col}"

def test_bmi_validity(heart_data):
    assert heart_data['BMI'].min() > 0
    assert heart_data['BMI'].max() < 100
