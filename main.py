from aggregate_stats import aggreagte_stats_extract
from collection_api import collection_extract
import streamlit as st
from streamlit_option_menu import option_menu
import datetime




st.set_page_config(
    page_title="ZORA API DASH",
    layout="wide"
)

new_title = '<p style="font-family: Tangerine; text-align: center; color:white; font-size: 70px;">ZORA API DASH</p>'
st.markdown(new_title, unsafe_allow_html=True)



option = option_menu("ZORA Explorer", ['Collections','AggStats','Collections','Token', 'Wallet','Summary', 'Mint'], 
    icons=['house'], menu_icon="cast", default_index=0,  orientation="horizontal")



if option == 'Collections':
   collection_extract()

elif option == 'AggStats':
    aggreagte_stats_extract()