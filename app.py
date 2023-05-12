import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pkl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Natural Language Processing with Disaster Tweets")
input_test = st.text_input("provide your disaster here", '')

button_clicked = st.button("Predict Tweet")
#if button_clicked:
def showResults():
    Model_Predict = Lrdetect_Model.predict([input_test])

    if Model_Predict[0]==1:
     st.text("This Tweet is Dissaster")

    else:
     st.text("This Tweet is Non Dissaster")

if(button_clicked):
    showResults()
