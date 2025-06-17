import streamlit as st
import pandas as pd
from titanic.data import load_data, prepare_data, upload_data
import matplotlib.pyplot as plt
import seaborn as sns
import requests
 
if __name__ == "__main__":
      
  st.title("Welcome, enter your information to stay alive on titanic")

  name = st.text_input("Name and surname")
  passenger_id = st.text_input("Passenger id")
  pcclass = st.text_input("ticket class")
  sex = st.selectbox('Select your gender',\
                      ('Male', 'Female'))
  sibsp = st.text_input("# of siblings/spouses aboard Titanic")
  parch = st.text_input("# of parents/children aboard Titanic")
  ticket = st.text_input("Ticket number")
  fare = st.text_input("Ticket price")
  cabin = st.text_input("Cabin")
  embarked = st.selectbox('Where did you get on',\
                      ('S', 'C', 'Q'))
  age = st.slider("Select a number", min_value=0, max_value=100, value=30)
  if st.button("Click Me!") : 
      params = {"passengerid": passenger_id,
                "pclass": pcclass,
                  "name": name,
                  "sex": sex,
                  "age": age,
                  "sibSp": sibsp,
                  "parch": parch,
                  "ticket": ticket,
                  "fare": fare,
                  "cabin": cabin,
                  "embarked": embarked
                }
      
      #answer = requests.get(url = f"https://localhost:8000/predict", params=params)
      answer = requests.get(url = f"https://titanic-api-956675984392.europe-west9.run.app/predict", params=params)
      if answer.status_code == 200:
          st.success(f"{answer.json()['survived']}")


