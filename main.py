import streamlit as st

import pandas as pd
import numpy as np

from sklearn import metrics
import matplotlib.pyplot as plt
# import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

import pickle


activityIDdict = {0: 'Transient',
              1: 'Lying',
              2: 'Sitting',
              3: 'Standing',
              4: 'Walking',
              5: 'Running',
              6: 'Cycling',
              7: 'Nordic_walking',
              9: 'Watching_TV',
              10: 'Computer_work',
              11: 'Car driving',
              12: 'Ascending_stairs',
              13: 'Descending_stairs',
              16: 'Vacuum_cleaning',
              17: 'Ironing',
              18: 'Folding_laundry',
              19: 'House_cleaning',
              20: 'Playing_soccer',
              24: 'Rope_jumping' }
              

html_temp = '''
    <div style = "background-color: rgba(25,25,112,0.06); padding-bottom: 30px; padding-top: 20px; padding-left: 5px; padding-right: 5px">
    <center><h1>Activity Prediction of the Elderly</h1></center>
    
    </div>
    '''
st.markdown(html_temp, unsafe_allow_html=True)

st.sidebar.header('Enter Features for Prediction')
heartrate  = st.sidebar.slider('The heartrate recorded: ',-10.0, 10.0, 0.001)
handTemperature  = st.sidebar.slider('Temperature of the hand: ',-10.0, 10.0, 0.001)
handAcc16_1 = st.sidebar.slider('Accelerometer reading of hand sensor: ',-10.0, 10.0, 0.001)
handAcc6_1 = st.sidebar.slider('Second Accelerometer reading of hand sensor ',-10.0, 10.0, 0.001)
handGyro1 = st.sidebar.slider('Gyrometer reading of hand sensor: ',-10.0, 10.0, 0.001)
handMagne1 = st.sidebar.slider('Magnetometer reading of hand sensor ',-10.0, 10.0, 0.001)
chestTemperature = st.sidebar.slider('Temperature of the chest: ',-10.0, 10.0, 0.001)
chestAcc16_1 = st.sidebar.slider('Accelerometer reading of chest sensor: ',-10.0, 10.0, 0.001)
chestGyro1 = st.sidebar.slider('Gyrometer reading of chest sensor: ',-10.0, 10.0, 0.001)
chestMagne1  = st.sidebar.slider('Magnetometer reading of chest sensor: ',-10.0, 10.0, 0.001)
chestMagne2 = st.sidebar.slider('Second magnetometer reading of chest sensor: ',-10.0, 10.0, 0.001)
ankleTemperature = st.sidebar.slider('Temperature of the ankle: ',-10.0, 10.0, 0.001)
ankleAcc16_2 = st.sidebar.slider('Accelerometer reading of ankle sensor: ',-10.0, 10.0, 0.001)
ankleAcc6_2 = st.sidebar.slider('Second Accelerometer reading of ankle sensor: ',-10.0, 10.0, 0.001)
ankleGyro2 = st.sidebar.slider('Gyrometer reading of ankle sensor: ',-10.0, 10.0, 0.001)
ankleMagne1 = st.sidebar.slider('Magnetometer reading of ankle sensor: ',-10.0, 10.0, 0.001)
ankleMagne3 = st.sidebar.slider('Second Magnetometer reading of ankle sensor: ',-10.0, 10.0, 0.001)

input = np.array([[heartrate, handTemperature, handAcc16_1, handAcc6_1, handGyro1, handMagne1, chestTemperature, chestAcc16_1, chestGyro1, chestMagne1, chestMagne2, ankleTemperature, ankleAcc16_2, ankleAcc6_2, ankleGyro2, ankleMagne1, ankleMagne3]])

html_temp = '''
    <div>
    <h2></h2>
    <center><h3>Select your Classification Model</h3></center>
    </div>
    '''
st.set_option('deprecation.showfileUploaderEncoding', False)
st.markdown(html_temp, unsafe_allow_html=True)
opt = st.selectbox("Which Model do you want for Activity Classification?\n", ('Please Select', 'Logistic Regressor', 'Decision Tree Classifier'))

if opt == 'Logistic Regressor':
  #logistic_regressor = LogisticRegression()

  logistic_regressor = pickle.load(open('models/logistic_regressor.pkl','rb'))

  if st.button('Predict'):
    activityid = logistic_regressor.predict(input)[0]
    activity = activityIDdict[activityid]
    st.write('Predicted Activity: ', activity)

elif opt == 'Decision Tree Classifier':
  #dtc_classifier = DecisionTreeClassifier(random_state=8)
  
  dtc_classifier = pickle.load(open('models/decision_tree_classifier.pkl','rb'))
  
  if st.button('Predict'):
    activityid = dtc_classifier.predict(input)[0]
    activity = activityIDdict[activityid]
    st.write('Predicted Activity: ', activity)
