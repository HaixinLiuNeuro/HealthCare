import pandas as pd
import numpy as np

# generate sythetic data
def generate_simulated_data():
    # Simulated Patient Dataset
    data = {
        "patient_id": range(1, 11),
        "age": [45, 67, 34, 70, 50, 29, 80, 60, 55, 40],
        "gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Other", "Female", "Male"],
        "bmi": [22.5, 31.2, 27.5, 35.6, 29.8, 18.7, 40.1, 33.0, 26.2, 24.5],
        "blood_pressure": ["120/80", "145/95", "118/76", "160/100", "130/85", "110/70", "170/110", "140/90", "125/82", "119/79"],
        "cholesterol_level": ["Normal", "High", "Normal", "High", "Borderline", "Normal", "High", "High", "Borderline", "Normal"],
        "diabetes": ["No", "Yes", "No", "Yes", "No", "No", "Yes", "Yes", "No", "No"],
        "heart_disease": ["No", "Yes", "No", "Yes", "No", "No", "Yes", "Yes", "No", "No"],
        "last_visit_date": ["2024-01-15", "2023-11-20", "2024-02-10", "2023-08-25", "2023-12-30", "2024-02-01", "2023-05-18", "2023-09-10", "2023-11-22", "2024-01-05"]
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df

# Example usage
# df = generate_simulated_data()
# print(df)

# feature engineering
def calculate_risk(row):
    score = 0

    # Age factor
    if row["age"] > 60:
        score += 2

    # BMI factor
    if row["bmi"] > 30:
        score += 2

    # Blood Pressure factor
    if row["systolic_bp"] > 140 or row["diastolic_bp"] > 90:
        score += 2

    # Cholesterol level factor
    if row["cholesterol_level"] == "High":
        score += 2

    # Diabetes factor
    if row["diabetes"] == "Yes":
        score += 2

    # Heart disease factor
    if row["heart_disease"] == "Yes":
        score += 2

    return score

# Apply the function to calculate risk score
# df["risk_score"] = df.apply(calculate_risk, axis=1)

# # Classify risk levels
# df["risk_level"] = pd.cut(df["risk_score"], bins=[0, 4, 8, 12], labels=["Low", "Medium", "High"])

# print(df[["patient_id", "age", "bmi", "systolic_bp", "diastolic_bp", "cholesterol_level", "diabetes", "heart_disease", "risk_score", "risk_level"]])

