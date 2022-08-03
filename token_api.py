from pprint import pprint
from typing import Collection
import requests
from common_1 import download_csv
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
  token(
    token: {address: $address, tokenId: $tokenId}
  ) {
    token {
      collectionAddress
      collectionName
      description
      lastRefreshTime
      name
      owner
      tokenId
      tokenUrl
      tokenUrlMimeType
      image {
        url
      }
    }
    sales {
      buyerAddress
      collectionAddress
      price {
        usdcPrice {
          decimal
        }
      }
      saleContractAddress
      saleType
      sellerAddress
      tokenId
    }
  }
}




'''


def token_extract():
    with st.form("form1", clear_on_submit=False): 
        Collection_address = st.text_input('Contract_address')
        token_id = st.text_input('Token_ID')

        submit = st.form_submit_button("Submit")

    if submit:
        variables = {'address': Collection_address, 'tokenId': token_id }
        result = run_query(query, variables)
        list_of_values = result['data']['token']

        col1, col2 = st.columns((5,3))
        
        with col1:
                st.write("Token Details")
                st.markdown('#')
                
                try:
                    st.image(list_of_values['token']['image']['url'], width=400)
                except:
                    pass
                st.write(list_of_values['token'])
                
        with col2:
                st.write("Sale Details")
                st.markdown('#')
                st.markdown('#')
                st.markdown('#')
                st.write(list_of_values['sales'])
        download_csv(result['data']['token']
)
    else:
        st.subheader("Random Token For Showcase")
        variables = {'address': '0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258', 'tokenId': '60809' }
        result = run_query(query, variables)
        list_of_values = result['data']['token']

        col1, col2 = st.columns((5,3))
        
        with col1:
                st.write("Token Details")
                st.markdown('#')
                
                try:
                    st.image(list_of_values['token']['image']['url'], width=400)
                except:
                    pass
                st.write(list_of_values['token'])
                
        with col2:
                st.write("Sale Details")
                st.markdown('#')
                st.markdown('#')
                st.markdown('#')
                st.write(list_of_values['sales'])
      
        