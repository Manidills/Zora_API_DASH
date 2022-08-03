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
        
    st.title("ZORA CREATOR")
    st.markdown("#")


    col1, col2, col3 = st.columns(3)
    col1.metric("Total Collections", '806')
    col2.metric("Fixed Size Collections", '671')
    col3.metric('Open Editions', '135')

    st.markdown('#')

   
    col1, col2 = st.columns((2,2))

    with col1:
        pie_chart(data, 'Zora_creator_pricing', 'num_minted', 'bucket', 'Zora_creator_mint_range')
        pie_chart(data, 'Zora_creator_mints_by_collection', 'num_minted', 'category', 'Zora_creator_mints_by_collection')
    with col2:
        pie_chart(data, 'Zora_creator_pricing', 'contract_address','total_eth',  'Zora_creator_total_eth_range_by_collection')
        pie_chart(data, 'Zora_creator_mints_by_collection', 'max_supply', 'category', 'Zora_creator_collection_max_supply')


    st.markdown("#")
    st.title("Zora API Genesis Hackathon")

    st.markdown("#")

    col1, col2, col3 = st.columns(3)
    col1.metric("Zora API Genesis Hackathon NFT Minted", '165,319')
    col2.metric("Total Unique Wallets", '15,007')
    col3.metric('Zora API Genesis Hackathon Gas', '63.72Ξ')

    st.markdown('#')

    line_chart(data, 'ZAGH_nft_minted_over_time', 'time', 'nft_minted', 'ZAGH_nft_minted_over_time')
    pie_chart(data, 'ZAGH_top_minters', 'address', 'minted_amount', 'ZAGH_top_minters')
    pie_chart(data, 'ZAGH_nft_range',  'wallets','range', 'ZAGH_nft_range')
   
    


   
