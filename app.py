# import streamlit as st
# import pandas as pd
# import joblib
# import traceback

# # =====================================================
# # PAGE CONFIG
# # =====================================================

# st.set_page_config(
#     page_title="Employee Attrition Intelligence Dashboard",
#     page_icon="📊",
#     layout="wide"
# )

# # =====================================================
# # CUSTOM CSS
# # =====================================================

# st.markdown("""
# <style>

# .main {
#     background-color: #f8fafc;
# }

# .hero {
#     background: linear-gradient(135deg,#1e3a8a,#2563eb);
#     padding: 30px;
#     border-radius: 15px;
#     color: white;
#     text-align: center;
#     margin-bottom: 25px;
# }

# .section-header {
#     background: white;
#     padding: 12px;
#     border-radius: 10px;
#     border-left: 6px solid #2563eb;
#     margin-bottom: 15px;
#     box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
# }

# .metric-container {
#     background: white;
#     padding: 20px;
#     border-radius: 15px;
#     box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
# }

# .low-risk {
#     background:#dcfce7;
#     color:#166534;
#     padding:15px;
#     border-radius:12px;
#     font-size:18px;
#     font-weight:bold;
# }

# .medium-risk {
#     background:#fef9c3;
#     color:#854d0e;
#     padding:15px;
#     border-radius:12px;
#     font-size:18px;
#     font-weight:bold;
# }

# .high-risk {
#     background:#fee2e2;
#     color:#991b1b;
#     padding:15px;
#     border-radius:12px;
#     font-size:18px;
#     font-weight:bold;
# }

# .stButton>button {
#     width:100%;
#     height:60px;
#     font-size:20px;
#     font-weight:bold;
#     border-radius:12px;
# }

# </style>
# """, unsafe_allow_html=True)

# # =====================================================
# # LOAD MODEL
# # =====================================================

# try:
#     model = joblib.load("attrition_model_v2.pkl")

# except Exception:
#     st.error("❌ Model Loading Failed")
#     st.code(traceback.format_exc())
#     st.stop()

# # =====================================================
# # SIDEBAR
# # =====================================================

# with st.sidebar:

#     st.title("📊 HR Analytics")

#     st.success("Model Loaded Successfully")

#     st.markdown("---")

#     st.info("""
#     Employee Attrition Intelligence System

#     Predict employee resignation risk using
#     Machine Learning and HR Analytics.
#     """)

#     st.markdown("---")

#     st.metric(
#         "Prediction Threshold",
#         "40%"
#     )

#     st.metric(
#         "Model Status",
#         "Active"
#     )

# # =====================================================
# # HEADER
# # =====================================================

# st.markdown("""
# <div class="hero">
#     <h1>📊 Employee Attrition Intelligence Dashboard</h1>
#     <h4>AI Powered Workforce Retention Analytics</h4>
#     <p>
#     Predict employee attrition risk and identify employees
#     likely to leave the organization.
#     </p>
# </div>
# """, unsafe_allow_html=True)

# # =====================================================
# # THRESHOLD
# # =====================================================

# THRESHOLD = 0.40

# # =====================================================
# # INPUT SECTION
# # =====================================================

# st.markdown("""
# <div class="section-header">
# <h3>👨‍💼 Employee Information</h3>
# </div>
# """, unsafe_allow_html=True)

# col1, col2 = st.columns(2)

# with col1:

#     age = st.number_input(
#         "Age",
#         min_value=18,
#         max_value=60,
#         value=30
#     )

#     monthly_income = st.number_input(
#         "Monthly Income",
#         min_value=1000,
#         max_value=50000,
#         value=5000
#     )

#     overtime = st.selectbox(
#         "OverTime",
#         ["No", "Yes"]
#     )

#     marital_status = st.selectbox(
#         "Marital Status",
#         ["Single", "Married", "Divorced"]
#     )

#     department = st.selectbox(
#         "Department",
#         [
#             "Sales",
#             "Research & Development",
#             "Human Resources"
#         ]
#     )

#     gender = st.selectbox(
#         "Gender",
#         ["Male", "Female"]
#     )

# with col2:

#     job_satisfaction = st.selectbox(
#         "Job Satisfaction",
#         [1, 2, 3, 4]
#     )

#     environment_satisfaction = st.selectbox(
#         "Environment Satisfaction",
#         [1, 2, 3, 4]
#     )

#     years_at_company = st.number_input(
#         "Years At Company",
#         min_value=0,
#         max_value=40,
#         value=5
#     )

#     total_working_years = st.number_input(
#         "Total Working Years",
#         min_value=0,
#         max_value=40,
#         value=8
#     )

#     stock_option_level = st.selectbox(
#         "Stock Option Level",
#         [0, 1, 2, 3]
#     )

#     work_life_balance = st.selectbox(
#         "Work Life Balance",
#         [1, 2, 3, 4]
#     )

# st.markdown("<br>", unsafe_allow_html=True)

# predict = st.button(
#     "🚀 Analyze Employee Attrition Risk"
# )

# # =====================================================
# # PREDICTION
# # =====================================================

# if predict:

#     employee = pd.DataFrame([{
#         'Age': age,
#         'BusinessTravel': 'Travel_Rarely',
#         'DailyRate': 800,
#         'Department': department,
#         'DistanceFromHome': 5,
#         'Education': 3,
#         'EducationField': 'Marketing',
#         'EnvironmentSatisfaction': environment_satisfaction,
#         'Gender': gender,
#         'HourlyRate': 60,
#         'JobInvolvement': 3,
#         'JobLevel': 2,
#         'JobSatisfaction': job_satisfaction,
#         'JobRole': 'Sales Executive',
#         'MaritalStatus': marital_status,
#         'MonthlyIncome': monthly_income,
#         'MonthlyRate': 15000,
#         'NumCompaniesWorked': 2,
#         'OverTime': overtime,
#         'PercentSalaryHike': 15,
#         'PerformanceRating': 3,
#         'RelationshipSatisfaction': 3,
#         'StockOptionLevel': stock_option_level,
#         'TotalWorkingYears': total_working_years,
#         'TrainingTimesLastYear': 2,
#         'WorkLifeBalance': work_life_balance,
#         'YearsAtCompany': years_at_company,
#         'YearsInCurrentRole': 3,
#         'YearsSinceLastPromotion': 1,
#         'YearsWithCurrManager': 3
#     }])

#     try:

#         probability = model.predict_proba(employee)[0][1]

#         prediction = int(probability >= THRESHOLD)

#         if probability < 0.30:
#             risk = "Low Risk"

#         elif probability < 0.70:
#             risk = "Medium Risk"

#         else:
#             risk = "High Risk"

#         st.markdown("---")

#         st.markdown("""
#         <div class="section-header">
#         <h3>📈 Prediction Dashboard</h3>
#         </div>
#         """, unsafe_allow_html=True)

#         c1, c2, c3 = st.columns(3)

#         with c1:
#             st.metric(
#                 "Attrition Probability",
#                 f"{probability*100:.2f}%"
#             )

#         with c2:
#             st.metric(
#                 "Prediction",
#                 "Likely To Leave"
#                 if prediction == 1
#                 else "Likely To Stay"
#             )

#         with c3:
#             st.metric(
#                 "Risk Level",
#                 risk
#             )

#         st.subheader("📊 Attrition Risk Meter")

#         st.progress(float(probability))

#         st.caption(
#             f"Risk Score: {probability*100:.2f}%"
#         )

#         st.markdown("<br>", unsafe_allow_html=True)

#         if risk == "High Risk":

#             st.markdown("""
#             <div class="high-risk">
#             🔴 HIGH RISK EMPLOYEE
#             <br><br>
#             Immediate HR intervention recommended.
#             </div>
#             """, unsafe_allow_html=True)

#         elif risk == "Medium Risk":

#             st.markdown("""
#             <div class="medium-risk">
#             🟡 MEDIUM RISK EMPLOYEE
#             <br><br>
#             Employee engagement monitoring recommended.
#             </div>
#             """, unsafe_allow_html=True)

#         else:

#             st.markdown("""
#             <div class="low-risk">
#             🟢 LOW RISK EMPLOYEE
#             <br><br>
#             Employee appears stable and engaged.
#             </div>
#             """, unsafe_allow_html=True)

#         st.markdown("<br>", unsafe_allow_html=True)

#         st.subheader("📋 Employee Snapshot")

#         summary = pd.DataFrame({
#             "Feature": [
#                 "Age",
#                 "Monthly Income",
#                 "Department",
#                 "Gender",
#                 "Years At Company",
#                 "Total Working Years",
#                 "Work Life Balance",
#                 "Job Satisfaction"
#             ],
#             "Value": [
#                 age,
#                 monthly_income,
#                 department,
#                 gender,
#                 years_at_company,
#                 total_working_years,
#                 work_life_balance,
#                 job_satisfaction
#             ]
#         })

#         st.dataframe(
#             summary,
#             use_container_width=True,
#             hide_index=True
#         )

#         with st.expander("🔍 View Model Input Data"):

#             st.dataframe(
#                 employee,
#                 use_container_width=True
#             )

#     except Exception:

#         st.error("❌ Prediction Failed")

#         st.code(
#             traceback.format_exc()
#         )



import streamlit as st
import pandas as pd
import joblib
import traceback
import plotly.graph_objects as go

st.set_page_config(page_title="Employee Attrition Intelligence Platform",
                   page_icon="📊",
                   layout="wide")

st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#0f172a,#1e293b,#0f172a);
}
.hero{
padding:35px;border-radius:20px;
background:linear-gradient(135deg,#2563eb,#7c3aed);
color:white;text-align:center;margin-bottom:20px;
}
.card{
background:rgba(255,255,255,.08);
padding:15px;border-radius:15px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load("attrition_model_v2.pkl")

try:
    model = load_model()
except Exception:
    st.error(traceback.format_exc())
    st.stop()

with st.sidebar:
    st.title("📊 HR Analytics")
    st.success("Model Online")
    st.metric("Threshold","40%")
    st.metric("Version","2.0")

st.markdown("""
<div class="hero">
<h1>🚀 Employee Attrition Intelligence Platform</h1>
<p>AI Powered Workforce Analytics Dashboard</p>
</div>
""", unsafe_allow_html=True)

k1,k2,k3,k4=st.columns(4)
k1.metric("Employees","1470")
k2.metric("Attrition Rate","16.1%")
k3.metric("Accuracy","92%")
k4.metric("Departments","3")

st.markdown("## 👤 Employee Profile")

c1,c2=st.columns(2)

with c1:
    age=st.number_input("Age",18,60,30)
    monthly_income=st.number_input("Monthly Income",1000,50000,5000)
    overtime=st.selectbox("OverTime",["No","Yes"])
    marital_status=st.selectbox("Marital Status",["Single","Married","Divorced"])
    department=st.selectbox("Department",["Sales","Research & Development","Human Resources"])
    gender=st.selectbox("Gender",["Male","Female"])

with c2:
    job_satisfaction=st.selectbox("Job Satisfaction",[1,2,3,4])
    environment_satisfaction=st.selectbox("Environment Satisfaction",[1,2,3,4])
    years_at_company=st.number_input("Years At Company",0,40,5)
    total_working_years=st.number_input("Total Working Years",0,40,8)
    stock_option_level=st.selectbox("Stock Option Level",[0,1,2,3])
    work_life_balance=st.selectbox("Work Life Balance",[1,2,3,4])

if st.button("🚀 Analyze Employee Attrition Risk", use_container_width=True):

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

    p = model.predict_proba(employee)[0][1]
    pred = "Likely To Leave" if p >= 0.40 else "Likely To Stay"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=p*100,
        title={'text':'Attrition Risk'},
        gauge={'axis':{'range':[0,100]}}
    ))
    st.plotly_chart(fig, use_container_width=True)

    a,b,c=st.columns(3)
    a.metric("Probability", f"{p*100:.2f}%")
    b.metric("Prediction", pred)
    c.metric("Risk", "High" if p>0.7 else "Medium" if p>0.3 else "Low")

    st.subheader("Employee Snapshot")
    st.dataframe(employee, use_container_width=True)
