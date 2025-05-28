import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header(' App (Prototype)')

data = pd.DataFrame()

col1, col2, col3 = st.columns(3)
with col1:
    admission_grade = float(st.number_input(label='Admission grade', value=95.00))
    data["Admission_grade"] = [admission_grade]
with col2:
    Age = int(st.number_input(label='Age', value=19))
    data["Age_at_enrollment"] = [Age]
with col3:
    application_mode = st.selectbox(
        label='Application mode',
        options=[17, 15, 1, 39, 18, 53, 44, 51, 43, 7, 42, 16, 5, 2, 10, 57, 26, 27],
        index=2  # Default value is 1 (index 2 in the list)
    )
    data["Application_mode"] = [application_mode]

col1, col2, col3, col4 = st.columns(4)
with col1:
    application_type = int(st.number_input(label='Application type', value=0, min_value=0, max_value=9, step=1))
    data["Application_order"] = [application_type]
with col2:
    course = int(st.number_input(label='Course', value=1, min_value=1, max_value=20, step=1))
    data["Course"] = [course]
with col3:
    attendance = int(st.number_input(label='Attendance', value=1, min_value=0, max_value=1, step=1))
    data["Daytime_evening_attendance"] = [attendance]
with col4:
    debtor = int(st.number_input(label='Debtor', value=0, min_value=0, max_value=1, step=1))
    data["Debtor"] = [debtor]

col1, col2, col3, col4 = st.columns(4)
with col1:
    displaced = int(st.number_input(label='Displaced', value=0, min_value=0, max_value=1, step=1))
    data["Displaced"] = [displaced]
with col2:
    educational_needs = int(st.number_input(label='Educational needs', value=0, min_value=0, max_value=1, step=1))
    data["Educational_special_needs"] = [educational_needs]
with col3:
    gdp = float(st.number_input(label='GDP', value=-1.0, min_value=-4.06, max_value=3.51))
    data["GDP"] = [gdp]
with col4:
    gender = int(st.number_input(label='Gender', value=0, min_value=0, max_value=1, step=1))
    data["Gender"] = [gender]
col1, col2, col3, col4 = st.columns(4)
with col1:
    inflation_rate = float(st.number_input(label='Inflation rate', value=0.0, min_value=-0.80, max_value=3.70))
    data["Inflation_rate"] = [inflation_rate]
with col2:
    international = int(st.number_input(label='International', value=0, min_value=0, max_value=1, step=1))
    data["International"] = [international]
with col3:
    marital_status = int(st.number_input(label='Marital status', value=0, min_value=0, max_value=6, step=1))
    data["Marital_status"] = [marital_status]
with col4:
    nacionality = st.selectbox(
        label='Nacionality',
        options=[1, 62, 6, 41, 26, 103, 13, 25, 21, 101, 11, 22, 32, 100, 24, 109, 2, 108, 105, 14, 17],
        index=0  # Default value is 1 (index 0 in the list)
    )
    data["Nacionality"] = [nacionality]
col1, col2, col3, col4 = st.columns(4)
with col1:
    previous_qualification_grade = int(st.number_input(label='Previous qualification grade', value=95, min_value=95, max_value=190))
    data["Previous_qualification_grade"] = [previous_qualification_grade]
with col2:
    previous_qualification = int(st.number_input(label='Previous qualification', value=0, min_value=0, max_value=3, step=1))
    data["Previous_qualification"] = [previous_qualification]
with col3:
    scholarship = int(st.number_input(label='Scholarship', value=0, min_value=0, max_value=1, step=1))
    data["Scholarship_holder"] = [scholarship]
with col4:
    tuition_fees_up_to_date = int(st.number_input(label='Tuition fees up to date', value=1, min_value=0, max_value=1, step=1))
    data["Tuition_fees_up_to_date"] = [tuition_fees_up_to_date]
with col1:
    unemployment_rate = float(st.number_input(label='Unemployment rate', value=0.0, min_value=0.0, max_value=20.0))
    data["Unemployment_rate"] = [unemployment_rate]

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)


if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Credit Scoring: {}".format(prediction(new_data)))