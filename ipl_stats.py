import streamlit as st
import pandas as pa
import matplotlib.pyplot as plt
import seaborn as sns


def app():
    st.title("IPL Stats")

    match_data = pa.read_csv("WebsiteDatasets/IPL Matches 2008-2020.csv")
    ball_data = pa.read_csv("WebsiteDatasets/IPL Ball-by-Ball 2008-2020.csv")

    match_data['Season'] = pa.DatetimeIndex(match_data['date']).year
    match_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id': 'matches'})

    season_data = match_data[['id', 'Season']].merge(ball_data, left_on='id',
                                                     right_on='id', how='left').drop('id', axis=1)
    season = season_data.groupby(['Season'])['total_runs'].sum().reset_index()

    runs_per_season = pa.concat([match_per_season, season.iloc[:, 1]], axis=1)
    runs_per_season['Runs scored per match'] = runs_per_season['total_runs'] / runs_per_season['matches']
    runs_per_season.set_index('Season', inplace=True)
    runs_scored_per_season = season.set_index('Season')

    st.subheader("Total Matches played")
    with st.expander("Total Matches Played", expanded=True):

        st.write("This section of the page consists the analysis of total matches played by "
                 "all teams in all seasons since the beginning of the IPL")

        columns = st.columns([1.5, 1])
        with columns[0]:

            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.countplot(match_data['Season'])
            ax.set_xlabel('Season')
            ax.set_ylabel('Count')
            ax.set_title('Total matches played in each season', fontweight="bold")

            st.pyplot(fig)

        with columns[1]:

            st.subheader("")
            st.subheader("")
            st.write(f"Matches played so far in IPL are {match_data.shape[0]}")

    st.subheader("Total Runs Scored")
    with st.expander("Total Runs Scored", expanded=True):

        columns = st.columns([1.5, 1])
        with columns[0]:

            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.lineplot(data=runs_scored_per_season, palette="magma")
            ax.set_title('Total runs in each season', fontweight="bold")

            st.pyplot(fig)

        with columns[1]:

            st.subheader("")
            st.subheader("")
            st.write(f"Total runs scored in each season is given below in the table")
            st.write(runs_per_season)

    st.subheader("Toss Winners and Decisions")
    with st.expander("Toss Winners", expanded=True):

        columns = st.columns([1.5, 1])
        with columns[0]:

            toss = match_data['toss_winner'].value_counts()
            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.barplot(y=toss.index, x=toss, orient='h', palette="dark:salmon_r", saturation=1)
            ax.set_xlabel('# of tosses won')
            ax.set_ylabel('Teams')
            ax.set_title('No. of tosses won by each team', fontweight="bold")

            st.pyplot(fig)

        with columns[1]:

            st.subheader("")
            st.subheader("")

        columns = st.columns([1, 1.5])
        with columns[1]:

            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.countplot(x='Season', hue='toss_decision', data=match_data, palette="YlOrBr", saturation=1)
            ax.set_xlabel('Season')
            ax.set_ylabel('Count')
            ax.set_title('Toss Decision across seasons', fontweight="bold")

            st.pyplot(fig)

        with columns[0]:

            st.subheader("")
            st.subheader("")

        columns = st.columns([1.5, 1])
        with columns[0]:

            fig, ax = plt.subplots(figsize=(10, 5))
            sns.countplot(match_data.toss_decision[match_data.toss_winner == match_data.winner])
            ax.set_xlabel('Decision')
            ax.set_ylabel('Count')
            ax.set_title('Toss Decision count', fontweight="bold")

            st.pyplot(fig)

        with columns[1]:

            st.subheader("")
            st.subheader("")

    st.subheader("Top Run scorers")
    with st.expander("Top Run scorers", expanded=True):

        columns = st.columns([1.5, 1])
        with columns[0]:

            runs = ball_data.groupby(['batsman'])['batsman_runs'].sum().reset_index()
            runs.columns = ['Batsman', 'runs']
            y = runs.sort_values(by='runs', ascending=False).head(10).reset_index().drop('index', axis=1)

            fig, ax = plt.subplots(figsize=(10, 5))
            ax = sns.barplot(x=y['Batsman'], y=y['runs'], palette='flare', saturation=1)
            ax.set_xlabel('Player')
            ax.set_ylabel('Total Runs')
            ax.set_title('Top 10 run scorers in IPL', fontweight="bold")

            st.pyplot(fig)

        with columns[1]:

            st.subheader("")
            st.subheader("")

    st.subheader("Highest Man of Match Winners")
    with st.expander("Highest Man of Match Winners", expanded=True):

        columns = st.columns([1, 1.5])
        with columns[1]:

            fig, ax = plt.subplots(figsize=(10, 5))
            match_data.player_of_match.value_counts()[:10].plot(kind='bar')
            ax.set_xlabel('Players')
            ax.set_ylabel("Count")
            ax.set_title("Highest MOM award winners", fontweight="bold")

            st.pyplot(fig)

        with columns[0]:

            st.subheader("")
            st.subheader("")
