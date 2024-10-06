import streamlit as st

# constant Variables
star_and_space = '&#x2605;&nbsp;'
square_bullet_point0 ='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2751'
square_bullet_point1 = '&#x2751;&nbsp;'
circle_bullet_point = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2022;&nbsp;'
tab = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"



def custom_title(title, color, fsize, weight):
    st.markdown(f"<p style='text-align: center; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

def custom_sidebar_title(title, color, fsize, weight):
    st.sidebar.markdown(f"<p style='text-align: left; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

def custom_text(text, color, fsize, weight):
    st.sidebar.markdown(f"<p style='text-align: left; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{text}</p>", unsafe_allow_html=True)

def custom_text_main(title, color, fsize, weight, align):
    st.markdown(f"<p style='text-align: {align}; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

intro = f"{square_bullet_point1} <b>Use-Case:</b><br> Predicting Motorbike Sales with SARIMAX model and understanding the Time Series Data.<br>"
evaluation = f"{square_bullet_point1}<b>Evaluation:</b><br> The time series data on motorbike sales shows clear seasonal patterns, with sales peaking at 300 units during the summer and dropping to 100 units in the winter. This seasonality is crucial for accurate forecasting and planning."
insights =f"{square_bullet_point1}<b>Insights And Takeaways:</b><br> {circle_bullet_point}<b>Seasonal Peaks and Troughs:</b> The SARIMAX model identified and predicted the seasonal peaks in summer and {tab}troughs in winter, allowing for better inventory management.<br>{circle_bullet_point}<b>Trend Analysis:</b>By analysing trends, the model helps in understanding whether the overall demand for <br>{tab} motorbikes is increasing or decreasing over time.<br>{circle_bullet_point}<b>External Influences:</b>Including exogenous variables like marketing efforts or economic indicators can refine<br>{tab} predictions, making them more accurate.<br>"
summary = f"{square_bullet_point1}<b>SARIMAX Applcations:</b><br> Supply Chain Management. | Production Scheduling. | Retail and Sales. | Sales Forecasting. | Promotional Strategies.| Energy Sector. | Demand Forecasting. | Healthcare. | Retail. <br><br>By leveraging the SARIMAX model, one can make informed decisions that align with the seasonal nature of your motorbike sales, ultimately leading to better business outcomes."