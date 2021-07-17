from fastapi.testclient import TestClient
from main import app
import datetime

# test to check the correct functioning of the /Group16 route
def test_Group16():
    with TestClient(app) as client:
        response = client.get("/Group16")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"Group16": "Members are Geeth and Ameer", "run_Time_timestamp":str(datetime.datetime.now().replace(microsecond=0))}

# testing just whether the classes api is working fine
def test_classes():
    with TestClient(app) as client:
        response = client.get("/classes")
        # asserting the correct response status is received
        assert response.status_code == 200

# test to check if Bad risk is classified correctly
def test_pred_Bad_risk():
    # defining a sample payload for the testcase
    payload = {
        "Status_of_existing_account": 1,
        "Duration_of_Credit_month": 60,
        "Payment_Status_of_Previous_Credit": 2,
        "Purpose_of_loan": 5,
        "Credit_Amount": 100000,
        "Value_of_Savings_accountbonds": 1,
        "Years_of_Present_Employment": 1,
        "Percentage_of_disposable_income": 1,
        "Sex_Marital_Status": 1,
        "Guarantors_Debtors": 1,
        "Duration_in_Present_Residence": 1,
        "Property": 1,
        "Age_in_years": 65,
        "Concurrent_Credits": 1,
        "Housing": 1,
        "No_of_Credits_at_this__Bank": 1,
        "Occupation": 1,
        "No_of_dependents": 1,
        "Telephone": 1,
        "Foreign_Worker": 1,
    }
    with TestClient(app) as client:
        response = client.post("/predict_creditscore", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"Cost_Matrix_Risk": "Bad Risk", "run_Time_timestamp":str(datetime.datetime.now().replace(microsecond=0))}


def test_pred_Good_risk():
    # defining a sample payload for the testcase
    payload = {
        "Status_of_existing_account": 4,
        "Duration_of_Credit_month": 9,
        "Payment_Status_of_Previous_Credit": 4,
        "Purpose_of_loan": 0,
        "Credit_Amount": 841,
        "Value_of_Savings_accountbonds": 1,
        "Years_of_Present_Employment": 2,
        "Percentage_of_disposable_income": 4,
        "Sex_Marital_Status": 2,
        "Guarantors_Debtors": 1,
        "Duration_in_Present_Residence": 4,
        "Property": 2,
        "Age_in_years": 21,
        "Concurrent_Credits": 3,
        "Housing": 1,
        "No_of_Credits_at_this__Bank": 1,
        "Occupation": 3,
        "No_of_dependents": 2,
        "Telephone": 1,
        "Foreign_Worker": 2,
    }
    with TestClient(app) as client:
        response = client.post("/predict_creditscore", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"Cost_Matrix_Risk": "Good Risk", "run_Time_timestamp":str(datetime.datetime.now().replace(microsecond=0))}

# TC2: Here we are checking correct functioning of feedback loop by providing a valid payload.
def test_feedback_loop():
    #defining a sample payload for the testcase
    payload = [{
        "Status_of_existing_account": 2,
        "Duration_of_Credit_month": 18,
        "Payment_Status_of_Previous_Credit": 4,
        "Purpose_of_loan": 2,
        "Credit_Amount": 1049,
        "Value_of_Savings_accountbonds": 1,
        "Years_of_Present_Employment": 2,
        "Percentage_of_disposable_income": 4,
        "Sex_Marital_Status": 2,
        "Guarantors_Debtors": 1,
        "Duration_in_Present_Residence": 4,
        "Property": 2,
        "Age_in_years": 21,
        "Concurrent_Credits": 3,
        "Housing": 1,
        "No_of_Credits_at_this__Bank": 1,
        "Occupation": 3,
        "No_of_dependents": 2,
        "Telephone": 1,
        "Foreign_Worker": 2,
        "Cost_Matrix_Risk": "Good Risk",
    }]
    with TestClient(app) as client:
        response = client.post("/feedback_loop", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"detail": "Feedback loop successful", "run_Time_timestamp":str(datetime.datetime.now().replace(microsecond=0))}