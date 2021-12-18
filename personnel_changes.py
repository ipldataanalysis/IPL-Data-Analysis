import streamlit as st
import pandas as pa
import numpy as npy
import base64


def app():
    def image_to_bytes(image_path):
        image_file = open(image_path, "rb")
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        return encoded_image

    page_icon = f'<img src="data:image/png;base64,{image_to_bytes("WebsiteImages/personnel_changes_page_icon.png")}"' \
                f' class="page_icon">'
    st.markdown(page_icon, unsafe_allow_html=True)
    st.subheader("")
    st.write("Every season IPL witnesses Personnel changes. New franchises are added and some old franchises are "
             "left. Each franchise depending on the availability of funds and opinions given by their respective "
             "managers and experts performs pre-auctions. Personnel changes table gives information about team "
             "players, retained/ released players, staff changes, sold players and so on.")
    st.subheader("")

    def streamlit_table(dataframe_styled):
        st.dataframe(dataframe_styled)

    @st.cache
    def convert_dataframe_to_csv(df):
        return df.to_csv().encode('utf-8')

    table_style = {
        'color': 'white',
        'font-size': '20px',
        'background-color': '#5aa70a',
        'text-align': 'center'
    }

    with st.expander("Personnel Changes Summary", expanded=True):

        st.subheader("")
        st.write("This section of the page consists the Personnel Changes summary of all teams in a tabular form")
        st.subheader("")

        columns = st.columns([7, 2])
        with columns[1]:
            st.write("(Amount in ₹ lakhs)")

        dataset = f"IPL 2021 PCS.csv"
        dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
        dataframe.index = npy.arange(1, len(dataframe) + 1)
        table = dataframe

        streamlit_table(table.style.set_properties(**table_style))

        csv = convert_dataframe_to_csv(table)

        st.subheader("")
        st.write(f"To download the Personnel Changes Summary data, please click the below button")
        st.subheader("")

        st.download_button(
            label=f"Download Personnel Changes Summary data as CSV",
            data=csv,
            file_name=f'personnel_changes_summary_data.csv',
            mime='text/csv',
        )

    st.subheader("")
    st.write("")
    st.subheader("")

    select_box_choices = ["Pre Auction", "Auction", "Support Staff"]
    choice = st.selectbox("Select a section to view in detail", select_box_choices)

    if choice == "Pre Auction":

        st.subheader("")
        st.subheader("Pre Auction")
        st.write("In every season a Pre-auction is conducted to maintain a level playing field for all the teams. All "
                 "the existing franchises are allowed upto four player retentions. Retention/released/ withdrawn of "
                 "players is done in pre-auction. Pre-auction details of all the teams are presented below.")
        st.subheader("")

        with st.expander("Pre Auction Summary", expanded=True):

            st.subheader("")
            st.write("This section of the page consists the Pre Auction summary of all teams in a tabular form")
            st.subheader("")

            columns = st.columns([7, 2])
            with columns[1]:
                st.write("(Amount in ₹ lakhs)")

            dataset = f"IPL 2021 PAS.csv"
            dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe

            streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(table)

            st.subheader("")
            st.write(f"To download the Pre Auction Summary data, please click the below button")
            st.subheader("")

            st.download_button(
                label=f"Download Pre Auction Summary data as CSV",
                data=csv,
                file_name=f'pre_auction_summary_data.csv',
                mime='text/csv',
            )

        with st.expander("Retained Players", expanded=False):

            st.subheader("")
            st.write("This section of the page consists the Retained players list along with team and salary")
            st.subheader("")

            dataset = f"IPL 2021 PART.csv"
            dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            retained_players_list = table['Player_Name'].tolist()
            retained_players_list.insert(0, "Select")

            columns = st.columns([2, 4, 2])
            with columns[0]:
                retained_players_choice = st.selectbox("Select or Enter the Player name", retained_players_list)
            with columns[2]:
                st.write("")
                st.write("")
                st.write("(Amount in ₹ lakhs)")

            if retained_players_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                location = retained_players_list.index(retained_players_choice)
                row = table.loc[[location]]
                streamlit_table(row.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(table)

            st.subheader("")
            st.write(f"To download the Retained Players data, please click the below button")
            st.subheader("")

            st.download_button(
                label=f"Download Retained Players data as CSV",
                data=csv,
                file_name=f'retained_players_data.csv',
                mime='text/csv',
            )

        with st.expander("Released Players", expanded=False):

            st.subheader("")
            st.write("This section of the page consists the Released players list along with team and salary")
            st.subheader("")

            dataset = f"IPL 2021 PARL.csv"
            dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            released_players_list = table['Player_Name'].tolist()
            released_players_list.insert(0, "Select")

            columns = st.columns([2, 4, 2])
            with columns[0]:
                released_players_choice = st.selectbox("Select or Enter the Player name", released_players_list)
            with columns[2]:
                st.write("")
                st.write("")
                st.write("(Amount in ₹ lakhs)")

            if released_players_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                location = released_players_list.index(released_players_choice)
                row = table.loc[[location]]
                streamlit_table(row.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(table)

            st.subheader("")
            st.write(f"To download the Released Players data, please click the below button")
            st.subheader("")

            st.download_button(
                label=f"Download Released Players data as CSV",
                data=csv,
                file_name=f'released_players_data.csv',
                mime='text/csv',
            )

        with st.expander("Player Transfers", expanded=False):

            st.subheader("")
            st.write("This section of the page consists the Player Transfers list along with team and salary")
            st.subheader("")

            dataset = f"IPL 2021 PAT.csv"
            dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            transferred_players_list = table['Player_Name'].tolist()
            transferred_players_list.insert(0, "Select")

            columns = st.columns([2, 4, 2])
            with columns[0]:
                transferred_players_choice = st.selectbox("Select or Enter the Player name", transferred_players_list)
            with columns[2]:
                st.write("")
                st.write("")
                st.write("(Amount in ₹ lakhs)")

            if transferred_players_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                location = transferred_players_list.index(transferred_players_choice)
                row = table.loc[[location]]
                streamlit_table(row.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(table)

            st.subheader("")
            st.write(f"To download the Player Transfers data, please click the below button")
            st.subheader("")

            st.download_button(
                label=f"Download Player Transfers data as CSV",
                data=csv,
                file_name=f'players_transfers_data.csv',
                mime='text/csv',
            )

    elif choice == "Auction":

        st.subheader("")
        st.subheader("Auction")
        st.write("Released/new players in pre-auction are auctioned and are open for all the franchises. Franchises "
                 "with the help of expert opinion participates in the auction and buys the players. So players "
                 "previously played for one franchise may play for another franchise in different seasons. All the "
                 "information regarding the auction of the players, their price at present and price earlier is "
                 "presented below.")
        st.subheader("")

        with st.expander("Auction Summary", expanded=True):

            st.subheader("")
            st.write("This section of the page consists the Auction summary of all teams in a tabular form")
            st.subheader("")

            dataset = f"IPL 2021 AS.csv"
            dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe

            columns = st.columns([7, 2])
            with columns[1]:
                st.write("(Amount in ₹ lakhs)")

            streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(table)

            st.subheader("")
            st.write(f"To download the Auction Summary data, please click the below button")
            st.subheader("")

            st.download_button(
                label=f"Download Auction Summary data as CSV",
                data=csv,
                file_name=f'auction_summary_data.csv',
                mime='text/csv',
            )

        with st.expander("Sold Players", expanded=False):

            st.subheader("")
            st.write("This section of the page consists the Sold players list along with team and salary")
            st.subheader("")

            dataset = f"IPL 2021 ASL.csv"
            dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            sold_players_list = table['Player_Name'].tolist()
            sold_players_list.insert(0, "Select")

            columns = st.columns([2, 4, 2])
            with columns[0]:
                sold_players_choice = st.selectbox("Select or Enter the Player name", sold_players_list)
            with columns[2]:
                st.write("")
                st.write("")
                st.write("(Amount in ₹ lakhs)")

            if sold_players_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                location = sold_players_list.index(sold_players_choice)
                row = table.loc[[location]]
                streamlit_table(row.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(table)

            st.subheader("")
            st.write(f"To download the sold Players data, please click the below button")
            st.subheader("")

            st.download_button(
                label=f"Download sold Players data as CSV",
                data=csv,
                file_name=f'sold_players_data.csv',
                mime='text/csv',
            )

        with st.expander("Unsold Players", expanded=False):

            st.subheader("")
            st.write("This section of the page consists the Unsold players list along with team and Salary")
            st.subheader("")

            dataset = f"IPL 2021 AUSL.csv"
            dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            unsold_players_list = table['Player_Name'].tolist()
            unsold_players_list.insert(0, "Select")

            columns = st.columns([2, 4, 2])
            with columns[0]:
                unsold_players_choice = st.selectbox("Select or Enter the Player name", unsold_players_list)
            with columns[2]:
                st.write("")
                st.write("")
                st.write("(Amount in ₹ lakhs)")

            if unsold_players_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                location = unsold_players_list.index(unsold_players_choice)
                row = table.loc[[location]]
                streamlit_table(row.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(table)

            st.subheader("")
            st.write(f"To download the Unsold Players data, please click the below button")
            st.subheader("")

            st.download_button(
                label=f"Download Unsold Players data as CSV",
                data=csv,
                file_name=f'unsold_players_data.csv',
                mime='text/csv',
            )

        with st.expander("Withdrawn Players", expanded=False):

            st.subheader("")
            st.write("This section of the page consists the Withdrawn players list along with team, replacement "
                     "player and salary")
            st.subheader("")

            dataset = f"IPL 2021 PAWD.csv"
            dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe
            withdrawn_players_list = table['Withdrawn_Player'].tolist()
            withdrawn_players_list.insert(0, "Select")

            columns = st.columns([2, 4, 2])
            with columns[0]:
                withdrawn_players_choice = st.selectbox("Select or Enter the Player name", withdrawn_players_list)
            with columns[2]:
                st.write("")
                st.write("")
                st.write("(Amount in ₹ lakhs)")

            if withdrawn_players_choice == "Select":
                streamlit_table(table.style.set_properties(**table_style))
            else:
                location = withdrawn_players_list.index(withdrawn_players_choice)
                row = table.loc[[location]]
                streamlit_table(row.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(table)

            st.subheader("")
            st.write(f"To download the Withdrawn players data, please click the below button")
            st.subheader("")

            st.download_button(
                label=f"Download Withdrawn players data as CSV",
                data=csv,
                file_name=f'withdrawn_players_data.csv',
                mime='text/csv',
            )

    elif choice == "Support Staff":

        st.subheader("")
        st.subheader("Support Staff")
        st.write("Apart from players, Franchises also do certain changes in Staff such as managers, coaches, "
                 "physiotherapists, and other managerial staff. Of all the staff coaches garner more interest among "
                 "IPL followers. Selection of Coaches also is observed with heightened interest among IPL fans. The "
                 "information about staff changes in every team is presented below.")
        st.subheader("")

        with st.expander("Staff Changes", expanded=True):

            st.subheader("")
            st.write("This section of the page consists the Support Staff summary of all teams in a tabular form")
            st.subheader("")

            dataset = f"IPL 2021 SS.csv"
            dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
            dataframe.index = npy.arange(1, len(dataframe) + 1)
            table = dataframe

            columns = st.columns([7, 2])
            with columns[1]:
                st.write("(Amount in ₹ lakhs)")

            streamlit_table(table.style.set_properties(**table_style))

            csv = convert_dataframe_to_csv(table)

            st.subheader("")
            st.write(f"To download the staff Changes data, please click the below button")
            st.subheader("")

            st.download_button(
                label=f"Download Staff Changes data as CSV",
                data=csv,
                file_name=f'staff_changes_data.csv',
                mime='text/csv',
            )
