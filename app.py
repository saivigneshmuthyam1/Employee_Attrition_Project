# import streamlit as st
# import pandas as pd
# import joblib
# import os

# print(os.listdir())
# # Load Model
# model = joblib.load(
#     "attrition_model_v2.pkl"
# )

# THRESHOLD = 0.40

# st.set_page_config(
#     page_title="Employee Attrition Predictor",
#     layout="wide"
# )

# st.title("AI Powered Employee Attrition Prediction System")

# st.write(
#     "Predict employee attrition risk using Machine Learning"
# )


import streamlit as st
import pandas as pd
import joblib
import traceback

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
try:
    model = joblib.load("attrition_model_v2.pkl")
    st.success("✅ Model Loaded Successfully")

except Exception as e:
    st.error("❌ Model Loading Failed")
    st.code(traceback.format_exc())
    st.stop()

# -----------------------------
# THRESHOLD
# -----------------------------
THRESHOLD = 0.40

# -----------------------------
# TITLE
# -----------------------------
st.title("AI Powered Employee Attrition Prediction System")

st.markdown("""
Predict employee attrition risk using Machine Learning.

This system analyzes employee information and estimates the probability of attrition.
""")

st.divider()

# -----------------------------
# INPUT SECTION
# -----------------------------
st.header("Employee Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=25000,
        value=5000
    )

    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced"]
    )

    department = st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col2:

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        [1, 2, 3, 4]
    )

    environment_satisfaction = st.selectbox(
        "Environment Satisfaction",
        [1, 2, 3, 4]
    )

    years_at_company = st.number_input(
        "Years At Company",
        min_value=0,
        max_value=40,
        value=5
    )

    total_working_years = st.number_input(
        "Total Working Years",
        min_value=0,
        max_value=40,
        value=8
    )

    stock_option_level = st.selectbox(
        "Stock Option Level",
        [0, 1, 2, 3]
    )

    work_life_balance = st.selectbox(
        "Work Life Balance",
        [1, 2, 3, 4]
    )

st.divider()

# -----------------------------
# PREDICTION BUTTON
# -----------------------------
if st.button("🔍 Predict Attrition Risk"):

    employee = pd.DataFrame([{
        'Age': age,
        'BusinessTravel': 'Travel_Rarely',
        'DailyRate': 800,
        'Department': department,
        'DistanceFromHome': 5,
        'Education': 3,
        'EducationField': 'Marketing',
        'EnvironmentSatisfaction': environment_satisfaction,
        'Gender': gender,
        'HourlyRate': 60,
        'JobInvolvement': 3,
        'JobLevel': 2,
        'JobSatisfaction': job_satisfaction,
        'JobRole': 'Sales Executive',
        'MaritalStatus': marital_status,
        'MonthlyIncome': monthly_income,
        'MonthlyRate': 15000,
        'NumCompaniesWorked': 2,
        'OverTime': overtime,
        'PercentSalaryHike': 15,
        'PerformanceRating': 3,
        'RelationshipSatisfaction': 3,
        'StockOptionLevel': stock_option_level,
        'TotalWorkingYears': total_working_years,
        'TrainingTimesLastYear': 2,
        'WorkLifeBalance': work_life_balance,
        'YearsAtCompany': years_at_company,
        'YearsInCurrentRole': 3,
        'YearsSinceLastPromotion': 1,
        'YearsWithCurrManager': 3
    }])

    try:

        probability = model.predict_proba(employee)[0][1]

        prediction = int(
            probability >= THRESHOLD
        )

        if probability < 0.30:
            risk = "Low Risk"
            color = "🟢"

        elif probability < 0.70:
            risk = "Medium Risk"
            color = "🟡"

        else:
            risk = "High Risk"
            color = "🔴"

        st.divider()

        st.header("Prediction Results")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Attrition Probability",
                f"{probability*100:.2f}%"
            )

        with c2:
            st.metric(
                "Prediction",
                "Likely To Leave" if prediction == 1 else "Likely To Stay"
            )

        with c3:
            st.metric(
                "Risk Level",
                risk
            )

        st.progress(float(probability))

        st.subheader(f"{color} {risk}")

        if risk == "High Risk":

            st.error("""
            Employee shows a strong probability of attrition.

            Suggested Actions:
            - HR discussion
            - Salary review
            - Workload review
            - Engagement survey
            """)

        elif risk == "Medium Risk":

            st.warning("""
            Employee may be at moderate attrition risk.

            Suggested Actions:
            - Monitor satisfaction
            - Conduct periodic check-ins
            - Review career growth opportunities
            """)

        else:

            st.success("""
            Employee appears stable.

            Suggested Actions:
            - Continue engagement
            - Maintain satisfaction levels
            """)

        st.subheader("Employee Summary")

        st.dataframe(employee)

    except Exception as e:

        st.error("Prediction Failed")

        st.code(traceback.format_exc())
