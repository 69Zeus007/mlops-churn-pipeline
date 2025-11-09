---
title: Mlops Churn Api
emoji: 🦀
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: mit
thumbnail: >-
  https://cdn-uploads.huggingface.co/production/uploads/690dab0636f9e9b8d3632f40/51uEaW77l3O_eVoGY8QL5.png
---
# Churn Prediction Demo

This Space showcases a machine learning model that predicts customer churn based on user input. It’s built with Scikit-learn and deployed using Gradio on Hugging Face Spaces.

## How It Works
Enter customer details:
- Tenure (months)
- Monthly Charges
- Total Charges

Click **Submit** to get a prediction: `Churn` or `No Churn`.
## What Does “Churn” Mean?

- **Churn**: The customer is predicted to leave the service (e.g., cancel subscription, stop using).
- **No Churn**: The customer is predicted to stay.

This prediction helps businesses proactively retain customers and reduce revenue loss.

## Tech Stack
- Python
- Scikit-learn
- Gradio
- Hugging Face Spaces

## Model Details
- Trained on synthetic or anonymized customer data
- Uses random forest classifier 
- Saved as `churn_model.pkl` and loaded at runtime

## Purpose
This project is part of my ML Engineering portfolio, demonstrating:
- End-to-end model deployment
- CI/CD integration (via GitHub Actions)
- Cloud hosting and UI design(working on UI Design)

## Author
Created by [69Zeus007](https://huggingface.co/69Zeus007)   
Check out more projects on [GitHub](https://github.com/69Zeus007)

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference