import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
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


def predict_note_authentication(sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,bedrooms,bathrooms,sqft_living,
                                   sqft_lot,floors,view,condition,grade):
    
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
   
    prediction=regressor.predict([[sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,bedrooms,bathrooms,sqft_living,
                                   sqft_lot,floors,view,condition,grade]])
      
      
    print(prediction)
    return prediction



def main():
    image = Image.open('images/icone.png')
    image2 = Image.open('images/image.png')
    st.image(image,use_column_width=False)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict House Price')
    st.sidebar.image(image2)
    st.title("HOUSE PRICE PREDICTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">House Price PREDICTION </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    sqft_basement = st.text_input("sqft_basement","Type Here")
    yr_built = st.text_input("yr_built","Type Here")
    yr_renovated = st.text_input("yr_renovated","Type Here")
    zipcode = st.text_input("zipcode","Type Here")
    lat = st.text_input("lat","Type Here")
    long = st.text_input("long","Type Here")
    sqft_living15 = st.text_input("sqft_living15","Type Here")
    bedrooms = st.text_input("bedrooms","Type Here")
    bathrooms = st.text_input("bathrooms","Type Here")
    sqft_living = st.text_input("sqft_living","Type Here")
    sqft_lot = st.text_input("sqft_lot","Type Here")
    floors = st.text_input("floors","Type Here")
    view = st.text_input("view","Type Here")
    condition = st.text_input("condition","Type Here")
    grade = st.text_input("grade","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,bedrooms,bathrooms,sqft_living,sqft_lot,floors,view,condition,grade)
    st.success('The output is {}'.format(result))


if __name__=='__main__':
    main()
    
    
    