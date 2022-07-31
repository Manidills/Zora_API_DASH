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

  query ListCollections($saleTypes: [SaleType!], $limit: Int!, $collectionAddresses: [String!]!, $sortKey: SaleSortKey! ) {
  sales(
    filter: {saleTypes: $saleTypes}
    networks: {chain: MAINNET, network: ETHEREUM}
    pagination: {limit: $limit}
    sort: {sortKey: $sortKey, sortDirection: DESC}
    where: {collectionAddresses: $collectionAddresses}
  ) {
    nodes {
      sale {
        buyerAddress
        collectionAddress
        networkInfo {
          chain
          network
        }
        price {
          usdcPrice {
            decimal
          }
        }
        saleContractAddress
        saleType
        sellerAddress
        tokenId
        transactionInfo {
          blockTimestamp
        }
      }
      token {
        collectionAddress
        collectionName
        description
        image {
          url
          size
        }
        metadata
        mintInfo {
          originatorAddress
          toAddress
        }
        name
        owner
      }
    }
  }
}



'''


def sales_extract():
    with st.form("form1", clear_on_submit=False): 
        Collection_address = st.text_input('Contract_address')
        Sales_type = st.selectbox(
            'Sales_Type',
            ('OPENSEA_BUNDLE_SALE', 'OPENSEA_SINGLE_SALE', 'SEAPORT_SALE', 'LOOKS_RARE_SALE',))
        col1, col2 = st.columns((2,2))
        with col1:
            val = st.radio(
            'NFT Limit',
            (10,20,100))
        with col2:
            sort_by = st.radio(
            'Sort_by',
            ('CHAIN_TOKEN_PRICE','NATIVE_PRICE','TIME'))

        submit = st.form_submit_button("Submit")

    if submit:
        variables = {'collectionAddresses': Collection_address, 'limit': val, 'saleTypes': Sales_type, 'sortKey': sort_by, }
        result = run_query(query, variables)
        list_of_values = result['data']['sales']['nodes']
        it = iter(list_of_values)

        col1, col2 = st.columns((2,2))
        for i in it:
            with col1:
                st.write("Token Details")
                st.markdown('#')
                st.write(i['token']['collectionName'])
                st.write(i['token']['owner'])
                st.write(i['token']['image']['url'])
                try:
                    st.image(i['token']['image']['url'], width=400)
                except:
                    pass
                
            with col2:
                st.write("Sale Details")
                st.markdown('#')
                st.markdown('#')
                st.markdown('#')
                st.write(i['sale'])
        