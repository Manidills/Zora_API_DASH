import io

import requests
import json
import tempfile
import requests
from PIL import Image
from store_retrieve_ipfs_data import  get_nft_storage, nft_storage_store
from tempfile import NamedTemporaryFile

import streamlit as st
from PIL import Image
from gtts import gTTS
from poppler import load_from_data, PageRenderer




def convert(pdf_document, start, end):
    try:
        text = ''
        for x in range(start - 1, end):
            page_current = pdf_document.create_page(x)
            text += page_current.text()
        # initialize tts, create mp3 and play
        mp3_fp = io.BytesIO()
        tts = gTTS(text=text, lang='en', slow=False, lang_check=False, tld='co.in')
        tts.write_to_fp(mp3_fp)
        return mp3_fp
    except AssertionError:
        st.error('The PDF does not seem to have text and maybe its a scanned')


@st.cache
def render_page(file, page):
    renderer = PageRenderer()
    page_1 = file.create_page(page - 1)
    image = renderer.render_page(page_1)

    pil_image = Image.frombytes(
        "RGBA",
        (image.width, image.height),
        image.data,
        "raw",
        str(image.format),
    )
    return pil_image

def easy_mint(name, description, wallet_address, image):

    # f = open(image, 'rb')
    # file = f.read()

    query_params = {
        "chain": "rinkeby",
        "name": name,
        "description": description,
        "mint_to_address": wallet_address
    }

    response = requests.post(
        "https://api.nftport.xyz/v0/mints/easy/files",
        headers={"Authorization": "f6ce3372-a928-4947-8f50-87649f60cee2"},
        params=query_params,
        files={"file": image}
    )

    return response.json()


def preview(pdf_document):
    input_page = st.number_input('Page number', 1, step=2)
    col1, col2 = st.columns(2)
    col1.header(f"Page {input_page}")
    col2.header(f"Page {input_page + 1}")
    left_page = render_page(pdf_document, input_page)
    right_page = render_page(pdf_document, input_page + 1)
    col1.image(left_page, use_column_width=True)
    col2.image(right_page, use_column_width=True)


def audio_main():
    with st.form("form1", clear_on_submit=False):
        st.title('Audio Book Maker')
        uploaded_file = st.file_uploader("Upload a PDF", type=['pdf'])
        start_page = st.number_input("Start Page", 1)
        end_page = st.number_input("End Page", 1)
        name = st.text_input('Name')
        description = st.text_input('Description')
        wallet_address = st.text_input('Mint_address')
        st.info('Conversion takes time, so please be patient')
        submit = st.form_submit_button("Submit & Mint")
    if uploaded_file is not None:
        pdf_document = load_from_data(uploaded_file.read())
    if start_page > end_page:
        st.error('Start Page cannot be greater than end page')
    elif start_page <= end_page:
        if submit and uploaded_file is not None:
            audio_file = convert(pdf_document, start_page, end_page)
            st.audio(audio_file, format='audio/mp3')
            download = st.download_button(
                "Press to Download",
                audio_file,
                "file.mp3",
                'audio/mp3',
                key='download-audio'
              )
        
            temp_file = NamedTemporaryFile(delete=False)
            temp_file.write(audio_file.getvalue())

            st.subheader("NFT Details")
            mint_image = easy_mint(name,description,wallet_address,audio_file)
            st.markdown("#")
            st.subheader(" ")
            if mint_image['response'] == 'OK':
                store_nft = nft_storage_store(temp_file.name)
                st.subheader("Retrive Stored Audio Data from NFT Storage")
                st.write(store_nft)
                st.markdown("#")
                st.subheader("Minted Audio")
                audio_cid = store_nft['value']['cid']
                st.write(f'https://{audio_cid}.ipfs.nftstorage.link/')
                st.audio(f'https://{audio_cid}.ipfs.nftstorage.link/',)
                if store_nft:
                    tfile = tempfile.NamedTemporaryFile(mode="w+")
                    json.dump(mint_image, tfile)
                    tfile.flush()
                    nft_meta = nft_storage_store(tfile.name)
                    st.markdown("#")
                    st.subheader("Retrive Stored Meta Data from NFT Storage")
                    retrive_data = get_nft_storage(nft_meta['value']['cid'])
                    st.success(retrive_data)
                    meta_cid = retrive_data['value']['cid']
                    st.markdown("#")
                    st.write(f'https://{meta_cid}.ipfs.nftstorage.link/')
                    meta_d = requests.get(url = f'https://{meta_cid}.ipfs.nftstorage.link/')
                    st.write(meta_d.text)





            

    # if uploaded_file is not None:
    #     preview(pdf_document)
    
   