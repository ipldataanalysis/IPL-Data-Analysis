import streamlit as st
import home
import about_ipl
import ipl_stats
import personnel_changes
import points_table
import feedback
import base64

def main():
    def image_to_bytes(image_path):
        image_file = open(image_path, "rb")
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        return encoded_image

    st.set_page_config(
        page_title="IPL Data Analysis",
        page_icon=f"data:image/png;"
                  f"base64,{image_to_bytes('WebsiteImages/page_icon.png')}",
        layout="wide"
    )

    markdown = open("WebsiteStyles/ipl_data_analysis.html", "r").read()
    st.markdown(markdown, unsafe_allow_html=True)

    st.sidebar.subheader("")
    sidebar_image = f'<img src="data:image/png;base64,{image_to_bytes("WebsiteImages/sidebar_image.png")}"' \
                    f' class="image_sidebar">'
    st.sidebar.markdown(sidebar_image, unsafe_allow_html=True)
    st.sidebar.subheader("")

    pages_list = ["Home", "About IPL", "IPL Stats", "Personnel Changes", "Points Table", "Feedback"]
    page = st.sidebar.radio("GO TO", pages_list)

    if page == "Home":
        home.app()
    elif page == "About IPL":
        about_ipl.app()
    elif page == "IPL Stats":
        ipl_stats.app()
    elif page == "Personnel Changes":
        personnel_changes.app()
    elif page == "Points Table":
        points_table.app()
    elif page == "Feedback":
        feedback.app()

    st.sidebar.subheader("")
    st.sidebar.title("Thank You for visiting our Web app")
    st.sidebar.subheader("")
    st.sidebar.write("Please take a few minutes from your busy schedule and provide us your feedback.")
    st.sidebar.write("Your feedback is valuable to us. It helps us to improve our Web analysis app")


if __name__ == "__main__":
    main()
