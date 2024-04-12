import streamlit as st
import pandas as pd
st.set_page_config(page_title= "Electricity-bill App", page_icon="🏘️" )

st.image('electricity_poll.jpg', caption='Electricity')
def load_data():
    df_data=pd.read_csv('electricity_bill_dataset_processed.csv')
    return  df_data
df=load_data()
st.title("Electricity Bill:red[Prediction]")
st.markdown("The application is used a prototype of Electricity or Energy price prediction")
st.write(df.head(10))