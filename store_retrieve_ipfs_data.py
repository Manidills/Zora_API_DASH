import time
import nft_storage
from nft_storage.api import nft_storage_api
from nft_storage.model.error_response import ErrorResponse
from nft_storage.model.upload_response import UploadResponse
from nft_storage.model.unauthorized_error_response import UnauthorizedErrorResponse
from nft_storage.model.forbidden_error_response import ForbiddenErrorResponse
from pprint import pprint
import pandas as pd
import streamlit as st
import requests




    


#NFT Storage IPFS
def nft_storage_store(file):
    # Defining the host is optional and defaults to https://api.nft.storage
    # See configuration.py for a list of all supported configuration parameters.
    configuration = nft_storage.Configuration(
        host = "https://api.nft.storage"
    )

    configuration = nft_storage.Configuration(
    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDE0RkY4NTU4MzVGMDYwZDBCRTk0ZWQyOTBjNTdiODE1YTE5MjQxNUQiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY1NzU2OTU4ODQxOSwibmFtZSI6Ik1BTklESUxMUyJ9.idaK-qJVyOb8WKP1cD0yddE8UJX4zRpBKtX-QqN49fU'
)
    with nft_storage.ApiClient(configuration) as api_client:
    # Create an instance of the API class
        api_instance = nft_storage_api.NFTStorageAPI(api_client)
        body = open(file, 'rb') # file_type | 

        # example passing only required values which don't have defaults set
        try:
            # Store a file
            api_response = api_instance.store(body, _check_return_type=False)
            return(api_response)
        except nft_storage.ApiException as e:
            st.info("Exception when calling NFTStorageAPI->store: %s\n" % e)

def get_nft_storage(cid_):
    configuration = nft_storage.Configuration(
    host = "https://api.nft.storage"
)
    configuration = nft_storage.Configuration(
        access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDE0RkY4NTU4MzVGMDYwZDBCRTk0ZWQyOTBjNTdiODE1YTE5MjQxNUQiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY1NzU2OTU4ODQxOSwibmFtZSI6Ik1BTklESUxMUyJ9.idaK-qJVyOb8WKP1cD0yddE8UJX4zRpBKtX-QqN49fU'
    )


    with nft_storage.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = nft_storage_api.NFTStorageAPI(api_client)
        cid = cid_ # str | CID for the NFT

        # example passing only required values which don't have defaults set
        try:
            # Get information for the stored file CID
            api_response = api_instance.status(cid,_check_return_type=False)
            return(api_response)
        except nft_storage.ApiException as e:
            print("Exception when calling NFTStorageAPI->status: %s\n" % e)