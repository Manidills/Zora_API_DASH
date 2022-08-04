import requests
import plost
import datetime
import pandas as pd
from pathlib import Path
from sqlite3 import Connection
from common.connect import *
import streamlit as st



def zora_data_1():
    
    st.markdown('#')

    data = connect('zora.db')
    st.markdown("#")
    st.title("Zora API Genesis Hackathon")

    st.markdown("#")

    col1, col2, col3 = st.columns(3)
    col1.metric("Zora API Genesis Hackathon NFT Minted", '165,319')
    col2.metric("Total Unique Wallets", '15,007')
    col3.metric('Zora API Genesis Hackathon Gas', '63.72Ξ')

    st.markdown('#')

    line_chart(data, 'ZAGH_nft_minted_over_time', 'time', 'nft_minted', 'ZAGH_nft_minted_over_time')

    st.markdown('#')
    pie_chart(data, 'ZAGH_top_minters', 'address', 'minted_amount', 'ZAGH_top_minters')
    pie_chart(data, 'ZAGH_nft_range',  'wallets','range', 'ZAGH_nft_range')
   
    


   
