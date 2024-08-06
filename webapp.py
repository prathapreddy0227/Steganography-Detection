import streamlit as st
from encode import main_encode
from decode import main_decode
# from tensorflow.keras.models import load_model
import cv2
from PIL import Image


# model = load_model('model.h5')
print("Loading model.......Loading complete")
st.title("SteganoGraphy Using ResNet")
st.write("Encoding")
host_image = st.file_uploader("Enter Host Image", type=["png", "jpg", "jpeg"])
hidden_image = st.file_uploader("Enter Hiding Image", type=["png", "jpg", "jpeg"])
encode_button = st.button('Encode')
if encode_button:
    host_image_data = Image.open(host_image)
    hidden_image_data = Image.open(hidden_image)

    host_image_data.save(f'{host_image.name}')
    hidden_image_data.save(f'{hidden_image.name}')
    main_encode(host_image.name, hidden_image.name)
    st.write('encoding complete')
    st.image('encoded/encoded_image.png')


st.write('Decode')
host_with_hidden = st.file_uploader('Enter the Host image with hidden data', type=["png", "jpg", "jpeg"])
decode_button = st.button("decode")
if decode_button:
    hidden_data_host_image = Image.open(host_with_hidden)
    hidden_data_host_image.save(f'{host_with_hidden.name}')
    main_decode(host_with_hidden.name)
    st.image('deocoded/decoded_image.png')
    



