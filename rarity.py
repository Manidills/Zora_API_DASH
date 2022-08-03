from typing import ItemsView
import requests
import json
import itertools
import streamlit as st
import pandas as pd


def get_rarity(tokens):
    # WIP
    for token in tokens:
        if "metadata" in token:
            return True

    st.error("This collection has no metadata")
    return False


def run_zora_query(query, variables=None):
    endpoint = "https://indexer-prod-mainnet.ZORA.co/v1/graphql"

    body = {"query": query}

    if variables is not None:
        body["variables"] = variables

    response = requests.post(
        endpoint, json=body, headers={"X-Hasura-Role": "anonymous"}
    )
    return response.json()


def get_tokens(address):
    token_query = """
    query GetTokens($address: String) {
      Token(
        where: { address: { _eq: $address } },
        order_by: { tokenId: asc }
      ) {
        tokenId
        address
        minter
        owner
        metadata {
          json
        }
      }
    }
    """
    variables = {"address": address}
    return run_zora_query(token_query, variables)



def rarity():

    st.title("NFT Tracker")
    default_item = "Select collection"

    if "contract_address" not in st.session_state:
        query = """
    {
        TokenContract {
        address
        name
        supportsMetadata
        symbol
        }
    }
    """
        data = run_zora_query(query)
        st.session_state["contract_address"] = {
            nft_collection["name"]: nft_collection["address"]
            for nft_collection in data["data"]["TokenContract"]
        }
        st.session_state["supported_contracts"] = [
            nft_collection["name"] for nft_collection in data["data"]["TokenContract"]
        ]
        st.session_state["supported_contracts"].insert(0, default_item)

    selected_contract = st.selectbox(
        label="NFT collection name",
        options=sorted(st.session_state["supported_contracts"]),
        index=20,
    )

    if selected_contract != default_item:
        selected_contract_address = st.session_state["contract_address"][selected_contract]

        tokens = get_tokens(st.session_state["contract_address"][selected_contract])
        tokens = tokens["data"]["Token"]

        has_rarity = get_rarity(tokens)

        if has_rarity:

            number_items = st.select_slider("Token limit", [50, 100, 150, 200], value=50)
            col1, col2, col3, col4, col5 = st.columns(5)
            image_columns = itertools.cycle([col1, col2, col3, col4, col5])

            collection_attributes = list(itertools.chain.from_iterable(tokens))
            actual_item = 0

            for request in tokens:
                actual_item += 1

                if actual_item > number_items:
                    break

                col = next(image_columns)
                # TODO: not all items have metadata, workaround

                token_id = request["tokenId"]
                if request["metadata"]["json"]["image"] is not None:
                    with col:
                        st.image(request["metadata"]["json"]["image"], width=128)
                        st.markdown(f"Token ID: {token_id}")
                        st.markdown(
                            f"[OpenSea listing](https://opensea.io/assets/{selected_contract_address.lower()}/{token_id})"
                        )