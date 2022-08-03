from Zora_analytics import zora_data
from aggregate_att import aggreagte_att_extract
from aggregate_stats import aggreagte_stats_extract
from collection_api import collection_extract
from mints import mint_extract
from rarity import rarity
from sales import sales_extract
from search import search_extract
import streamlit as st
from streamlit_option_menu import option_menu
import datetime

from token_api import token_extract
import pandas as pd




st.set_page_config(
    page_title="ZORA API DASH",
    layout="wide"
)

new_title = '<p style="font-family: Tangerine; text-align: center; color:white; font-size: 70px;">ZORA API DASH</p>'
st.markdown(new_title, unsafe_allow_html=True)

with st.sidebar:

    option = option_menu("ZORA Explorer", ['ZORA','Collection','AggStats','AggAtt','Sales','Token', 'Search','Mints', 'Rarity'], 
        icons=['house'], menu_icon="cast", default_index=0)

if option == 'ZORA':
    zora_data()

elif option == 'Collection':
   collection_extract()

elif option == 'AggStats':
    aggreagte_stats_extract()

elif option == 'Sales':
    sales_extract()

elif option == 'Token':
    token_extract()

elif option == 'Search':
    search_extract()

elif option == 'Mints':
    mint_extract()

elif option == 'AggAtt':
    aggreagte_att_extract()

elif option == 'Rarity':
    rarity()