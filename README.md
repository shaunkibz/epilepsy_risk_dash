> **⚠️ DISCLAIMER:** This dashboard is for **educational purposes only**. It uses simulated data and does not provide medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for any medical concerns.

# Epilepsy Seizure Risk Dashboard

A Streamlit-based dashboard to simulate seizure risk using patient metrics for educational and social-impact purposes.

## Project Overview

Epilepsy affects millions of people worldwide, with limited early monitoring tools, especially in low-resource settings. This dashboard allows users to input daily lifestyle and health metrics (such as sleep hours, stress levels, missed medication, alcohol intake, screen time, and physical activity) to estimate the simulated risk of a seizure using a trained Random Forest model.

The project is designed to help users visualize potential triggers, understand risk factors, and demonstrate the application of machine learning in healthcare contexts.

## Features

* **Interactive Sidebar:** Seamless input mechanism for patient metrics.
* **Real-time Risk Calculation:** Immediate risk inference using a Random Forest classifier.
* **Probability-based Categorization:** Translates raw probabilities into Low, Moderate, or High risk buckets.
* **Visual Feedback:** Clear, color-coded dashboard output in the main panel.
* **Cross-platform Compatibility:** Accessible via Streamlit's web interface.

## Dataset & Methodology

The project uses a simulated dataset generated specifically for educational modeling.

* **Age (int):** Patient age in years
* **Sleep_Hours (float):** Sleep in the last 24 hours
* **Stress_Level (int):** Self-reported stress (1-10)
* **Temperature_C (float):** Body temperature in Celsius
* **Missed_Medication (bool):** Whether the patient missed medication
* **Alcohol_Intake (bool):** Alcohol consumption today
* **Screen_Time_Hours (float):** Daily screen time in hours
* **Physical_Activity_Hours_Per_Week (float):** Weekly physical activity in hours
* **Seizure (int):** Target variable (0 = No seizure, 1 = Seizure)

## Tech Stack

* **Frontend:** Streamlit (Interactive dashboard user interface)
* **Backend:** Python (Core programming language)
* **Machine Learning:** scikit-learn (Random Forest classifier)
* **Data Handling:** pandas, numpy (Data preprocessing and calculations)
* **Model Storage:** joblib (Save and load trained model)
* **Environment:** venv (Isolated Python environment)

## Architecture / Workflow

1. User Inputs via Streamlit UI
2. Input Features converted to DataFrame
3. Processed by Random Forest Model
4. Risk Probability Calculated
5. Risk Categorization (Low/Moderate/High)
6. Dashboard Output Displayed

## Model Evaluation

*(Note to developer: You must replace these placeholders with your actual model metrics prior to publishing.)*

* **Accuracy:** `[Insert %]`
* **Precision:** `[Insert %]`
* **Recall:** `[Insert %]`
* **F1-Score:** `[Insert %]`

## Installation

Clone the repository:
```bash
git clone [https://github.com/shaunkibz/epilepsy-risk-dashboard.git](https://github.com/shaunkibz/epilepsy-risk-dashboard.git)
cd epilepsy-risk-dashboard
