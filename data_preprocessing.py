# import joblib
# import numpy as np
# import pandas as pd


# # Load PCA models
# pca_1 = joblib.load('model/pca_1.joblib')
# pca_2 = joblib.load('model/pca_2.joblib')

# # Load scalers
# scaler_admission = joblib.load('model/scaler_Admission_grade.joblib')
# scaler_age = joblib.load('model/scaler_Age_at_enrollment.joblib')
# scaler_application_mode = joblib.load('model/scaler_Application_mode.joblib')
# scaler_application_order = joblib.load('model/scaler_Application_order.joblib')
# scaler_course = joblib.load('model/scaler_Course.joblib')
# scaler_daytime_evening = joblib.load('model/scaler_Daytime_evening_attendance.joblib')
# scaler_debtor = joblib.load('model/scaler_Debtor.joblib')
# scaler_displaced = joblib.load('model/scaler_Displaced.joblib')
# scaler_educational_needs = joblib.load('model/scaler_Educational_special_needs.joblib')
# scaler_gdp = joblib.load('model/scaler_GDP.joblib')
# scaler_gender = joblib.load('model/scaler_Gender.joblib')
# scaler_inflation = joblib.load('model/scaler_Inflation_rate.joblib')
# scaler_international = joblib.load('model/scaler_International.joblib')
# scaler_marital_status = joblib.load('model/scaler_Marital_status.joblib')
# scaler_nacionality = joblib.load('model/scaler_Nacionality.joblib')
# scaler_previous_qualification_grade = joblib.load('model/scaler_Previous_qualification_grade.joblib')
# scaler_previous_qualification = joblib.load('model/scaler_Previous_qualification.joblib')
# scaler_scholarship = joblib.load('model/scaler_Scholarship_holder.joblib')
# scaler_Tuition_fees_up_to_date = joblib.load('model/scaler_Tuition_fees_up_to_date.joblib')
# scaler_Unemployment_rate = joblib.load('model/scaler_Unemployment_rate.joblib')

# # Load models
# rdf_model = joblib.load('model/rdf_model.joblib')
# gboost_model = joblib.load('model/gboost_model.joblib')


# pca_numerical_columns_1 = [
#     'Curricular_units_1st_sem_credited',
#     'Curricular_units_1st_sem_enrolled',
#     'Curricular_units_1st_sem_evaluations',
#     'Curricular_units_1st_sem_approved',
#     'Curricular_units_1st_sem_grade',
#     'Curricular_units_1st_sem_without_evaluations',
#     'Curricular_units_2nd_sem_credited',
#     'Curricular_units_2nd_sem_enrolled',
#     'Curricular_units_2nd_sem_evaluations',
#     'Curricular_units_2nd_sem_approved',
#     'Curricular_units_2nd_sem_grade',
#     'Curricular_units_2nd_sem_without_evaluations'
# ]
# pca_numerical_columns_2 = [
#     'Mothers_qualification',
#     'Fathers_qualification',
#     'Mothers_occupation',
#     'Fathers_occupation'
# ]

# # def data_preprocessing(data):
# #     """Preprocessing data
 
# #     Args:
# #         data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
# #     return:
# #         Pandas DataFrame: Dataframe that contain all the preprocessed data
# #     """

# #     data = data.copy()
# #     df = pd.DataFrame()

# #     df['Admission_grade'] = scaler_admission.transform(np.asarray(data['Admission_grade']).reshape(-1, 1)).flatten()
# #     df['Age_at_enrollment'] = scaler_age.transform(np.asarray(data['Age_at_enrollment']).reshape(-1, 1)).flatten()
# #     df['Application_mode'] = scaler_application_mode.transform(np.asarray(data['Application_mode']).reshape(-1, 1)).flatten()
# #     df['Application_order'] = scaler_application_order.transform(np.asarray(data['Application_order']).reshape(-1, 1)).flatten()
# #     df['Course'] = scaler_course.transform(np.asarray(data['Course']).reshape(-1, 1)).flatten()
# #     df['Daytime_evening_attendance'] = scaler_daytime_evening.transform(np.asarray(data['Daytime_evening_attendance']).reshape(-1, 1)).flatten()
# #     df['Debtor'] = scaler_debtor.transform(np.asarray(data['Debtor']).reshape(-1, 1)).flatten()
# #     df['Displaced'] = scaler_displaced.transform(np.asarray(data['Displaced']).reshape(-1, 1)).flatten()
# #     df['Educational_special_needs'] = scaler_educational_needs.transform(np.asarray(data['Educational_special_needs']).reshape(-1, 1)).flatten()
# #     df['GDP'] = scaler_gdp.transform(np.asarray(data['GDP']).reshape(-1, 1)).flatten()
# #     df['Gender'] = scaler_gender.transform(np.asarray(data['Gender']).reshape(-1, 1)).flatten()
# #     df['Inflation_rate'] = scaler_inflation.transform(np.asarray(data['Inflation_rate']).reshape(-1, 1)).flatten()
# #     df['International'] = scaler_international.transform(np.asarray(data['International']).reshape(-1, 1)).flatten()
# #     df['Marital_status'] = scaler_marital_status.transform(np.asarray(data['Marital_status']).reshape(-1, 1)).flatten()
# #     df['Nacionality'] = scaler_nacionality.transform(np.asarray(data['Nacionality']).reshape(-1, 1)).flatten()
# #     df['Previous_qualification_grade'] = scaler_previous_qualification_grade.transform(np.asarray(data['Previous_qualification_grade']).reshape(-1, 1)).flatten()
# #     df['Previous_qualification'] = scaler_previous_qualification.transform(np.asarray(data['Previous_qualification']).reshape(-1, 1)).flatten()
# #     df['Scholarship_holder'] = scaler_scholarship.transform(np.asarray(data['Scholarship_holder']).reshape(-1, 1)).flatten()
# #     df['Tuition_fees_up_to_date'] = scaler_Tuition_fees_up_to_date.transform(np.asarray(data['Tuition_fees_up_to_date']).reshape(-1, 1)).flatten()
# #     df['Unemployment_rate'] = scaler_Unemployment_rate.transform(np.asarray(data['Unemployment_rate']).reshape(-1, 1)).flatten()

  

# #      # Validasi kolom untuk PCA
# #     missing_columns_1 = [col for col in pca_numerical_columns_1 if col not in data.columns]
# #     missing_columns_2 = [col for col in pca_numerical_columns_2 if col not in data.columns]

# #     if missing_columns_1:
# #         print(f"Missing columns for PCA 1: {missing_columns_1}")
# #         for col in missing_columns_1:
# #             data[col] = 0

# #     if missing_columns_2:
# #         print(f"Missing columns for PCA 2: {missing_columns_2}")
# #         for col in missing_columns_2:
# #             data[col] = 0

# #     # Apply PCA
# #     df[['pc1_1', 'pc1_2', 'pc1_3', 'pc1_4']] = pca_1.transform(data[pca_numerical_columns_1])
# #     df[['pc2_1', 'pc2_2']] = pca_2.transform(data[pca_numerical_columns_2])

# #     # Pastikan urutan kolom sesuai dengan model
# #     expected_columns = [
# #         'Marital_status', 'Application_mode', 'Application_order', 'Course',
# #         'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
# #         'Nacionality', 'Admission_grade', 'Displaced', 'Debtor', 'Educational_special_needs',
# #         'GDP', 'Gender', 'Inflation_rate', 'International', 'Unemployment_rate',
# #         'Age_at_enrollment', 'Scholarship_holder', 'Tuition_fees_up_to_date',
# #         'pc1_1', 'pc1_2', 'pc1_3', 'pc1_4', 'pc2_1', 'pc2_2'
# #     ]
# #     df = df[expected_columns]


# #     # # Apply PCA on numerical columns
# #     # df[['pc1_1', 'pc1_2', 'pc1_3', 'pc1_4']] = pca_1.transform(data[pca_numerical_columns_1])
# #     # df[['pc2_1', 'pc2_2']] = pca_2.transform(data[pca_numerical_columns_2])

# #     return df


# def data_preprocessing(data):
#     """Preprocessing data

#     Args:
#         data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
#     return:
#         Pandas DataFrame: Dataframe that contain all the preprocessed data
#     """

#     data = data.copy()
#     df = pd.DataFrame()

#     # Apply scalers
#     df['Admission_grade'] = scaler_admission.transform(np.asarray(data['Admission_grade']).reshape(-1, 1)).flatten()
#     df['Age_at_enrollment'] = scaler_age.transform(np.asarray(data['Age_at_enrollment']).reshape(-1, 1)).flatten()
#     df['Application_mode'] = scaler_application_mode.transform(np.asarray(data['Application_mode']).reshape(-1, 1)).flatten()
#     df['Application_order'] = scaler_application_order.transform(np.asarray(data['Application_order']).reshape(-1, 1)).flatten()
#     df['Course'] = scaler_course.transform(np.asarray(data['Course']).reshape(-1, 1)).flatten()
#     df['Daytime_evening_attendance'] = scaler_daytime_evening.transform(np.asarray(data['Daytime_evening_attendance']).reshape(-1, 1)).flatten()
#     df['Debtor'] = scaler_debtor.transform(np.asarray(data['Debtor']).reshape(-1, 1)).flatten()
#     df['Displaced'] = scaler_displaced.transform(np.asarray(data['Displaced']).reshape(-1, 1)).flatten()
#     df['Educational_special_needs'] = scaler_educational_needs.transform(np.asarray(data['Educational_special_needs']).reshape(-1, 1)).flatten()
#     df['GDP'] = scaler_gdp.transform(np.asarray(data['GDP']).reshape(-1, 1)).flatten()
#     df['Gender'] = scaler_gender.transform(np.asarray(data['Gender']).reshape(-1, 1)).flatten()
#     df['Inflation_rate'] = scaler_inflation.transform(np.asarray(data['Inflation_rate']).reshape(-1, 1)).flatten()
#     df['International'] = scaler_international.transform(np.asarray(data['International']).reshape(-1, 1)).flatten()
#     df['Marital_status'] = scaler_marital_status.transform(np.asarray(data['Marital_status']).reshape(-1, 1)).flatten()
#     df['Nacionality'] = scaler_nacionality.transform(np.asarray(data['Nacionality']).reshape(-1, 1)).flatten()
#     df['Previous_qualification_grade'] = scaler_previous_qualification_grade.transform(np.asarray(data['Previous_qualification_grade']).reshape(-1, 1)).flatten()
#     df['Previous_qualification'] = scaler_previous_qualification.transform(np.asarray(data['Previous_qualification']).reshape(-1, 1)).flatten()
#     df['Scholarship_holder'] = scaler_scholarship.transform(np.asarray(data['Scholarship_holder']).reshape(-1, 1)).flatten()
#     df['Tuition_fees_up_to_date'] = scaler_Tuition_fees_up_to_date.transform(np.asarray(data['Tuition_fees_up_to_date']).reshape(-1, 1)).flatten()
#     df['Unemployment_rate'] = scaler_Unemployment_rate.transform(np.asarray(data['Unemployment_rate']).reshape(-1, 1)).flatten()

#     # Validate columns for PCA
#     missing_columns_1 = [col for col in pca_numerical_columns_1 if col not in data.columns]
#     missing_columns_2 = [col for col in pca_numerical_columns_2 if col not in data.columns]

#     if missing_columns_1:
#         print(f"Missing columns for PCA 1: {missing_columns_1}")
#         for col in missing_columns_1:
#             data[col] = 0

#     if missing_columns_2:
#         print(f"Missing columns for PCA 2: {missing_columns_2}")
#         for col in missing_columns_2:
#             data[col] = 0

#     # Apply PCA
#     df[['pc1_1', 'pc1_2', 'pc1_3', 'pc1_4']] = pca_1.transform(data[pca_numerical_columns_1])
#     df[['pc2_1', 'pc2_2']] = pca_2.transform(data[pca_numerical_columns_2])

#     # Ensure column order matches the model's expected input
#     expected_columns = [
#         'Marital_status', 'Application_mode', 'Application_order', 'Course',
#         'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
#         'Nacionality', 'Admission_grade', 'Displaced', 'Debtor', 'Educational_special_needs',
#         'GDP', 'Gender', 'Inflation_rate', 'International', 'Unemployment_rate',
#         'Age_at_enrollment', 'Scholarship_holder', 'Tuition_fees_up_to_date',
#         'pc1_1', 'pc1_2', 'pc1_3', 'pc1_4', 'pc2_1', 'pc2_2'
#     ]
#     df = df[expected_columns]

#     return df


import numpy as np
import pandas as pd
import joblib

# Load PCA models
pca_1 = joblib.load('model/pca_1.joblib')
pca_2 = joblib.load('model/pca_2.joblib')

# Load scalers
scalers = {
    'Admission_grade': joblib.load('model/scaler_Admission_grade.joblib'),
    'Age_at_enrollment': joblib.load('model/scaler_Age_at_enrollment.joblib'),
    'Application_mode': joblib.load('model/scaler_Application_mode.joblib'),
    'Application_order': joblib.load('model/scaler_Application_order.joblib'),
    'Course': joblib.load('model/scaler_Course.joblib'),
    'Daytime_evening_attendance': joblib.load('model/scaler_Daytime_evening_attendance.joblib'),
    'Debtor': joblib.load('model/scaler_Debtor.joblib'),
    'Displaced': joblib.load('model/scaler_Displaced.joblib'),
    'Educational_special_needs': joblib.load('model/scaler_Educational_special_needs.joblib'),
    'GDP': joblib.load('model/scaler_GDP.joblib'),
    'Gender': joblib.load('model/scaler_Gender.joblib'),
    'Inflation_rate': joblib.load('model/scaler_Inflation_rate.joblib'),
    'International': joblib.load('model/scaler_International.joblib'),
    'Marital_status': joblib.load('model/scaler_Marital_status.joblib'),
    'Nacionality': joblib.load('model/scaler_Nacionality.joblib'),
    'Previous_qualification_grade': joblib.load('model/scaler_Previous_qualification_grade.joblib'),
    'Previous_qualification': joblib.load('model/scaler_Previous_qualification.joblib'),
    'Scholarship_holder': joblib.load('model/scaler_Scholarship_holder.joblib'),
    'Tuition_fees_up_to_date': joblib.load('model/scaler_Tuition_fees_up_to_date.joblib'),
    'Unemployment_rate': joblib.load('model/scaler_Unemployment_rate.joblib')
}

# Define columns
pca_numerical_columns_1 = [
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_2nd_sem_without_evaluations'
]
pca_numerical_columns_2 = [
    'Mothers_qualification',
    'Fathers_qualification',
    'Mothers_occupation',
    'Fathers_occupation'
]
numeric_columns = [
    'Marital_status',
    'Application_mode',
    'Application_order',
    'Course',
    'Daytime_evening_attendance',
    'Previous_qualification',
    'Previous_qualification_grade',
    'Nacionality',
    'Admission_grade',
    'Displaced',
    'Educational_special_needs',
    'Debtor',
    'Tuition_fees_up_to_date',
    'Gender',
    'Scholarship_holder',
    'Age_at_enrollment',
    'International',
    'Unemployment_rate',
    'Inflation_rate',
    'GDP'
]

def data_preprocessing(data):
    """Preprocess the input data for prediction.

    Args:
        data (pd.DataFrame): Raw input data.

    Returns:
        pd.DataFrame: Preprocessed data ready for prediction.
    """
    data = data.copy()
    df = pd.DataFrame()

    # Apply scalers to numeric columns
    for col in numeric_columns:
        if col in data.columns:
            df[col] = scalers[col].transform(np.asarray(data[col]).reshape(-1, 1)).flatten()
        else:
            print(f"Warning: Column {col} is missing. Filling with 0.")
            df[col] = 0

    # Validate and handle missing PCA columns
    missing_columns_1 = [col for col in pca_numerical_columns_1 if col not in data.columns]
    missing_columns_2 = [col for col in pca_numerical_columns_2 if col not in data.columns]

    if missing_columns_1:
        print(f"Missing columns for PCA 1: {missing_columns_1}")
        for col in missing_columns_1:
            data[col] = 0

    if missing_columns_2:
        print(f"Missing columns for PCA 2: {missing_columns_2}")
        for col in missing_columns_2:
            data[col] = 0

    # Apply PCA
    df[['pc1_1', 'pc1_2', 'pc1_3', 'pc1_4']] = pca_1.transform(data[pca_numerical_columns_1])
    df[['pc2_1', 'pc2_2']] = pca_2.transform(data[pca_numerical_columns_2])

    # Ensure column order matches the model's expected input
    expected_columns = numeric_columns + ['pc1_1', 'pc1_2', 'pc1_3', 'pc1_4', 'pc2_1', 'pc2_2']
    df = df[expected_columns]

    return df