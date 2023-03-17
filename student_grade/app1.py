import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from studentgrade import DecisionTreeRegressor
model_file = 'model_C=1.0.bin'

from PIL import Image

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
pickle_in = open("regressor.pkl","rb")
regressor=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(age,Medu,Fedu,traveltime,studytime,failures,schoolsup,famsup,paid,activities,nursery,internet,romantic,famrel,freetime,goout,absences,prev_grade,sex):
    

   
    prediction=regressor.predict([[age,Medu,Fedu,traveltime,studytime,failures,schoolsup,famsup,paid,activities,nursery,internet,romantic,famrel,freetime,goout,absences,prev_grade,sex]])
    print(prediction)
    return prediction



def main():
    image = Image.open('images/icone.png')
    image2 = Image.open('images/image.png')
    st.image(image,use_column_width=False)

    st.sidebar.info('This app is created to predict STUDENT PERFORMENCE')
    st.sidebar.image(image2)
    st.title("STUDENT PERFORMENCE PREDICTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">STUDENT PERFORMENCE PREDICTION </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.slider('age', min_value=15, max_value=22, step=1, value=18)

    display13 = (['none','primary education 4th grade','5th to 9th grade','secondary education','higher education'])
    options13= list(range(len(display13)))
    value13 = st.selectbox("Medu", options13, format_func=lambda x: display13[x])
    Medu =value13
    
    display12 = (['none','primary education 4th grade','5th to 9th grade','secondary education','higher education'])
    options12= list(range(len(display12)))
    value12 = st.selectbox("Fedu", options12, format_func=lambda x: display12[x])
    Fedu =value12
    

    display11 = (["Any", "<15 min.", "15 to 30 min.", "30 min. to 1 hour", ">1 hour"])
    options11 = list(range(len(display11)))
    value11 = st.selectbox("traveltime", options11, format_func=lambda x: display11[x])
    traveltime =value11

    display10 = (["Any", "<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"])
    options10= list(range(len(display10)))
    value10 = st.selectbox("studytime", options10, format_func=lambda x: display10[x])
    studytime =value10
    

    display9 = (["Any", "0", "1", "2", "3 or more"])
    options9= list(range(len(display9)))
    value9 = st.selectbox("failures", options9, format_func=lambda x: display9[x])
    failures =value9
    

    display8 = (['YES', 'NO'])
    options8= list(range(len(display8)))
    value8 = st.selectbox("schoolsup", options8, format_func=lambda x: display8[x])
    schoolsup =value8
    

    display7 = (['YES', 'NO'])
    options7= list(range(len(display7)))
    value7 = st.selectbox("famsup", options7, format_func=lambda x: display7[x])
    famsup =value7
   

    display6 = (['YES', 'NO'])
    options6= list(range(len(display6)))
    value6 = st.radio("paid", options6, format_func=lambda x: display6[x])
    paid =value6

    

    display1 = (['YES', 'NO'])
    options1= list(range(len(display1)))
    value1 = st.selectbox("activities", options1, format_func=lambda x: display1[x])
    activities =value1
    

    display3 = (['YES', 'NO'])
    options3= list(range(len(display3)))
    value3 = st.selectbox("nursery", options3, format_func=lambda x: display3[x])
    nursery =value3
    
  

    display4 = (['YES', 'NO'])
    options4= list(range(len(display4)))
    value4 = st.selectbox("internet", options4, format_func=lambda x: display4[x])
    internet =value4
    

    display2 = (['YES', 'NO'])
    options5= list(range(len(display2)))
    value5 = st.selectbox("romantic", options5, format_func=lambda x: display2[x])
    romantic =value5

    famrel = st.slider('famrel', min_value=0, max_value=5, step=1, value=3)
    freetime = st.slider('freetime', min_value=0, max_value=5, step=1, value=3)
    goout = st.slider('goout', min_value=0, max_value=5, step=1, value=3)
    
    absences = st.slider('absences', min_value=0, max_value=93, step=1, value=30)
    prev_grade = st.slider('prev_grade', min_value=0, max_value=30, step=1, value=15)
    
    display15 = (['Male', 'Female'])
    options15= list(range(len(display15)))
    value15 = st.radio("sex", options15, format_func=lambda x: display15[x])
    sex =value15

    result=""
    if st.button("Predict"):
       
        result=predict_note_authentication(age,Medu,Fedu,traveltime,studytime,failures,schoolsup,famsup,paid,activities,nursery,internet,romantic,famrel,freetime,goout,absences,prev_grade,sex)
    st.success('The output is {}'.format(result))


if __name__=='__main__':
    main()
    
    
    