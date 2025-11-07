import gradio as gr
import joblib
import numpy as np

model = joblib.load("models/churn_model.pkl")

def predict_churn(tenure, monthly_charges, total_charges):
    features = np.array([[tenure, monthly_charges, total_charges]])
    prediction = model.predict(features)[0]
    return "Churn" if prediction == 1 else "No Churn"

demo = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Number(label="Tenure"),
        gr.Number(label="Monthly Charges"),
        gr.Number(label="Total Charges")
    ],
    outputs="text",
    title="Churn Prediction Demo",
    description="Enter customer details to predict churn using a trained ML model"
)

demo.launch()