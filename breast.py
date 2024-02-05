# -*- coding: utf-8 -*-


import pickle
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

breast_model = load_model(open('breast_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Breast_Cancer_Classificaton Prediction System',
                          
                          ['Breast_Cancer_Classificaton'],
                          icons=['person'],
                          default_index=0)
    
# Breast Cancer Classification Prediction Page
if (selected == "Breast_Cancer_Classificaton"):
    
    # page title
    st.title("Breast Cancer Classification with Neural Network")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        mean_radius = st.text_input('mean radius')
        
    with col2:
        mean_texture = st.text_input('mean texture')
        
    with col3:
         mean_perimeter = st.text_input('mean perimeter')
        
    with col4:
         mean_area = st.text_input('mean area')
        
    with col5:
         mean_smoothness = st.text_input('mean smoothness')
        
    with col1:
         mean_compactness = st.text_input('mean compactness')
        
    with col2:
      mean_concavity = st.text_input('mean concavity')
        
    with col3:
         mean_concave_points = st.text_input('mean concave points')
        
    with col4:
         mean_symmetry = st.text_input('mean symmetry')
        
    with col5:
         mean_fractal_dimension = st.text_input('mean fractal dimension')
        
    with col1:
        texture_error = st.text_input('texture error')
        
    with col2:
        perimeter_error = st.text_input('perimeter error')
        
    with col3:
       area_error = st.text_input('area error')
        
    with col4:
        smoothness_error = st.text_input('smoothness error')
        
    with col5:
        compactness_error = st.text_input('compactness error')
        
    with col1:
        concavity_error = st.text_input('concavity error')
        
    with col2:
        concave_points_error = st.text_input('concave points error')
        
    with col3:
        symmetry_error= st.text_input('symmetry error')
        
    with col4:
        fractal_dimension_error = st.text_input('fractal dimension error')
        
    with col5:
        worst_radius = st.text_input('worst radius')
        
    with col1:
        worst_texture = st.text_input('worst texture')
        
    with col2:
        worst_perimeter = st.text_input('worst perimeter')
    
    with col3:
        worst_area = st.text_input('worst area')
        
    with col4:
        worst_smoothness = st.text_input('worst smoothness')
        
    with col5:
        worst_compactness = st.text_input('worst compactness')
        
    with col1:
        worst_concavity = st.text_input('worst concavity')
        
    with col2:
        worst_concave_points = st.text_input('worst concave points')
        
    with col3:
        worst_symmetry= st.text_input('worst symmetry')
        
    with col4:
        worst_fractal_dimension = st.text_input('worst fractal dimension')
        
    
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("breast_cancer_Classification Test Result"):
        breast_cancer_prediction = breast_model.predict([[ mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness,mean_concavity,mean_concave_points,mean_symmetry, mean_fractal_dimension,texture_error, perimeter_error,area_error, smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius, worst_texture,worst_perimeter, worst_area , worst_smoothness ,worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]])                          
        
        if (breast_cancer_prediction[0] == 0):
          breast_cancer_diagnosis = "This tumor is Malignant"
        else:
          breast_cancer_diagnosis = "This tumor is Benign"
        
    st.success(breast_cancer_diagnosis)

