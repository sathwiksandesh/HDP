import streamlit as st
import joblib
st.title('Heart Disease Prediction')
model= joblib.load('hdp.joblib')
age= st.number_input('Enter your age:')
cigsperday= st.number_input('Enter no.of cigarettes you consume per day:')
totchol=st.number_input("Enter Cholesterol level in Blood:")
sysBP=st.number_input('Enter Systolic Blood Pressure:')
diaBP=st.number_input('Enter Diastolic Blood Pressure:')
BMI=st.number_input('Enter Body Mass Index:')
heartRate=st.number_input('Enter Resting Heart Rate:')
glucose=st.number_input('Enter Glucose levels:')
if st.button('Predict Disease'):
    prediction=model.predict([[age,cigsperday,totchol,sysBP,diaBP,BMI,heartRate,glucose]])
    if prediction==1:
        st.text('May be there is a Heart Disease')
    else:
        st.text("Don't have Heart Disease")
