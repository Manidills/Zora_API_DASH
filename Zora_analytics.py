import requests
import plost
import datetime
import pandas as pd
from pathlib import Path
from sqlite3 import Connection
from common.connect import *
import streamlit as st



def zora_data():
    
    st.markdown('#')

    data = connect('zora.db')
    st.markdown('#')

    st.title("ZORA MARKETPLACE")
    st.markdown('#')

    col1, col2, col3 = st.columns(3)
    col1.metric("Zora Marketplace Total Volume", '$47,565,089')
    col2.metric("Zora Marketplace Total Volume By Version 3", '$5,217,185')
    col3.metric('Zora Marketplace Total Volume By Version 2', '$25,603,545')

    st.markdown('#')
    col1, col2 = st.columns((2,2))

    with col1:
        line_chart(data, 'Zora_marketplace_volume_in_usd', 'time', 'weekly_volume_usd', 'Zora_marketplace_volume_in_usd')
        st.markdown('#')
        bar_chart_vertical(data, 'Zora_marketplace_volume_in_usd', 'time', 'weekly_volume_cumulated_usd', 'Zora_marketplace_volume_in_cumulated_usd')
        st.markdown('#')
        pie_chart(data, 'Zora_marketplace_volume_by_collection_in_usd', 'collection_name', 'total_volume_usd', 'Zora_marketplace_volume_by_collection_in_usd')
        st.markdown("#")
        line_chart_multi(data, 'Zora_marketplace_unique_wallet', 'month', 'address_count', 'version','Zora_marketplace_unique_wallet')

       
    with col2:
        line_chart(data, 'Zora_marketplace_volume_in_usd', 'time', 'weekly_volume_eth', 'Zora_marketplace_volume_in_eth')
        st.markdown('#')
        bar_chart_vertical(data, 'Zora_marketplace_volume_in_usd', 'time', 'weekly_volume_cumulated_eth', 'Zora_marketplace_volume_in_cumulated_eth')
        st.markdown('#')
        pie_chart(data, 'Zora_marketplace_volume_by_collection_in_usd', 'collection_name', 'total_volume_eth', 'Zora_marketplace_volume_by_collection_in_eth')
        st.markdown('#')
        pie_chart(data, 'Zora_marketplace_distribution_in_usd', 'total_volume_usd', 'version', 'Zora_marketplace_distribution_in_usd')
