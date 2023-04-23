import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split
red_wine=pd.read_csv(r"C:\Users\shiva\Downloads\red-wine.csv")
#df_train=red_wine[:-1]#.sample(frac=0.7,random_state=0)

x=np.array(red_wine[['fixed acidity', 'volatile acidity', 'citric acid',
       'chlorides', 'total sulfur dioxide','pH',
        'sulphates', 'alcohol']])
y=np.array(red_wine['quality'])
model=RandomForestClassifier()
model.fit(x,y)


# Code of Web application 
import streamlit as st
# # app heading
st.set_page_config(page_title="Implementation ", page_icon="\U0001F4CC")
st.write(""" # Wine Quality Prediction App
          This App is for predicting ***wines Quality***
          """)

# Creating sidebar for user input
st.sidebar.header("User Input Parameter")
def user_input():
    fixed_acidity=st.sidebar.slider('fixed acidity',4.6,15.9,8.32)
    volatile_acidity=st.sidebar.slider('volatile acidity',0.12,1.58,0.52)
    citric_acid=st.sidebar.slider('citric acid',0.0,1.0,0.27)
    chlorides=st.sidebar.slider('chlorides',0.01,0.61,0.08)
    total_sulfur_dioxide=st.sidebar.slider('total sulfur dioxide',6.0,289.0,46.47)
    pH=st.sidebar.slider('pH',2.74,4.01,3.31)
    sulphates=st.sidebar.slider('sulphates',0.33,2.0,0.66)
    alcohol=st.sidebar.slider('alcohol',8.4,14.9,10.42)
    data={"fixed_acidity":fixed_acidity,
          "volatile_acidity":volatile_acidity,
          "citric_acid":citric_acid,
          "chlorides":chlorides,
          "total_sulfur_dioxide":total_sulfur_dioxide,
          "pH":pH,
          "sulphates":sulphates,
          "alcohol":alcohol
        }
    features=pd.DataFrame(data,index=[0])
    return features
df=user_input()

st.subheader('User Input Parameters')
st.write(df)

st.subheader("Wine quality labels and their indes")
st.write(pd.DataFrame({
    'Wine Quality': [3,4,5,6,7,8]
}))
prediction=model.predict(df)
prediction_probability=model.predict_proba(df)
pred_sco=model.score(x,y,sample_weight=None)
st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_probability)



# x = st.button('x')  #  this is a widget
# st.write(x, 'squared is', x * x)

# st.subheader('Predictions Score')
# st.write(pred_sco)

#print(x_train.columns)