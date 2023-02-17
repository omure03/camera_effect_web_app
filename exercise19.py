import streamlit as st
from PIL import Image

with st.expander("take a photo"):
    # Start camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)