import streamlit as st
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import joblib
from utils import DateModification

class DateModification(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, data, y=None):
        return self

    def transform(self, data, y=None):
        return data


# Load the trained model
joblib_file = "best_model_2.pkl"
model = joblib.load(joblib_file)



# Read data
data = pd.read_csv('car_last.csv')

# Perform DateModification transformations
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
df = data.copy()

data['day'] = data['Date'].dt.day
data['month'] = data['Date'].dt.month
data['year'] = data['Date'].dt.year
data.drop(columns=['Date'], inplace=True)
data_transformed = DateModification().transform(data)

def predict(list_):
    y_pred = model.predict([list_])
    return y_pred

def main():
    st.title('Weekly Sales Prediction')
    st.write('Enter values according to given statements:')
    
    store = st.number_input('Store', min_value=0, max_value=int(data_transformed['Store'].max()), step=int(data_transformed['Store'].min()), value=0)
    
    holiday_flag = st.selectbox('Holiday Flag', ['Yes', 'No'])
    if holiday_flag == 'Yes':
        category_encoded = 1
    else:
        category_encoded = 0

    temperature = st.number_input('Temperature', min_value=float(data_transformed['Temperature'].min()), max_value=float(data_transformed['Temperature'].max()), step=float(data_transformed['Temperature'].min()), value=float(data_transformed['Temperature'].min()))
    
    fuel = st.number_input('Fuel_Price', min_value=float(data_transformed['Fuel_Price'].min()), max_value=float(data_transformed['Fuel_Price'].max()), step=float(data_transformed['Fuel_Price'].min()), value=float(data_transformed['Fuel_Price'].min()))
    
    cpi = st.number_input('CPI', min_value=float(data_transformed['CPI'].min()), max_value=float(data_transformed['CPI'].max()), step=float(data_transformed['CPI'].min()), value=float(data_transformed['CPI'].min()))
    unemployment = st.number_input('Unemployment', min_value=float(data_transformed['Unemployment'].min()), max_value=float(data_transformed['Unemployment'].max()), step=float(data_transformed['Unemployment'].min()), value=float(data_transformed['Unemployment'].min()))
    
    date = st.date_input("Select a date", min_value=df['Date'].min(), max_value=df['Date'].max(), value=df['Date'].min())
    day = date.day
    month = date.month
    year = date.year
    
    list_ = [store, category_encoded, temperature, fuel, cpi, unemployment, day, month, year]
    
    if st.button('Predict'):
        predicted_value = predict(list_)
        st.write(f'Predicted price for given values is {predicted_value[0].round(2)} AZN')

if __name__ == '__main__':
    main()
