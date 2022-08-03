import streamlit as st
import pandas as pd



@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')

def download_csv(data):
    df = pd.DataFrame(data)
    csv = convert_df(df)
    download = st.download_button(
                "Press to Download",
                csv,
                "file.csv",
                "text/csv",
                key='download-csv'
            )      