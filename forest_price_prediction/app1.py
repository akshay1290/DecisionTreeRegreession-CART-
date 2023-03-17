import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
from forest_fires_prediction import DecisionTreeRegressor
import streamlit as st 
model_file = 'model_C=1.0.bin'

from PIL import Image

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
pickle_in = open("regressor.pkl","rb")
regressor=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,
       wind,rain):
    
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
   
    prediction=regressor.predict([[X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain]])
    print(prediction)
    return prediction



def main():
    image = Image.open('images/icone.png')
    image2 = Image.open('images/image.png')
    st.image(image,use_column_width=False)
    
    st.sidebar.info('This app is created to predict FOREST FIRE')
    st.sidebar.image(image2)
    st.title("FOREST FIRE PREDICTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">FOREST FIRE PREDICTION </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    X = st.sidebar.slider("X", min_value=1, max_value=9, value=1)
    Y = st.sidebar.slider("Y", min_value=2, max_value=9, value=2)

    display1 = (["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"])
    options1= list(range(len(display1)))
    value1 = st.selectbox("month", options1, format_func=lambda x: display1[x])
    month =value1
    
    
    display3 = (["mon","tue","wed","thu","fri","sat","sun"])
    options3= list(range(len(display3)))
    value3 = st.selectbox("day", options3, format_func=lambda x: display3[x])
    day =value3
    
    FFMC = st.sidebar.slider("FFMC", min_value=18.7, max_value=96.20, value=50.0, step=0.1)
    DMC = st.sidebar.slider("DMC", min_value=1.1, max_value=291.3, value=50.0, step=0.1)
    DC = st.sidebar.slider("DC", min_value=7.9, max_value=860.6, value=50.0, step=0.1)
    ISI = st.sidebar.slider("ISI", min_value=0.0, max_value=56.10, value=50.0, step=0.1)
    temp = st.sidebar.slider("temp", min_value=2.2, max_value=33.30, value=20.0, step=0.1)
    RH = st.sidebar.slider("RH", min_value=15, max_value=100, value=50, step=1)
    wind = st.sidebar.slider("wind", min_value=0.4, max_value=9.4, value=3.0, step=0.1)
    rain = st.sidebar.slider("Rainfall", min_value=0.0, max_value=6.4, value=0.0, step=0.1)
    result=""
    if st.button("Predict"):
        X=float(X)
        Y=float(Y)
        month=float(month)
        day=float(day)
        FFMC=float(FFMC)
        DMC=float(DMC)
        DC=float(DC)
        ISI=float(ISI)
        temp=float(temp)
        RH=float(RH)
        wind=float(wind)
        rain=float(rain)
        result=predict_note_authentication(X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain)
    st.success('The output is {}'.format(result))


if __name__=='__main__':
    main()
    
    
    