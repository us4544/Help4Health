import streamlit as st

import pandas as pd
import numpy as np

from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

html_temp = '''
    <div style = "background-color: rgba(25,25,112,0.06); padding-bottom: 30px; padding-top: 20px; padding-left: 5px; padding-right: 5px">
    <center><h1>Boston Housing Prices</h1></center>
    
    </div>
    '''
st.markdown(html_temp, unsafe_allow_html=True)

st.sidebar.header('Enter Features for Prediction')
heartrate  = st.sidebar.slider('Per capita crime rate by town: ',1,-10,10)
handTemperature  = st .slider('Proportion of residential land zoned for lots over 25,000 sq.ft: ')
handAcc16_1 = st.sidebar.slider('Proportion of non-retail business acres per town: ')
handAcc6_1 = st.sidebar.slider('Charles River dummy variable: ',(0,1))
handGyro1 = st.sidebar.slider('Nitric oxides concentration (parts per 10 million): ')
handMagne1 = st.sidebar.slider('Average number of rooms per dwelling: ')
chestTemperature = st.sidebar.slider('Proportion of owner-occupied units built prior to 1940: ',1,100,20)
chestAcc16_1 = st.sidebar.slider('Weighted distances to five Boston employment centres: ')
chestGyro1 = st.sidebar.slider('Index of accessibility to radial highways: ',1,25,5)
chestMagne1  = st.sidebar.slider('Full-value property-tax rate per 10,000 USD: ',100,1000,250)
chestMagne2 = st.sidebar.slider('Full-value property-tax rate per 10,000 USD: ',100,1000,250)
ankleTemperature = st.sidebar.slider('Pupil-teacher ratio by town: ')
ankleAcc16_2 = st.sidebar.slider('Proportion of blacks by town: ')
ankleAcc6_2 = st.sidebar.slider('Lower status of the population: ')
ankleGyro2 = st.sidebar.slider('Proportion of blacks by town: ')
ankleMagne1 = st.sidebar.slider('Proportion of blacks by town: ')
ankleMagne3 = st.sidebar.slider('Proportion of blacks by town: ')

input = np.array([[heartrate, handTemperature, handAcc16_1, handAcc6_1, handGyro1, handMagne1, chestTemperature, chestAcc16_1, chestGyro1, chestMagne1, chestMagne2, ankleTemperature, ankleAcc16_2, ankleAcc6_2, ankleGyro2, ankleMagne1, ankleMagne3]])

html_temp = '''
    <div>
    <h2></h2>
    <center><h3>Select your Regression Model</h3></center>
    </div>
    '''
st.set_option('deprecation.showfileUploaderEncoding', False)
st.markdown(html_temp, unsafe_allow_html=True)
opt = st.selectbox("Which Model do you want for Regression?\n", ('Please Select', 'Logistic Regressor', 'Decision Tree Classifier'))

if opt == 'Logistic Regressor':
  logistic_regressor = LogisticRegression()
  '''logistic_regressor.fit(X, y)'''
  if st.button('Predict'):
    st.info('Predicted Activity: $ {:.3f}'.format(logistic_regressor.predict(input)[0]))

elif opt == 'Decision Tree Classifier':
  dtc_classifier = DecisionTreeClassifier(random_state=8)
  '''dtc_classifier.fit(X, y)'''
  if st.button('Predict'):
    st.info('Predicted Activity: $ {:.3f}'.format(dtc_classifier.predict(input)[0]))
