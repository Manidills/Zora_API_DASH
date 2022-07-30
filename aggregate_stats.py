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

  query ListCollections($collectionAddresses: [String!]!, $limit: Int!) {
  aggregateStat {
    floorPrice(
      where: {collectionAddresses: $collectionAddresses}
      networks: {chain: MAINNET, network: ETHEREUM}
    )
    nftCount(
      where: {collectionAddresses: $collectionAddresses}
      networks: {chain: MAINNET, network: ETHEREUM}
    )
    ownerCount(
      where: {collectionAddresses: $collectionAddresses}
      networks: {chain: MAINNET, network: ETHEREUM}
    )
    ownersByCount(
      where: {collectionAddresses: $collectionAddresses}
      networks: {chain: MAINNET, network: ETHEREUM}
      pagination: {limit: $limit}
    ) {
      nodes {
        count
        owner
      }
    }
    salesVolume(
      networks: {chain: MAINNET, network: ETHEREUM}
      where: {collectionAddresses: $collectionAddresses}
    ) {
      chainTokenPrice
      totalCount
      usdcPrice
    }
  }
}


'''


def aggreagte_stats_extract():
    with st.form("form1", clear_on_submit=False): 
        Collection_address = st.text_input('Contract_address')
        val = st.radio(
        'Owner Limit',
        (10,20,100))

        submit = st.form_submit_button("Submit")

    if submit:
        variables = {'collectionAddresses': Collection_address, 'limit': val}
        result = run_query(query, variables)
        st.subheader("Metadata For The Collection")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("floorPrice", result['data']['aggregateStat']['floorPrice'])
        col2.metric("nftCount", result['data']['aggregateStat']['nftCount'])
        col3.metric("ownerCount", result['data']['aggregateStat']['ownerCount'])

        st.markdown("#")
        st.subheader("SalesVolume")
        st.write(result['data']['aggregateStat']['salesVolume'])


        st.markdown("#")
        st.subheader(f"Top {val} OwnersByCount")
       

        variables = {'collectionAddresses': Collection_address, 'limit': val}
        result = run_query(query, variables)
        list_of_values = result['data']['aggregateStat']['ownersByCount']['nodes']
        it = iter(list_of_values)

        col1, col2 = st.columns((2,2))
        for i in it:
            with col1:
                st.markdown("#")
                st.write(i)
            with col2:
                st.markdown("#")
                st.write(next(it))


