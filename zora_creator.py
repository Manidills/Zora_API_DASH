import requests
import plost
import datetime
import pandas as pd
from pathlib import Path
from sqlite3 import Connection
from common.connect import *
import streamlit as st



def zora_data_creator():
    
    st.markdown('#')

    data = connect('zora.db')
    st.markdown('#')

    
    st.title("ZORA CREATOR")
    st.markdown("#")


    col1, col2, col3 = st.columns(3)
    col1.metric("Total Collections", '806')
    col2.metric("Fixed Size Collections", '671')
    col3.metric('Open Editions', '135')

    st.markdown('#')

    st.subheader("Zora_creator_collections")
    st.dataframe(table(data, 'Zora_creator_mints_by_collection'))
    

    st.markdown('#')
    col1, col2 = st.columns((2,2))

    with col1:
        pie_chart(data, 'Zora_creator_pricing', 'num_minted', 'bucket', 'Zora_creator_mint_range')
        pie_chart(data, 'Zora_creator_mints_by_collection', 'num_minted', 'category', 'Zora_creator_mints_by_collection')
    with col2:
        pie_chart(data, 'Zora_creator_pricing', 'contract_address','total_eth',  'Zora_creator_total_eth_range_by_collection')
        pie_chart(data, 'Zora_creator_mints_by_collection', 'max_supply', 'category', 'Zora_creator_collection_max_supply')


    st.markdown("#")
    st.subheader("Zora_creator_pricing")
    st.dataframe(table(data,'Zora_creator_pricing'))