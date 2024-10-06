import pandas as pd
import numpy as np

import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
from pandas.tseries.offsets import DateOffset

import formatted_characters as fc

import streamlit as st
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")
st.set_option('client.showErrorDetails', False)

def custom_text_main(title, color, fsize, weight, align):
    st.markdown(f"<p style='text-align: {align}; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

def custom_title(title, color, fsize, weight, align):
    st.markdown(f"<p style='text-align: {align}; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    custom_title('Revenue & Sales Prediction','red',30,'bold','center') 
with col2:
    st.image("data/biker.png") 
with col3:
    custom_title('Demand Forecasting','yellow',30,'bold','center')    

# File uploader widget in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose any file on your system but will be overidden by default file. ⚠️")
start = 60
end =   300
selected_end = 240

uploaded_file ="data/sales_data.csv"

data = pd.DataFrame()
isUploadCompleted = False
if uploaded_file is not None:
    # Read the file into a DataFrame
    data = pd.read_csv(uploaded_file)    
   
    st.sidebar.divider()

    selected_end = st.sidebar.slider("Specify the range of the forecast in months: ",0,60,24)
    st.sidebar.write("Prediction range : ", selected_end, " months.")
    isUploadCompleted = True

    data.isna().sum()
    # Sample data
    data = pd.DataFrame({
        'Month': pd.date_range(start='1/1/2020', periods=60, freq='M'),
        'Sales': np.random.randint(100, 300, size=60)
    })

    # Preprocess data
    data.index = pd.to_datetime(data['Month'])
    data.drop(columns='Month', inplace=True)

    # Calculate rolling mean and difference
    rolling_mean = data.rolling(window=12).mean()
    data['rolling_mean_diff'] = rolling_mean - rolling_mean.shift()

    # ARIMA model
    model = ARIMA(data["Sales"], order=(1, 1, 1))
    model_fit = model.fit()
    data['forecast'] = model_fit.predict(start=60, end=300, dynamic=True)

    # ARIMA model on rolling mean difference
    model = ARIMA(data['rolling_mean_diff'].dropna(), order=(1, 1, 1))
    model_fit = model.fit()
    data['forecast'] = model_fit.predict(start=60, end=300, dynamic=True)

    # SARIMAX model
    model = SARIMAX(data['Sales'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    results = model.fit()
    data['forecast'] = results.predict(start=60, end=300, dynamic=True)

    # Extend forecast
    pred_date = [data.index[-1] + DateOffset(months=x) for x in range(0, selected_end)]
    pred_date = pd.DataFrame(index=pred_date[1:], columns=data.columns)

    data = pd.concat([data, pred_date])
    data['forecast'] = results.predict(start=60, end=300, dynamic=True)    

    # Function to create a plot.   
    if st.sidebar.button('Plot Graph'):
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.set_title("Motorbike Sales Prediction.  ")
        data[['Sales', 'forecast']].plot(ax=ax)
        st.pyplot(fig)

        st.write("Data Storytelling (Machine Learning / SARIMAX Model).")
        text="The project presents estimates for motorbike unit sales based on historical data, which was utilised to forecast or predict the future unit sales values. Additionally, demand management procurement scenarios and store or warehouse replenishments could make use of this use case."
        custom_text_main(text, 'orange', 14, 'normal', 'justified')                 
        fc.custom_text_main(fc.intro, 'orange', 14, 'normal', 'left')
        fc.custom_text_main(fc.evaluation, 'orange', 14, 'normal', 'left') 
        fc.custom_text_main(fc.insights, 'orange', 14, 'normal', 'left')
        fc.custom_text_main(fc.summary, 'orange', 14, 'normal', 'left') 
    st.sidebar.divider()

    st.sidebar.write(":red[App showcasing demand forecasting Use-Case.]")
    st.sidebar.write(":orange[ Implemented by Pete Chisamba.]")




