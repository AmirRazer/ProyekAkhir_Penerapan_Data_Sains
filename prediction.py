import joblib

# Load model
model = joblib.load("model/gboost_model.joblib")

# Mapping for prediction results
status_mapping = {
    0: 'Dropout',
    1: 'Enrolled',
    2: 'Graduate'
}

def prediction(data):
    """Making prediction

    Args:
        data (Pandas DataFrame): Dataframe that contains all the preprocessed data

    Returns:
        str: Prediction result (Dropout, Enrolled, or Graduate)
    """
    result = model.predict(data)
    final_status = status_mapping[result[0]]  # Map the numerical result to its corresponding status
    return final_status