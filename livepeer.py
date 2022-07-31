import streamlit as st
import cv2 as cv
import tempfile

f = st.file_uploader("Upload file")
tfile = tempfile.NamedTemporaryFile(delete=False)
tfile.write(f.read())
vf = cv.VideoCapture(tfile.name)