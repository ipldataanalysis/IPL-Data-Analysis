import streamlit as st
import pandas as pa
import matplotlib.pyplot as plt
import numpy as npy
import seaborn as sns
import base64


def app():
    def image_to_bytes(image_path):
        image_file = open(image_path, "rb")
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        return encoded_image

    page_icon = f'<img src="data:image/png;base64,{image_to_bytes("WebsiteImages/ipl_stats_page_icon.png")}"' \
                f' class="page_icon">'
    st.markdown(page_icon, unsafe_allow_html=True)
    st.subheader("")
    st.write("This page gives information about total matches, man of the match, top scorers in the match etc., "
             "IPL stats page assists user in retrieving, interpreting the player’s performance in particular or "
             "cumulative years. The analysis given in IPL Stats pages also helps the visitor to make intelligent "
             "conclusions on future performance of the player.")
    st.subheader("")

    years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

    match_data = pa.read_csv("WebsiteDatasets/IPL Matches 2008-2020.csv")
    ball_data = pa.read_csv("WebsiteDatasets/IPL Ball-by-Ball 2008-2020.csv")

    match_data['Season'] = pa.DatetimeIndex(match_data['date']).year
    match_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id': 'matches'})

    season_data = match_data[['id', 'Season']].merge(ball_data, left_on='id',
                                                     right_on='id', how='left').drop('id', axis=1)
    season = season_data.groupby(['Season'])['total_runs'].sum().reset_index()

    runs_per_season = pa.concat([match_per_season, season.iloc[:, 1]], axis=1)
    runs_per_season['Average Runs scored per match'] = runs_per_season['total_runs'] / runs_per_season['matches']
    runs_per_season.set_index('Season', inplace=True)
    runs_scored_per_season = season.set_index('Season')

    table_style = {
        'color': 'white',
        'font-size': '20px',
        'background-color': '#b0e0fa',
        'text-align': 'center'
    }

    st.subheader("Total Matches played")
    with st.expander("Total Matches Played", expanded=True):
        columns = st.columns([1.5, 1])
        with columns[0]:

            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.countplot(match_data['Season'], palette="tab10")
            ax.set_xlabel('Season')
            ax.set_ylabel('Count')
            ax.set_title('Total matches played in each season', fontweight="bold")
            st.pyplot(fig)

        with columns[1]:
            st.subheader("")
            total_matches_data = match_data['Season']
            dictionary = {}
            count = []
            for year in years:
                number = (total_matches_data == year).sum()
                count.append(number)
            dictionary['years'] = years
            dictionary['Count'] = count
            frame = pa.DataFrame.from_dict(dictionary)
            st.dataframe(frame.style.set_properties(**table_style))

    st.subheader("Total Runs Scored")
    with st.expander("Total Runs Scored", expanded=True):

        columns = st.columns([1.5, 1])
        with columns[0]:

            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.lineplot(data=runs_scored_per_season, palette="dark:salmon_r")
            ax.set_title('Total runs in each season', fontweight="bold")

            st.pyplot(fig)

        with columns[1]:
            st.subheader("")
            total_runs = runs_per_season
            total_runs.index = npy.arange(1, len(total_runs) + 1)
            total_runs['Season'] = years
            total_runs = total_runs[['Season', 'matches', 'total_runs', 'Average Runs scored per match']]
            st.dataframe(total_runs.style.set_properties(**table_style))

    st.subheader("Toss Winners and Decisions")
    with st.expander("Toss Winners and Decisions", expanded=True):

        columns = st.columns([1.5, 1])
        with columns[0]:

            toss = match_data['toss_winner'].value_counts()
            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.barplot(y=toss.index, x=toss, orient='h', palette="icefire", saturation=1)
            ax.set_xlabel('# of tosses won')
            ax.set_ylabel('Teams')
            ax.set_title('No. of tosses won by each team', fontweight="bold")

            st.pyplot(fig)

        with columns[1]:
            toss_ranks = toss
            st.dataframe(toss_ranks)

        columns = st.columns([1, 1.5])
        with columns[1]:

            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.countplot(x='Season', hue='toss_decision', data=match_data, palette="YlOrBr", saturation=1)
            ax.set_xlabel('Season')
            ax.set_ylabel('Count')
            ax.set_title('Toss Decision across seasons', fontweight="bold")

            st.pyplot(fig)

        with columns[0]:

            toss_decisions_across_seasons = pa.DataFrame()
            toss_decisions_across_seasons['Season'] = match_data['Season']
            toss_decisions_across_seasons['toss_decision'] = match_data['toss_decision']
            st.dataframe(toss_decisions_across_seasons.style.set_properties(**table_style))

        columns = st.columns([1.5, 1])
        with columns[0]:

            decision_count = match_data.toss_decision[match_data.toss_winner == match_data.winner]
            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.countplot(decision_count)
            ax.set_xlabel('Decision')
            ax.set_ylabel('Count')
            ax.set_title('Toss Decision count', fontweight="bold")

            st.pyplot(fig)

        with columns[1]:
            toss_decisions = decision_count
            toss_decisions = toss_decisions.reset_index().drop('index', axis=1)
            st.dataframe(toss_decisions.style.set_properties(**table_style))

    st.subheader("Top Run scorers")
    with st.expander("Top Run scorers", expanded=True):

        columns = st.columns([1.5, 1])
        with columns[0]:

            runs = ball_data.groupby(['batsman'])['batsman_runs'].sum().reset_index()
            runs.columns = ['Batsman', 'runs']
            y = runs.sort_values(by='runs', ascending=False).head(10).reset_index().drop('index', axis=1)

            fig, ax = plt.subplots(figsize=(11, 5))
            ax = sns.barplot(x=y['Batsman'], y=y['runs'], palette='flare', saturation=1)
            ax.set_xlabel('Player')
            ax.set_ylabel('Total Runs')
            ax.set_title('Top 10 run scorers in IPL', fontweight="bold")

            st.pyplot(fig)

        with columns[1]:
            scorers = runs.sort_values(by='runs', ascending=False).reset_index().drop('index', axis=1)
            st.dataframe(scorers.style.set_properties(**table_style))

    st.subheader("Highest Man of Match Winners")
    with st.expander("Highest Man of Match Winners", expanded=True):

        columns = st.columns([1, 1.5])
        with columns[1]:

            winners = match_data.player_of_match.value_counts()
            fig, ax = plt.subplots(figsize=(10, 5))
            ax = winners[:10].plot(kind='bar')
            ax.set_xlabel('Players')
            ax.set_ylabel("Count")
            ax.set_title("Highest MOM award winners", fontweight="bold")

            st.pyplot(fig)

        with columns[0]:
            st.dataframe(winners)
