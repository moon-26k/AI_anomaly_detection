import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

st.title("AI-Based Anomaly Detection Platform")

# 1. Data Upload
uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.write(data.head())

    # 2. Data Preprocessing (Selecting numeric columns only)
    numeric_data = data.select_dtypes(include=['int64', 'float64'])

    if not numeric_data.empty:
        # 3. Model Training
        # Contamination is the expected % of outliers (0.05 = 5%)
        model = IsolationForest(contamination=0.05, random_state=42)
        data['anomaly_score'] = model.fit_predict(numeric_data)

        # In Isolation Forest: -1 is an anomaly, 1 is normal
        data['is_anomaly'] = data['anomaly_score'].apply(lambda x: 'Yes' if x == -1 else 'No')

        # 4. Results Display
        st.subheader("Detection Results")
        st.write(data)

        anomalies = data[data['anomaly_score'] == -1]
        st.error(f"Detected {len(anomalies)} anomalies in the dataset.")
        st.write(anomalies)
    else:
        st.warning("Please upload a dataset with numeric columns.")