import numpy as np
import pickle
import pandas as pd
from googleplaystore import DecisionTreeRegressor
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


def predict_note_authentication(Reviews,Genres,Current_Ver,Android_Ver,App,Category,Rating,Size,Installs,Type):
   
   
    prediction=regressor.predict([[Reviews,Genres,Current_Ver,Android_Ver,App,Category,Rating,Size,Installs,Type]])
    print(prediction)
    return prediction



def main():
    image = Image.open('images/icone.png')
    image2 = Image.open('images/image.png')
    st.image(image,use_column_width=False)

    st.sidebar.info('This app is created to predict GOOGLE PLAY STORE PRICE')
    st.sidebar.image(image2)
    st.title("GOOGLE PLAY STORE PRICE PREDICTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">GOOGLE PLAY STORE PRICE PREDICTION </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Reviews = st.number_input('Reviews', min_value=0, value=1000)
    Genres = st.text_input("Genres","Type Here")
    Current_Ver = st.text_input("Current_Ver","Type Here")
    Android_Ver = st.text_input("Android_Ver","Type Here")
    App = st.text_input("App","Type Here")

    display1 = (['ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 'BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FINANCE', 'FOOD_AND_DRINK', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'MAPS_AND_NAVIGATION', 'MEDICAL', 'NEWS_AND_MAGAZINES', 'PARENTING', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING', 'SOCIAL', 'SPORTS', 'TOOLS', 'TRAVEL_AND_LOCAL', 'VIDEO_PLAYERS', 'WEATHER'])
    options1= list(range(len(display1)))
    value1 = st.selectbox("Category", options1, format_func=lambda x: display1[x])
    Category = value1

    Rating =st.slider('Rating', min_value=0.0, max_value=5.0, step=0.1, value=4.0)
    Size = st.number_input('Size', min_value=0.0, value=50.0, step=0.1)
    Installs = st.slider('Installs', min_value=0, max_value=1000000000, step=1000000, value=1000000)
   
    display2 = (['Free', 'Paid'])
    options5= list(range(len(display2)))
    value5 = st.radio("Type", options5, format_func=lambda x: display2[x])
    Type = value5
   
    result=""
    if st.button("Predict"):
        Reviews=float(Reviews)
        Genres=float(Genres)
        Current_Ver=float(Current_Ver)
        Android_Ver=float(Android_Ver)
        App=float(App)
        Category=float(Category)
        Rating=float(Rating)
        Size=float(Size)
        Installs=float(Installs)
        Type=float(Type)
       
        result=predict_note_authentication(Reviews,Genres,Current_Ver,Android_Ver,App,Category,Rating,Size,Installs,Type)
    st.success('The output is {}'.format(result))


if __name__=='__main__':
    main()
    
    
    