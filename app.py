import streamlit as st
import pandas as pd
import joblib

# Load model
try:
    model = joblib.load('fraud_detection_model.pkl')
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Model loading failed: {str(e)}")
    st.stop()

# All possible categories (update these lists if your dataset has more)
ALL_LOCATIONS = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 
     
 'San Francisco', 'Boston','Seattle','Miami'
]

ALL_TRANSACTION_TYPES = [
    'Bank Transfer', 'Bill Payment', 'Online Purchase',
    'POS Payment', 'ATM Withdrawal'
]

ALL_PAYMENT_METHODS = [
    'Debit Card', 'Credit Card', 'Net Banking',
    'UPI', 'Invalid Method'
]

ALL_DEVICES = ['Mobile', 'Tablet', 'Desktop', 'Unknown']

def main():
    st.title('💰 Fraud Detection System')
    st.write("Predicts fraudulent transactions using machine learning")

    with st.form("transaction_form"):
        # --- Numerical Inputs ---
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=50.0, step=0.01)
            time = st.slider("Time of Transaction (Hour)", 0, 23, 12)
            prev_fraud = st.number_input("Previous Fraudulent Transactions", min_value=0, value=0)
        
        with col2:
            age = st.number_input("Account Age (Days)", min_value=0, value=100)
            last_24h = st.number_input("Transactions in Last 24 Hours", min_value=0, value=3)
            device = st.selectbox("Device Used", ALL_DEVICES)

        # --- Categorical Inputs ---
        transaction_type = st.selectbox("Transaction Type", ALL_TRANSACTION_TYPES)
        location = st.selectbox("Location", ALL_LOCATIONS)
        payment_method = st.selectbox("Payment Method", ALL_PAYMENT_METHODS)

        submitted = st.form_submit_button("Predict Fraud Risk")

    if submitted:
        try:
            # Initialize all possible features to 0
            features = {
                'Transaction_Amount': amount,
                'Time_of_Transaction': time,
                'Previous_Fraudulent_Transactions': prev_fraud,
                'Account_Age': age,
                'Number_of_Transactions_Last_24H': last_24h,
                # Device
                'Device_Used_Mobile': 1 if device == 'Mobile' else 0,
                'Device_Used_Tablet': 1 if device == 'Tablet' else 0,
                'Device_Used_Desktop': 1 if device == 'Desktop' else 0,
                # Transaction Types
                'Transaction_Type_Bank Transfer': 1 if transaction_type == 'Bank Transfer' else 0,
                'Transaction_Type_Bill Payment': 1 if transaction_type == 'Bill Payment' else 0,
                'Transaction_Type_Online Purchase': 1 if transaction_type == 'Online Purchase' else 0,
                'Transaction_Type_POS Payment': 1 if transaction_type == 'POS Payment' else 0,
                'Transaction_Type_ATM Withdrawal': 1 if transaction_type == 'ATM Withdrawal' else 0,
                
                # Locations (example for 3 cities - add all you need)
                'Location_New York': 1 if location == 'New York' else 0,
                'Location_Los Angeles': 1 if location == 'Los Angeles' else 0,
                'Location_Chicago': 1 if location == 'Chicago' else 0,
                # Payment Methods
                'Payment_Method_Debit Card': 1 if payment_method == 'Debit Card' else 0,
                'Payment_Method_Credit Card': 1 if payment_method == 'Credit Card' else 0,
                'Payment_Method_Net Banking': 1 if payment_method == 'Net Banking' else 0,
                'Payment_Method_UPI': 1 if payment_method == 'UPI' else 0,
                
            }

            # Convert to DataFrame with model's expected features
            input_df = pd.DataFrame([features])
            
            # Ensure we only keep features the model was trained on
            model_features = model.feature_names_in_
            input_df = input_df.reindex(columns=model_features, fill_value=0)

            # Predict
            proba = model.predict_proba(input_df)[0]
            
            # Display results
            st.subheader("Results")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Legitimate", f"{proba[0]:.1%}")
            with col2:
                st.metric("Fraudulent", f"{proba[1]:.1%}", delta_color="inverse")
            
            # Visual indicator
            if proba[1] > 0.7:
                st.error("🚨 High fraud risk detected!")
            elif proba[1] > 0.3:
                st.warning("⚠️ Moderate fraud risk")
            else:
                st.success("✅ Low fraud risk")

        except Exception as e:
            st.error(f"❌ Prediction error: {str(e)}")
            st.write("Model expects these features:", model.feature_names_in_)

if __name__ == '__main__':
    main()