from pprint import pprint
from typing import Collection
import requests
from common_1 import convert_df, download_csv
import streamlit as st
import pandas as pd


# function to use requests.post to make an API call to the subgraph url
def run_query(query, variables):

    # endpoint where you are making the request
    request = requests.post(' https://api.zora.co/graphql'
                            '',
                            json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))


# The Graph query - Query aave for a list of the last 10 flash loans by time stamp


query = '''

  query ListCollections($address: String!, $tokenId: String!) {
  aggregateAttributes(
    where: {tokens: {address: $address, tokenId: $tokenId }}
  ) {
    traitType
    valueMetrics {
      count
      percent
      value
    }
  }
}



'''


def aggreagte_att_extract():
    with st.form("form1", clear_on_submit=False): 
        Collection_address = st.text_input('Contract_address')
        token_id = st.text_input('token_id')

        submit = st.form_submit_button("Submit")

    if submit:
        variables = {'address': Collection_address, 'tokenId': token_id}
        result = run_query(query, variables)
        list_of_att = result['data']['aggregateAttributes']
        it = iter(list_of_att)
        st.subheader("Attributes of the NFT")
        col1, col2 = st.columns((2,2))
        
        for i in it:
            with col1:
                st.markdown("#")
                st.write(i)
            with col2:
                try:
                    st.markdown("#")
                    st.write(next(it))
                except:
                    pass
        download_csv(result['data']['aggregateAttributes'])  
    else:
        variables = {'address': '0x60e4d786628fea6478f785a6d7e704777c86a7c6', 'tokenId': '7077'}
        result = run_query(query, variables)
        list_of_att = result['data']['aggregateAttributes']
        it = iter(list_of_att)
        st.subheader("Attributes of the Random NFT")
        col1, col2 = st.columns((2,2))
        
        for i in it:
            with col1:
                st.markdown("#")
                st.write(i)
            with col2:
                try:
                    st.markdown("#")
                    st.write(next(it))
                except:
                    pass
            
