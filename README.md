

![Screenshot 2025-05-02 152748](https://github.com/user-attachments/assets/df1ec345-cf5a-49ed-9dd7-a7eeb0beff34)

![Screenshot 2025-05-02 152807](https://github.com/user-attachments/assets/6b494a41-d5bc-4c7a-8246-fcb8aa91c443)

![Screenshot 2025-05-02 152827](https://github.com/user-attachments/assets/ae177ea1-c551-4ff7-b7ce-4d1ed43c38e6)

![Screenshot 2025-05-02 152827](https://github.com/user-attachments/assets/092eb2e0-d05a-45d1-810d-4b08e08b41de)



📌 Project Summary
This project focuses on detecting fraudulent transactions in online payments using a Machine Learning classification model. It enables users to identify potentially fraudulent activities in real-time by analyzing key transaction features through an interactive Streamlit web application.

The model was built using the XGBoost Classifier and deployed using Streamlit, allowing easy and fast detection of fraud through a simple user interface.

📂 Dataset Details
Features used for prediction (examples – modify based on your dataset):

Transaction Amount

Old Balance (before transaction)

New Balance (after transaction)

Transaction Type (e.g., transfer, cash out)

Account Age

Customer Location

Transaction Time

Target Variable:

isFraud (1 = Fraudulent, 0 = Genuine)

🛠️ Technologies Used

Python

Streamlit (for deploying the web app)

XGBoost Classifier (for fraud detection)

Scikit-learn (for preprocessing and evaluation)

Pandas & NumPy (for data handling)

Joblib (for model serialization)

🛠️ Project Workflow

Data Cleaning & Preprocessing:

Removed missing/irrelevant values

Encoded categorical features (like transaction type)

Normalized numerical values

Feature Selection:

Selected most impactful features using correlation and domain knowledge

Model Training:

Trained an XGBoost Classifier due to its high accuracy and performance on imbalanced data

Model Evaluation:

Evaluated using Precision, Recall, F1-Score, and ROC-AUC

Model Saving:

Saved the trained model using Joblib

Web Application:

Built an interactive front-end with Streamlit for real-time fraud predictions

📈 Model Performance

The XGBoost model showed excellent performance with:

High Precision and Recall on fraud class

ROC-AUC Score: 0.98 (example)

F1-Score: 0.92 (example)

Handled class imbalance using SMOTE or class weighting
