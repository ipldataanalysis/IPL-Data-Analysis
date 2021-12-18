import streamlit as st
import matplotlib.pyplot as plt
import pandas as pa
import numpy as npy
import base64


def app():
    def image_to_bytes(image_path):
        image_file = open(image_path, "rb")
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        return encoded_image

    page_icon = f'<img src="data:image/png;base64,{image_to_bytes("WebsiteImages/points_table_page_icon.png")}"' \
                f' class="page_icon">'
    st.markdown(page_icon, unsafe_allow_html=True)
    st.subheader("")

    years = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019",
             "2020", "2021"]

    points_table_dataframes = []
    for year in years:

        dataset = f"IPL {year} PT.csv"
        dataframe = pa.read_csv(f"WebsiteDatasets/{dataset}")
        dataframe.index = npy.arange(1, len(dataframe) + 1)
        points_table_dataframes.append(dataframe)

    st.subheader("")
    st.write("This page of the web app is the most viewed page as it gives the performance of teams in a "
             "particular year as well as in cumulative years. The points table helps the viewer in "
             "assessing the team and also helps in predicting the future of the team in coming games and "
             "seasons. The information provided is from the season 2008 to 2021.")
    st.subheader("")

    choice = st.selectbox("Select a season to view the Standing of teams in IPL", years)
    table = points_table_dataframes[years.index(choice)]

    def streamlit_table(dataframe_styled):
        st.dataframe(dataframe_styled)

    table_style = {
        'color': 'white',
        'font-size': '20px',
        'background-color': '#5aa70a',
        'text-align': 'center'
    }

    with st.expander(f"Points Table of the year {choice}", expanded=True):

        st.subheader("")
        st.write("The points table gives information about the team’s performance in particular season. The table has "
                 "information about the team’s standing, games played, won matches, lost matches, tied matches, N/R, "
                 "Net run rate, average runs scored for and against the rival teams, and total points scored in that "
                 "particular season.")
        st.subheader("")

        team_list = table['Team'].tolist()
        team_list.insert(0, "Select")

        columns = st.columns([2, 4, 1])
        with columns[0]:
            team_choice = st.selectbox("Select or Enter the team name", team_list)

        if team_choice == "Select":
            streamlit_table(table.style.set_properties(**table_style))
        else:
            location = team_list.index(team_choice)
            row = table.loc[[location]]
            streamlit_table(row.style.set_properties(**table_style))

        @st.cache
        def convert_dataframe_to_csv(df):
            return df.to_csv().encode('utf-8')

        csv = convert_dataframe_to_csv(table)

        st.subheader("")
        st.write(f"To download the points table data of the year {choice}, please click the below button")
        st.subheader("")

        st.download_button(
            label=f"Download {choice} data as CSV",
            data=csv,
            file_name=f'points_table_{choice}.csv',
            mime='text/csv',
        )

    st.subheader("")
    st.subheader("Average Matches Won")
    st.subheader("")

    content = "We can understand the required team’s performance for cumulative seasons with the help of the graph." \
              " The graph depicts the team’s wins for all the seasons played and also gives the teams average winning" \
              " performance."
    st.subheader("")
    st.write(content)
    st.subheader("")

    def graph_function(count):
        team = table["Team"][count]
        if team != "Pune Warriors India PWI":
            with st.expander(f"{team}", expanded=True):

                x_values = []
                y_values = []
                for count_team in range(0, len(points_table_dataframes)):

                    data = points_table_dataframes[count_team]
                    number = data[data["Team"] == team].index.values

                    if number.size > 0:
                        x_values.append(int(years[count_team]))
                        y_values.append(int(data["Won"][number]))

                x_values = npy.array(x_values)
                y_values = npy.array(y_values)
                average = npy.average(y_values)

                fig, ax = plt.subplots()
                ax.plot(x_values, y_values)
                ax.axhline(y=int(average), color='red', linestyle='--')
                ax.set_xlabel("Seasons")
                ax.set_ylabel("Matches")
                ax.set_title("Average Wins")
                st.pyplot(fig)

                st.subheader("")
                st.write(f"The Average wins by {team} is {int(average)}")
        else:
            pass

    columns = st.columns(3)
    with columns[0]:

        team_number = 1
        while team_number <= len(table):
            graph_function(team_number)
            team_number = team_number + 3

    with columns[1]:

        team_number = 2
        while team_number <= len(table):
            graph_function(team_number)
            team_number = team_number + 3

    with columns[2]:

        team_number = 3
        while team_number <= len(table):
            graph_function(team_number)
            team_number = team_number + 3
