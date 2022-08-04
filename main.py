from Zora_analytics import zora_data
from aggregate_att import aggreagte_att_extract
from aggregate_stats import aggreagte_stats_extract
from collection_api import collection_extract
from events import event_extract
from mints import mint_extract
from rarity import rarity
from sales import sales_extract
from search import search_extract
import streamlit as st
from streamlit_option_menu import option_menu
import datetime

from token_api import token_extract
import pandas as pd
from zora_auction import zora_data_auction

from zora_collection import zora_data_1
from zora_creator import zora_data_creator




st.set_page_config(
    page_title="ZORA API DASH",
    layout="wide"
)

new_title = '<p style="font-family: Tangerine; text-align: center; color:white; font-size: 70px;">ZORA API DASH</p>'
st.markdown(new_title, unsafe_allow_html=True)



option = option_menu("ZORA Explorer", ['ZORA','Collection','AggStats','AggAtt','Sales','Token', 'Search'], 
    icons=['house'], menu_icon="cast", default_index=0, orientation="horizontal")

if option == 'ZORA':
    st.markdown('#')
    st.markdown('<p style="font-family: Tangerine; text-align: center; color:white; font-size: 20px;">ZORA analytics that shows the basic insights on zora marketplaces, zora auction house, zora creator and zora api genesis hackathon</p>',unsafe_allow_html=True)

    st.markdown('#')
    with st.form("form1", clear_on_submit=False): 
        option_zora = st.selectbox('SELECT ZORA PROTOCOL',('ZORA_MARKETPLACE','ZORA_AUCTION_HOUSE', 'ZORA_CREATOR', 'ZAGH'))
        submit = st.form_submit_button("Submit") 
    st.markdown("#")
    if submit:
        if option_zora == 'ZORA_MARKETPLACE':
            zora_data()
        elif option_zora == 'ZORA_AUCTION_HOUSE':
            zora_data_auction()
        elif option_zora == 'ZORA_CREATOR':
            zora_data_creator()
        elif option_zora == 'ZAGH':
            zora_data_1()
    else:
        zora_data()

elif option == 'Collection':
   collection_extract()

elif option == 'AggStats':
    aggreagte_stats_extract()

elif option == 'Sales':
    sales_extract()

elif option == 'Token':
    st.markdown('#')

    option_token = st.radio('TOKEN ANALYTICS',('Token','Mints', 'Events', 'Rarity'))
    st.markdown('#')
    if option_token == 'Token':
        token_extract()
    elif option_token == 'Mints':
        mint_extract()
    elif option_token == 'Events':
        event_extract()
    elif option_token == 'Rarity':
        rarity()

elif option == 'Search':
    search_extract()

elif option == 'AggAtt':
    aggreagte_att_extract()

