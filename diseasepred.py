# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 16:19:27 2023

@author: Sidd
"""
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Set page configuration
st.set_page_config(page_title="Medical Care Navigator",
                   layout="wide",
                   page_icon="🧑‍⚕️")


    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/Sidd/Desktop/diseasepredictionproject/saved models/diabetes_model (1).sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/Sidd/Desktop/diseasepredictionproject/saved models/heart_disease_model (1).sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/Sidd/Desktop/diseasepredictionproject/saved models/parkinsons_model (1).sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/Sidd/Desktop/diseasepredictionproject/saved models/breastcancer.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    # Add custom CSS for sidebar background color
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: crimson;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    selected = option_menu(' Diagno Sure  Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast-Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart-pulse', 'person', 'bag-plus'],
                           default_index=0)



# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
            # Provide tips for managing diabetes
            st.write("Here are some tips to manage diabetes:")
            st.write("- Follow a healthy diet rich in fruits, vegetables, and whole grains.")
            st.write("- Exercise regularly to help control blood sugar levels.")
            st.write("- Monitor blood sugar levels regularly as advised by your healthcare provider.")

        else:
            diab_diagnosis = 'The person is not diabetic'
            st.write("Here are some tips to prevent diabetes:")
            st.write("- Maintain a healthy weight.")
            st.write("- Be physically active.")
            st.write("- Eat a balanced diet.")

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            # Provide tips for managing heart disease
            st.write("Here are some tips to manage heart disease:")
            st.write("- Follow a heart-healthy diet low in saturated and trans fats.")
            st.write("- Engage in regular physical activity.")
            st.write("- Take medications as prescribed by your doctor.")
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            # Provide tips for maintaining heart health
            st.write("Here are some tips to maintain heart health:")
            st.write("- Eat a balanced diet rich in fruits, vegetables, and whole grains.")
            st.write("- Exercise regularly to keep your heart strong.")
            st.write("- Avoid smoking and excessive alcohol consumption.")

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
            # Provide tips for managing Parkinson's disease
            st.write("Here are some tips to manage Parkinson's disease:")
            st.write("- Engage in regular physical therapy and exercise.")
            st.write("- Follow a balanced diet and stay hydrated.")
            st.write("- Take medications as prescribed by your doctor.")
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            # Provide tips for promoting brain health
            st.write("Here are some tips to promote brain health:")
            st.write("- Stay mentally active with puzzles, reading, or learning new skills.")
            st.write("- Exercise regularly to improve blood flow to the brain.")
            st.write("- Get plenty of sleep to support brain function.")

    st.success(parkinsons_diagnosis)
    
    # Breast-cancer Prediction Page
    '''if selected == "Breast-Cancer Prediction":

        # page title
        st.title("Breast-Cancer Prediction Prediction ")

        col1, col2, col3, col4, col5 = st.columns(5)
        

    with col1:
        radius_mean = st.text_input('Radius Mean')

    with col2:
        texture_mean = st.text_input('Texture Mean')

    with col3:
        perimeter_mean = st.text_input('Perimeter Mean')

    with col4:
        area_mean = st.text_input('Area Mean')

    with col5:
        smoothness_mean = st.text_input('Smoothness Mean')

    with col1:
        compactness_mean = st.text_input('Compactness Mean')

    with col2:
        concavity_mean = st.text_input('Concavity Mean')

    with col3:
        concave_points_mean = st.text_input('Concave Points Mean')

    with col4:
        symmetry_mean = st.text_input('Symmetry Mean')

    with col5:
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean')

    with col1:
        radius_se = st.text_input('Radius SE')

    with col2:
        texture_se = st.text_input('Texture SE')

    with col3:
        perimeter_se = st.text_input('Perimeter SE')

    with col4:
        area_se = st.text_input('Area SE')

    with col5:
        smoothness_se = st.text_input('Smoothness SE')

    with col1:
        compactness_se = st.text_input('Compactness SE')

    with col2:
        concavity_se = st.text_input('Concavity SE')

    with col3:
        concave_points_se = st.text_input('Concave Points SE')

    with col4:
        symmetry_se = st.text_input('Symmetry SE')

    with col5:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')

    with col1:
        radius_worst = st.text_input('Radius Worst')

    with col2:
        texture_worst = st.text_input('Texture Worst')

    with col3:
        perimeter_worst = st.text_input('Perimeter Worst')

    with col4:
        area_worst = st.text_input('Area Worst')

    with col5:
        smoothness_worst = st.text_input('Smoothness Worst')

    with col1:
        compactness_worst = st.text_input('Compactness Worst')

    with col2:
        concavity_worst = st.text_input('Concavity Worst')

    with col3:
        concave_points_worst = st.text_input('Concave Points Worst')

    with col4:
        symmetry_worst = st.text_input('Symmetry Worst')

    with col5:
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst')


        # code for Prediction
        breast_cancer_diagnosis = ''

         
        if st.button('Breast Cancer Test Result'):

            user_input = [radius_mean, texture_mean, perimeter_mean,
                      area_mean, smoothness_mean, compactness_mean,
                      concavity_mean, concave_points_mean, symmetry_mean,
                      fractal_dimension_mean, radius_se, texture_se,
                      perimeter_se, area_se, smoothness_se,
                      compactness_se, concavity_se, concave_points_se,
                      symmetry_se, fractal_dimension_se, radius_worst,
                      texture_worst, perimeter_worst, area_worst,
                      smoothness_worst, compactness_worst, concavity_worst,
                      concave_points_worst, symmetry_worst,
                      fractal_dimension_worst]

            user_input = [float(x) for x in user_input]
        

        breast_cancer_prediction = breastcancer_model.predict([user_input])

        if breast_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = 'The tumor is malignant'
        else:
            breast_cancer_diagnosis = 'The tumor is benign'

    st.success(breast_cancer_diagnosis)'''