import requests
import plost
import datetime
import pandas as pd
from pathlib import Path
from sqlite3 import Connection
from common.connect import *
import streamlit as st



def zora_data_auction():
    
    st.markdown('#')

    data = connect('zora.db')
    st.markdown('#')


    st.title("ZORA ACTION HOUSE")
    st.markdown("#")

    
    st.metric("Zora Auction House Total Sales Volume", '$25,007,654')
    

    st.markdown('#')
   

    line_chart(data, 'Zora_actionhouse_monthly_volume', 'month', 'usd', 'Zora_actionhouse_monthly_volume')

    col1, col2 = st.columns((2,2))

    with col1:
        line_chart(data, 'Zora_actionhouse_weekly_volume', 'week', 'usd', 'Zora_actionhouse_weekly_volume')
        line_chart(data, 'Zora_actionhouse_bidders_over_time', 'date', 'users', 'Zora_actionhouse_bidders_over_time')
        

       
    with col2:
        line_chart(data, 'Zora_actionhouse_monthly_active_house', 'date', 'bidders', 'Zora_actionhouse_monthly_active_bidders')
        pie_chart(data, 'Zora_actionhouse_volume', 'usd','token_contract',  'Zora_actionhouse_volume')
        
   