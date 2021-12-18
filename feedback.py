import streamlit as st
import pymongo
import base64


def app():
    def image_to_bytes(image_path):
        image_file = open(image_path, "rb")
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        return encoded_image

    page_icon = f'<img src="data:image/png;base64,{image_to_bytes("WebsiteImages/feedback_page_icon.png")}"' \
                f' class="page_icon">'
    st.markdown(page_icon, unsafe_allow_html=True)
    st.subheader("")
    st.write("Your feedback is highly appreciated as it gives us the inputs for further improvement of our webapp. "
             "Your feedback helps us in better understanding of your requirements and enables us to make "
             "our webapp more user-friendly, convenient and hassle free.")
    st.subheader("")

    with st.form(key="feedback_form", clear_on_submit=True):

        question1 = "Which age group do you belong?"
        options_question1 = ['Select', 'Below 15', 'Below 25', 'Below 40', 'Below 55', 'Above 55']
        question2 = "How did you come known about us?"
        question3 = "Did we meet your expectations?"
        question4 = "Did you get required information with ease?"
        question5 = "How would you rate our website?"
        question6 = "Share your suggestions to improve our website?"

        response1 = st.selectbox(question1, options_question1)
        response2 = st.text_input(label=question2)
        response3 = st.text_input(label=question3)
        response4 = st.text_input(label=question4)
        response5 = st.slider(question5, min_value=1, max_value=5, value=3)
        response6 = st.text_input(label=question6)
        submit = st.form_submit_button(label="Submit this form")

        if submit:
            connection = pymongo.MongoClient(st.secrets["mongodb"]["url"])
            database = connection.get_database("feedback_database")
            table = database.feedback_table

            response_data = {
                "S_No": (table.count_documents({}) + 1),
                "Question1": response1,
                "Question2": response2,
                "Question3": response3,
                "Question4": response4,
                "Question5": response5,
                "Question6": response6
            }

            table.insert_one(response_data)

            st.success("Your response is recorded and we thank you for your feedback.")
