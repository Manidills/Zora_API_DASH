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

query ListCollections($address: String!,$tokenId: String!,$eventTypes: [EventType!], $limit: Int!) {
  events(
    where: {tokens: {address: $address, tokenId: $tokenId}}
    filter: {eventTypes: $eventTypes}
    sort: {sortKey: CREATED, sortDirection: DESC}
    pagination: {limit: $limit}
  ) {
    nodes {
      collectionAddress
      eventType
      tokenId
      properties {
        ... on ApprovalEvent {
          approved
          approvalEventType
          approvedAddress
          ownerAddress
        }
        ... on MintEvent {
          __typename
          collectionAddress
          originatorAddress
          price {
            usdcPrice {
              decimal
            }
          }
          toAddress
        }
        ... on Sale {
          saleContractAddress
          buyerAddress
          saleType
          sellerAddress
          tokenId
        }
        ... on TransferEvent {
          __typename
          collectionAddress
          fromAddress
          toAddress
        }
        ... on V3AskEvent {
          __typename
          address
          tokenId
          v3AskEventType
        }
        ... on V3ReserveAuctionEvent {
          __typename
          address
          eventType
          properties {
            ... on V3ReserveAuctionV1AuctionBidProperties {
              __typename
              firstBid
              price {
                usdcPrice {
                  decimal
                }
              }
            }
            ... on V3ReserveAuctionV1AuctionCreatedProperties {
              __typename
              auction {
                currency
                duration
                highestBid
                highestBidder
                seller
                sellerFundsRecipient
              }
            }
          }
        }
      }
    }
  }
}




'''


def event_extract():
    with st.form("form1", clear_on_submit=False): 
        address = st.text_input('Contract_address')
        token_id = st.text_input('Token_ID')
        Sales_type = st.selectbox(
            'Event_Type',
            ('APPROVAL_EVENT', 'SALE_EVENT', 'V3_ASK_EVENT', 'V3_RESERVE_AUCTION_EVENT', 'MINT_EVENT', 'TRANSFER_EVENT'))
        col1, col2 = st.columns((2,2))
        with col1:
            val = st.radio(
            'NFT Limit',
            (10,20,100))

        submit = st.form_submit_button("Submit")

    if submit:
        variables = {'address':address,'tokenId':token_id,'eventTypes': Sales_type,'limit': val, }
        result = run_query(query, variables)
        list_of_values = result['data']['events']['nodes']
        st.subheader(Sales_type)
        it = iter(list_of_values)

        col1, col2 = st.columns((2,2))

        for i in it:
            with col1:
                st.write(i)
            with col2:
                try:
                    st.write(next(it))
                except:
                    pass
        download_csv(result['data']['events']['nodes'])
    else:
        variables = {'address':'0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258','tokenId':'500','eventTypes': 'APPROVAL_EVENT','limit': 20 }
        result = run_query(query, variables)
        list_of_values = result['data']['events']['nodes']
        st.subheader(f'Random token {Sales_type}')
        it = iter(list_of_values)

        col1, col2 = st.columns((2,2))

        for i in it:
            with col1:
                st.write(i)
            with col2:
                try:
                    st.write(next(it))
                except:
                    pass
        