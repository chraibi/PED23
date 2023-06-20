import streamlit as st
import plotly.graph_objects as go
from itertools import groupby

schedule_data = [
    {
        "day": "Day 1",
        "time": "8:00 - 9:00",
        "session": "Reception and registration",
    },
    {
        "day": "Day 1",
        "time": "9:00 - 9:10",
        "session": "Opening (Blauwe zaal)",
    },
    {
        "day": "Day 1",
        "time": "9.10 - 10.00",
        "session": "Keynote lecture (Blauwe zaal): Max Kinateder",
    },
    {
        "day": "Day 1",
        "time": "10:05 - 11:15",
        "session": "Session A (Room 4): Christina Mayr, Ahmed Syed, Tobias Kretz",
    },
    {
        "day": "Day 1",
        "time": "10:05 - 11:15",
        "session": "Session B (Room 5): Martyn Amos, Emiliano Cristiani, Matteo Butano",
    },
    {
        "day": "Day 1",
        "time": "11:45 - 12:55",
        "session": "Session A (Room 4): Thomas Matyus, Mineko Imanishi, Steve Gwynne",
    },
    {
        "day": "Day 1",
        "time": "11:45 - 12:55",
        "session": "Session B (Room 5): Angelika Kneidl, Michael Spearpoint, Adrien Gregorj",
    },
    {
        "day": "Day 1",
        "time": "13:55 - 15:05",
        "session": "Session A (Room 4): Kei Yoshida, Paul Geoerg, Nikolai Bode",
    },
    {
        "day": "Day 1",
        "time": "13:55 - 15:05",
        "session": "Session B (Room 5): Giuseppe Vizzari, Jun Zhang, Asim Siddiqui",
    },
    {
        "day": "Day 1",
        "time": "16:05 - 17:15",
        "session": "Session A (Room 4): Sina Feldmann, Thomas Chatagnon, Geert van der Vleuten",
    },
    {
        "day": "Day 1",
        "time": "16:05 - 17:15",
        "session": "Session B (Room 5): Carl Kjaergaard, Evandro José da Silva, Jakob Cordes",
    },
    {
        "day": "Day 1",
        "time": "17:30",
        "session": "Group picture and Drinks",
    },
    # ========================== Day 2
    {"day": "Day 2", "time": "8:40 - 9:10", "session": "Coffee & Tea"},
    {
        "day": "Day 2",
        "time": "9:10 - 10:00",
        "session": "Keynote Speaker: Denise McGrath",
    },
    {
        "day": "Day 2",
        "time": "10:05 - 11:15",
        "session": "Session A (Room 4): Pavel Hrabák, Rainald Löhner, Simon Rahn",
    },
    {
        "day": "Day 2",
        "time": "10:05 - 11:15",
        "session": "Session B (Room 5): Krisztina Konya, Enrico Ronchi, Bilal Farooq",
    },
    {
        "day": "Day 2",
        "time": "11:45 - 12:55",
        "session": "Session A (Room 4): Claudio Feliciani, Benoit Gaudou, Peter Lawrence",
    },
    {
        "day": "Day 2",
        "time": "11:45 - 12:55",
        "session": "Session B (Room 5): Armin Seyfried, Ezel Üsten, Milad Haghani",
    },
    {
        "day": "Day 2",
        "time": "13:55 - 15:05",
        "session": "Session A (Room 4): Leo Willem Menzemer, Wei Xie, Capucine-Marin Dubroca-Voisin",
    },
    {
        "day": "Day 2",
        "time": "13:55 - 15:05",
        "session": "Session B (Room 5): Anna Sieben / Tom Postmes, Rabia Kodapanakkal, Anne Templeton",
    },
    {"day": "Day 2", "time": "", "session": "Poster session (Senaatszaal)"},
    {
        "day": "Day 2",
        "time": "16:00",
        "session": "Social event: guided city tour 's-Hertogenbosch (includes bus transport and drinks)",
    },
    {
        "day": "Day 2",
        "time": "19:30",
        "session": "Social dinner: Eindhoven, Radio Royaal",
    },
    # =============== Day 3
    {"day": "Day 3", "time": "8:40 - 9:10", "session": "Coffee & Tea"},
    {
        "day": "Day 3",
        "time": "9:10 - 10:00",
        "session": "Keynote Speaker: Daniel R. Parisi",
    },
    {
        "day": "Day 3",
        "time": "10:05 - 11:15",
        "session": "Session A (Room 4): Caspar Pouw, Francesco Zanlungo, Juliane Adrian",
    },
    {
        "day": "Day 3",
        "time": "10:05 - 11:15",
        "session": "Session B (Room 5): Celeste Richard, Yan Feng, Arco van Beek",
    },
    {
        "day": "Day 3",
        "time": "11:45 - 12:55",
        "session": "Session A (Room 4): Iñaki Echeverría, Karthika Sobhana, Guanning Wang",
    },
    {"day": "Day 3", "time": "", "session": "Closing words"},
    {"day": "Day 3", "time": "", "session": "Lunch"},
]


grouped_data = groupby(schedule_data, key=lambda x: x["day"])

day1, day2, day3 = st.tabs(["Day 1", "Day 2", "Day 3"])
figs = {}

for day, group in grouped_data:
    # Sort the sessions within the day by time in descending order
    sorted_group = group  # sorted(group, key=lambda x: x["time"])
    fig = go.Figure()

    for session in sorted_group:
        fig.add_trace(
            go.Scatter(
                x=[session["time"]],
                y=[session["session"]],
                mode="markers",
                marker=dict(size=10),
                name=session["session"],
                hovertemplate="%{y}<extra></extra>",
            )
        )

    fig.update_layout(
        title="Conference Schedule",
        xaxis_title="Time",
        yaxis_title="Session",
        showlegend=False,
    )

    figs[day] = fig

with day1:
    st.plotly_chart(figs["Day 1"])

with day2:
    st.plotly_chart(figs["Day 2"])

with day3:
    st.plotly_chart(figs["Day 3"])
