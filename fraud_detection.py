##Imports the Streamlit library, which is used for building web applications in Python.
import streamlit as st 

import pandas as pd 

##Imports the Joblib library, which is used for loading and saving Python objects, especially machine learning models.
import joblib 

##Loads a pre-trained machine learning model from a file named fraud_detection_pipeline.pkl using Joblib.
model= joblib.load('fraud_detection_pipeline.pkl')


##Sets the title of the web application to "Fraud Detection Prediction App".
st.title("Fraud Detection Prediction App")

##Displays a markdown text prompting the user to enter transaction details and use the predict button.
st.markdown("Please enter the transaction details and uses the predict button:")

##Adds a visual divider in the app layout to separate sections for better readability.
st.divider()


##Creates a dropdown menu (select box) for the user to choose the type of transaction, with options: CASH_OUT, TRANSFER, DEPOSIT, and PAYMENT.
transaction_type = st.selectbox("Transaction Type", ["CASH_OUT", "TRANSFER", "DEPOSIT", "PAYMENT"])


amount = st.number_input("Amount", min_value=0.0,value= 1000.0)
oldbalanceOrg = st.number_input("Old Balance(Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance(Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance(Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance(Receiver)", min_value=0.0, value=0.0)


##Creates a button labeled "Predict". When clicked, the following code block will execute.
if st.button("Predict"):
    input_data = pd.DataFrame([{
        'type': transaction_type,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest
    }])
    
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'" )

    if prediction == 1:
        st.error("This transaction is likely to be fraudulent.")
    else:
        st.success("This transaction is likely to be legitimate.")