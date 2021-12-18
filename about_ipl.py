import streamlit as st
import base64


def app():
    def image_to_bytes(image_path):
        image_file = open(image_path, "rb")
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        return encoded_image

    page_icon = f'<img src="data:image/png;base64,{image_to_bytes("WebsiteImages/about_ipl_page_icon.png")}"' \
                f' class="page_icon">'
    st.markdown(page_icon, unsafe_allow_html=True)
    st.subheader("")

    columns = st.columns([0.5, 2, 2])
    with columns[1]:
        st.image(f"data:image/png;"
                 f"base64,{image_to_bytes('WebsiteImages/intro_bcci_logo.png')}")
    with columns[2]:
        st.subheader("")
        st.write("The Indian Premier League (IPL) is a Twenty-20 cricket tournament league established with the "
                 "objective of promoting cricket in India and thereby nurturing young and talented players. The "
                 "league is an annual event where teams representing different Indian cities compete against each "
                 "other.")
        st.write("It was started by the Board of Control for Cricket in India (BCCI) in 2008 and has now become a "
                 "giant, remunerative cricket venture. The teams for IPL are selected by means of an auction.")
        st.subheader("")
        st.subheader("")

    st.subheader("Teams in IPL")
    columns = st.columns([2, 0.5, 2])
    with columns[0]:
        st.subheader("")
        st.write("Teams of IPL are:- ")
        st.write("Royal Challengers Bangalore, Kings XI Punjab, Delhi Daredevils, Mumbai Indians, Kolkata Knight "
                 "Riders, Rajasthan Royals, Deccan Chargers, Chennai Super Kings, Kochi Tuskers Kerala, "
                 "Pune Warriors, Sunrisers Hyderabad, Gujarat Lions, Rising Pune Supergiants and Delhi Capitals")
        st.write("The owners of the IPL franchises, includes major companies, Bollywood film stars, and media "
                 "moguls. The IPL is the most-attended cricket league in the world.")
    with columns[2]:
        st.image(f"data:image/png;"
                 f"base64,{image_to_bytes('WebsiteImages/body1_teams_logo.png')}")
    st.write("Due to the involvement of money, team spirit, city loyalty and a massive fan following, "
             "the outcome of matches is very important for all stake holders. This, in turn, is dependent on "
             "the complex rules governing the game, luck of the team (Toss), the ability of players and their "
             "performances on a given day. Various other natural parameters, such as the historical data "
             "related to players, play an integral role in predicting the outcome of a cricket match.")
    st.write("A report from Duff & Phelps said that one of the contributing factors in the rapid growth of the "
             "value of the Indian Premier League was signing a new television deal with Star India Private "
             "Limited, which engaged more viewers due to the fact that the IPL was transmitted to regional "
             "channels in 8 languages, rather than the previous deal, which saw the transmissions limited to "
             "sports networks with English language commentary.")
    columns = st.columns(2)
    with columns[0]:
        st.image(f"data:image/png;"
                 f"base64,{image_to_bytes('WebsiteImages/body1_iconic_logo.png')}")
    with columns[1]:
        st.write("The IPL is the most-attended cricket league in the world and in 2014 was ranked sixth by average "
                 "attendance among all sports leagues. In 2010, the IPL became the first sporting event in the "
                 "world to be broadcast live on YouTube. According to BCCI, the 2015 IPL season contributed ₹1,"
                 "150 crore (US$150 million) to the GDP of the Indian economy. The 2020 IPL season set a massive "
                 "viewership record with 31.57 million average impressions and with an overall consumption "
                 "increase of 23 per cent from the 2019 season.")
    st.write("From 2008 to 2012, the title sponsor was DLF, India's largest real estate developer, "
             "who had secured the rights with a bid of ₹200 crore (US$27 million) for five seasons. After the "
             "conclusion of the 2012 season, PepsiCo bought the title sponsorship rights for ₹397 crore (US$53 "
             "million) for the subsequent five seasons. The BCCI then transferred the title sponsorship rights "
             "for the remaining two seasons of the contract to Chinese smartphone manufacturer Vivo for ₹200 "
             "crore (US$27 million). In June 2017, Vivo retained the rights for the next five seasons ("
             "2018–2022) with a winning bid of ₹2,199 crore (US$290 million).")
    st.subheader("")

    st.subheader("Team's Performance")
    st.write("Out of the thirteen teams that have played in the Indian Premier League since its inception, "
             "one team has won the competition five times, one team has won the competition four times, "
             "one team has won the competition twice and three other teams have won it once. Mumbai Indians "
             "are the most successful team in league's history in terms of the number of titles won. The "
             "Chennai Super Kings have won 4 titles, the Kolkata Knight Riders have won two titles,"
             "[46] and the other three teams who have won the tournament are the Deccan Chargers, "
             "Rajasthan Royals and Sunrisers Hyderabad. The current champions are the Chennai Super Kings who "
             "defeated the Kolkata Knight Riders by 27 runs in the final of the 2021 season securing their "
             "fourth title.")

    columns = st.columns([1, 2, 0.5])
    with columns[1]:
        st.image(f"data:image/png;"
                 f"base64,{image_to_bytes('WebsiteImages/body2_winnings_logo.png')}")
    st.subheader("")
    st.subheader("")

    st.subheader("Orange Cap")
    st.write("The Orange Cap is awarded to the top run-scorer in the IPL during a season. It is an "
             "ongoing competition with the leader wearing the cap throughout the tournament until the "
             "final game, with the eventual winner keeping the cap for the season. Latest winner – "
             "Ruturaj Gaikwad - 635 Runs (2021).")
    st.subheader("Purple Cap")
    st.write("The Purple Cap is awarded to the top wicket-taker in the IPL during a season. It is an "
             "ongoing competition with the leader wearing the cap throughout the tournament until the "
             "final game, with the eventual winner keeping the cap for the season. Latest winner – "
             "Harshal Patel - 32 wickets (2021).")
    st.subheader("Most Valuable Player")
    st.write('The award was called the "man of the tournament" till the 2012 season. The IPL introduced '
             'the Most Valuable Player rating system in 2013, the leader of which would be named the '
             '"Most Valuable Player" at the end of the season. Latest winner – Harshal Patel (2021).')
    st.subheader("Fairplay Award")
    st.write("The Fair Play Award is given after each season to the team with the best record of fair "
             "play. The winner is decided on the basis of the points the umpires give to the teams. After "
             "each match, the two on-field umpires, and the third umpire, scores the performance of both "
             "the teams. Latest winner – Rajasthan Royals (2021).")
    st.subheader("Emerging Player Award")
    st.write('The award was presented for the "best under-19 player" in 2008 and "best under-23 player" '
             'in 2009 and 2010, being called "Under-23 Success of the Tournament". In 2011 and 2012, '
             'the award was known as "Rising Star of the Year", while, in 2013, it was called "Best Young '
             'Player of the Season". Since 2014, the award has been called the Emerging Player of the '
             'Year. In 2016, Mustafizur Rahman of Bangladesh was the first and only foreign player till '
             'date to win the Emerging Player of the Year award. Latest winner – Ruturaj Gaikwad (2021).')
    st.subheader("Most sixes Award")
    st.write("The Maximum Sixes Award, currently known as Unacademy Let's Crack It Sixes Award for "
             "sponsorship reasons, is presented to the batsman who hits the most sixes in a season of the "
             "IPL. Latest winner – KL Rahul - 30 Sixes (2021).")
