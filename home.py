import streamlit as st
import base64


def app():
    def image_to_bytes(image_path):

        image_file = open(image_path, "rb")
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        return encoded_image

    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    with col2:

        page_icon = f'<img src="data:image/png;base64,{image_to_bytes("WebsiteImages/home_page_icon.png")}"' \
                    f' class="page_icon">'
        st.markdown(page_icon, unsafe_allow_html=True)
        st.subheader("")
