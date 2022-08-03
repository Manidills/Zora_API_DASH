from pprint import pprint
from typing import Collection
import requests
from common_1 import convert_df
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
query_page = """
  query ListCollections($limit: Int!, $sortKey: CollectionSortKey!, $sortDirection: SortDirection! ) {
  collections(
    sort: {sortKey: $sortKey, sortDirection: $sortDirection}
    networks: {chain: MAINNET, network: ETHEREUM}
    pagination: {limit: $limit}
  ) {
    nodes {
      address
      name
      symbol
      totalSupply
      networkInfo {
        chain
        network
      }
      attributes {
        traitType
        valueMetrics {
          count
          percent
          value
        }
      }
    }
  }
}

"""

query = '''

  query ListCollections($collectionAddresses: [String!]!) {
  collections(
    sort: {sortKey: CREATED, sortDirection: ASC}
    networks: {chain: MAINNET, network: ETHEREUM}
    where: {collectionAddresses: $collectionAddresses}
  ) {
    nodes {
      address
      name
      symbol
      totalSupply
      networkInfo {
        chain
        network
      }
      attributes {
        traitType
        valueMetrics {
          count
          percent
          value
        }
      }
      description
    }
  }
}


'''


def collection_extract():
    with st.form("form1", clear_on_submit=False): 
        Collection_address = st.text_input('Contract_address')
        submit = st.form_submit_button("Submit")

            

    if submit:
      variables = {'collectionAddresses': Collection_address}
      result = run_query(query, variables)
      st.subheader("Metadata For The Collection")
      st.write(result['data']['collections']['nodes'])

    
      df = pd.DataFrame(result['data']['collections']['nodes'])
      csv = convert_df(df)
      download = st.download_button(
                "Press to Download",
                csv,
                "file.csv",
                "text/csv",
                key='download-csv'
              )
    else:
      num_value = 10

      st.subheader("Top 10 Collection")
      st.markdown("#")

      col1, col2 = st.columns((2,2)) 
      with col1:
        sort_by = st.radio(
        'Sort_by',
        ('CREATED', 'NAME'))
      with col2:
        sort_order = st.radio(
          'order', ('DESC', 'ASC')
        )
      
      variables = {'limit': num_value, 'sortKey': sort_by, 'sortDirection': sort_order}
      result = run_query(query_page, variables)
     
      
      list_of_values = result['data']['collections']['nodes']
      it = iter(list_of_values)

      col1, col2 = st.columns((2,2))
      for i in it:
        with col1:
          st.markdown("#")
          st.write(i)
        with col2:
          st.markdown("#")
          st.write(next(it))


   


    