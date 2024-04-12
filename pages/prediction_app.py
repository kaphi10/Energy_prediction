import streamlit as st
import pandas as pd
import numpy as np
from pickle import load
from electricity_app import load_data

st.set_page_config(page_title= "energy_price_prediction", page_icon="🌍")

st.sidebar.header("Energy price Prediction")
st.subheader('Predicting the price of energy consumed')
#load the encoded data
def load_encoded():
    df=pd.read_csv('selected_data.csv')
    return df
#load model and scaler-> pickle file
def load_model():
    model=load(open('model.pickle', 'rb'))
    scaler=load(open('scaler2.pickle', 'rb'))
    return  model, scaler
df=load_data()
df_encoded=load_encoded()
# company= st.selectbox('company', (sorted(df.Company.unique())))
# selected_company=df.loc[df['Company']==company]
city=st.selectbox('city',(sorted(df.City.unique())))
selected_city=df.loc[df['City']==city]
monthly_hour=st.number_input("Enter Hour consumed")
tariff=st.number_input("Enter The Tarif consumed")
# reverse_company_dict= dict(zip(df_encoded['Company_encoded'], df['Company']))
city_recorded=[]
for city in selected_city.City.unique():
    update= selected_city.loc[selected_city['City']==city]
    city_recorded.append(city)
# set the dataframe to train
dataset=pd.DataFrame({'MonthlyHours':monthly_hour, 'TariffRate':tariff, 'City':city_recorded})
encoded_df=pd.DataFrame(0, index=np.arange(len(city_recorded)), columns=df_encoded.columns.values)
#st.write(dataset)
dummies_data=pd.get_dummies(dataset, columns=['City'])

other_col= encoded_df.loc[:, ~encoded_df.columns.isin(dummies_data.columns)]
final_test_col=pd.concat([dummies_data,other_col], axis=1)

if st.button('Predict'):

    model, scaler =load_model()
    test_scaled=scaler.transform(final_test_col.values)
    Bill_prediction=model.predict(test_scaled)

    # st.write(prediction)
    dataset['predicted']=Bill_prediction

    predicted_value=list(dataset.predicted)
    def listToString(number):
        # initialize an empty string
        str1 = 0
        # traverse in the string
        for ele in number:
            str1 +=ele
        # return string
        return str1
    # Driver code
    num = predicted_value
    st.write(f"Amount predicted for the electricity consumption is  {listToString(num)}$" )
