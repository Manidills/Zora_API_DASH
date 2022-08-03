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

  query ListCollections( $limit: Int!, $text: String!) {
  search(
    pagination: {limit: $limit}
    query: {text: $text}
    filter: {entityType: COLLECTION}
  ) {
    nodes {
      collectionAddress
      description
      entityType
      name
      tokenId
      entity {
        ... on Collection {
          name
          symbol
          address
          description
          totalSupply
          networkInfo {
            chain
            network
          }
        }
      }
    }
    pageInfo {
      hasNextPage
      limit
    }
  }
}




'''


def search_extract():
    with st.form("form1", clear_on_submit=False): 
        Entity = st.selectbox(
                'Entity Type',
                ('COLLECTION', 'NONE'))
        
        text = st.text_input('Enter Search Query')

        val = st.radio(
        'Limit',
        (10,20,100))

        submit = st.form_submit_button("Submit")

    if submit:
        variables = {'text': text, 'limit': val }
        result = run_query(query, variables)
        list_of_values = result['data']['search']['nodes']
        it = iter(list_of_values)

        col1, col2 = st.columns((2,2))
        for i in it:
            with col1:
                st.markdown("#")
                st.write(i)
            with col2:
                st.markdown("#")
                st.write(next(it))
        download_csv(result['data']['search']['nodes'])
    else:
        st.subheader('Random Collection Search')
        variables = {'text': 'punk', 'limit': 10 }
        result = run_query(query, variables)
        list_of_values = result['data']['search']['nodes']
        it = iter(list_of_values)

        col1, col2 = st.columns((2,2))
        for i in it:
            with col1:
                st.markdown("#")
                st.write(i)
            with col2:
                st.markdown("#")
                st.write(next(it))
       