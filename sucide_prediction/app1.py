import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from suicide_prevention import DecisionTreeRegressor
model_file = 'model_C=1.0.bin'

from PIL import Image

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
pickle_in = open("regressor.pkl","rb")
regressor=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(gdp_per_capita,year,sex,age,suicides_no,population):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=regressor.predict([[gdp_per_capita,year,sex,age,suicides_no,population]])
    print(prediction)
    return prediction



def main():
    image = Image.open('images/icone.png')
    image2 = Image.open('images/image.png')
    st.image(image,use_column_width=False)
    st.sidebar.info('This app is created to predict SUCIDE NUMBER PREDICTION')
    st.sidebar.image(image2)
    st.title("SUCIDE NUMBER PREDICTION PREDICTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">SUCIDE NUMBER PREDICTION PREDICTION </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    gdp_per_capita = st.number_input('GDP per Capita', min_value=0, max_value=100000, value=10000)
    year = st.slider('Year', min_value=1985, max_value=2016, value=2016)

    display2 = (['Male', 'Female'])
    options5= list(range(len(display2)))
    value5 = st.radio("sex", options5, format_func=lambda x: display2[x])
    sex = value5
   
    age = st.number_input('age', min_value=0, max_value=100, value=75)
    suicides_no = st.number_input('suicides_no', min_value=0, max_value=1000000000, value=100000)
    population =st.number_input('Population', min_value=0, max_value=1000000000, value=100000)
   

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(gdp_per_capita,year,sex,age,suicides_no,population)
    st.success('The output is {}'.format(result))


if __name__=='__main__':
    main()
    
    
    