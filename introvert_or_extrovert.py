import joblib 
import streamlit as st
import pandas as pd

#loading the model
model=joblib.load('personality_analysis.pkl')

#function to predict based on input
def predict_input(input_params):
  k=model.predict(input_params)
  if k==0:
    return "Extrovert"
  else:
    return "Introvert"
  

#loading the data
data=pd.read_csv("personality_dataset.csv")

#user interfave for collectin information
st.set_page_config(page_title="Personality Prediction", layout="centered")

st.title("Personality Prediction")
st.markdown("Fill out the information below to help us predict your personality traits.")

st.subheader("Alone Time")
tsa=st.slider(
   "How much time do you usually spend alone (in hours)?",
   min_value=data["Time_spent_Alone"].min(),
   max_value=data["Time_spent_Alone"].max()
)

st.subheader("stage presence")
st_fear=st.radio("Do you have stage fear?",["Yes","No"])

st.subheader("Social Engagement")
sea=st.slider(
   "How frequently do you attend social events?",
   min_value=int(data["Social_event_attendance"].min()),
   max_value=int(data["Social_event_attendance"].max()),
   step=1
)

st.subheader("Going Out")
goo=st.slider(
   "How often do you like to go outside?",
   min_value=int(data["Going_outside"].min()),
   max_value=int(data["Going_outside"].max()),
   step=1
)

st.subheader("After Socializing")
das=st.radio("Do you feel drained after socializing?",["Yes","No"])

st.subheader("Friends Circle")
fcs=st.slider(
   "How many close friends do you have?",
   min_value=int(data["Friends_circle_size"].min()),
   max_value=int(data["Friends_circle_size"].max()),
   step=1
)

st.subheader("Social Media Activity")
pf=st.slider(
   "How frequently do you post on social media?",
   min_value=int(data["Post_frequency"].min()),
   max_value=int(data["Post_frequency"].max())
)

#button
if st.button("submit"):
    st_fear=0 if st_fear=="No" else 1
    das=0 if das=="No" else 1
    input=[[tsa,st_fear,sea,goo,das,fcs,pf]]
    res=predict_input(input)
    st.header(f"you are a {res.upper()}")
    print(input)
