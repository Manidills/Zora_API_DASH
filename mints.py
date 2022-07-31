from pprint import pprint
from typing import Collection
import requests
import streamlit as st


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

 query ListCollections($sortKey: MintSortKey!, $limit: Int!, $minterAddresses: [String!]) {
  mints(
    pagination: {limit: $limit}
    sort: {sortKey: $sortKey, sortDirection: DESC}
    where: {minterAddresses: $minterAddresses}
  ) {
    nodes {
      mint {
        collectionAddress
        originatorAddress
        price {
          usdcPrice {
            decimal
          }
        }
        toAddress
        tokenId
      }
      token {
        collectionAddress
        collectionName
        description
        name
        owner
        tokenId
        image {
          url
        }
      }
    }
  }
}


'''


def mint_extract():
    with st.form("form1", clear_on_submit=False): 
        Collection_address = st.text_input('Minter_address')
        col1, col2 = st.columns((2,2))
        with col1:
            val = st.radio(
            'NFT Limit',
            (10,20,100))
        with col2:
            sort_by = st.radio(
            'Sort_by',
            ('TOKEN_ID','PRICE','TIME'))

        submit = st.form_submit_button("Submit")

    if submit:
        variables = {'minterAddresses': Collection_address, 'limit': val,  'sortKey': sort_by, }
        result = run_query(query, variables)
        list_of_values = result['data']['mints']['nodes']
        it = iter(list_of_values)

        col1, col2 = st.columns((2,2))

        for i in it:
            with col1:
                st.write('NFT')
                try:
                    st.markdown("#")
                    st.markdown("#")
                    st.markdown("#")
                    if i['token']['image']['url'].startswith("ipfs") or i['token']['image']['url'].startswith('https://exodia'):
                        st.image('https://opensea.io/static/images/logos/opensea.svg', width=300)
                    else:
                        st.image(i['token']['image']['url'], width=300)
                except:
                    st.image('https://opensea.io/static/images/logos/opensea.svg', width=300)
            with col2:
                st.write('Minted NFT Details')
                st.markdown("#")
                st.markdown("#")
                st.write(i['mint'])   
       
        