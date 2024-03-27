
import streamlit as st
from streamlit_extras import add_vertical_space
import streamlit.components.v1 as components
from annotated_text import annotated_text


#st.set_page_config(layout='wide')

import pandas as pd

import json



with st.sidebar:
    st.title("Onsite Health Diagnostics-OHD")
    

    diseases = ["Diabetes Prediction","Breast Cancer","Performance Measures","Prediction"]

    


    selected_diseases = st.selectbox("Select Diseases to Predict", diseases)


    
if selected_diseases == "Diabetes Prediction":
    
    st.title("DIABETES PREDICTION")
    
    # Input fields for user to input data
    pregnancies = st.number_input("Number of Pregnancies", 0, 17, 1)
    glucose = st.number_input("Plasma Glucose Concentration (mg/dL)", 0, 200, 100)
    blood_pressure = st.number_input("Diastolic Blood Pressure (mm Hg)", 0, 122, 70)
    skin_thickness = st.number_input("Skin Thickness (mm)", 0, 99, 20)
    insulin = st.number_input("Insulin Level (mu U/mL)", 0, 846, 79)
    bmi = st.number_input("Body Mass Index (BMI)", 0.0, 67.1, 30.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.078, 2.42, 0.3725)
    age = st.number_input("Age (years)", 21, 81, 25)




if selected_diseases == "Breast Cancer":
    
    st.title("BREAST CANCER PREDICTION")
    
    # Input fields for user to input data
    radius_mean = st.number_input("Radius Mean", 6.981, 28.11, 14.127)
    area_mean = st.number_input("Area Mean", 143.5, 2501.0, 654.889)
    compactness_mean = st.number_input("Compactness Mean", 0.019, 0.345, 0.104)
    concavity_mean = st.number_input("Concavity Mean", 0.0, 0.427, 0.089)
    concave_points_mean = st.number_input("Concave Points Mean", 0.0, 0.201, 0.049)
    area_worst = st.number_input("Area Worst", 185.200000, value=686.500000)
    compactness_worst = st.number_input("Compactness Worst",0.027290, value=0.211900)
    concavity_worst = st.number_input("Concavity Worst",0.000000, value=0.226700)
    area_se = st.number_input("Area Se", 6.802000, value=24.530000)
    fractal_dimension_se = st.number_input("Fractal Dimension Mean", 0.05, 0.097, 0.062)
    symmetry_worst = st.number_input("Symmetry Worst", 0.106, 0.304, 0.181)
    fractal_dimension_worst = st.number_input("Fractal_Dimension_Worst", 0.055040, value=0.080040)



