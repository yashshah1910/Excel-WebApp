import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import altair as alt
st.set_page_config(page_title='Nifty Data',
                   page_icon="🎯")

st.title('Welcome to Nifty Futures Data')
option = st.selectbox(
    'Select Option',
    ('Nifty-I Mid', 'Nifty-I Spread', 'Nifty-II Mid', 'Nifty-II Spread', 'Nifty-III Mid', 'Nifty-III Spread'))

nifty1 = 'NIFTY-I.NFO.csv'
nifty2 = 'NIFTY-II.NFO.csv'
nifty3 = 'NIFTY-III.NFO.csv'

n1 = pd.read_csv(nifty1)
n2 = pd.read_csv(nifty2)
n3 = pd.read_csv(nifty3)

nm1 = pd.DataFrame()
ns1 = pd.DataFrame()
nm2 = pd.DataFrame()
ns2 = pd.DataFrame()
nm3 = pd.DataFrame()
ns3 = pd.DataFrame()

nm1['Time'] = n1["Time"]
ns1['Time'] = n1["Time"]
nm2['Time'] = n2["Time"]
ns2['Time'] = n2["Time"]
nm3['Time'] = n3["Time"]
ns3['Time'] = n3["Time"]

nm1['Nifty-I Mid'] = 0.5 * (n1['BuyPrice'] + n1['SellPrice'])
ns1['Nifty-I Spread'] = n1['SellPrice']-n1['BuyPrice']
nm2['Nifty-II Mid'] = 0.5 * (n2['BuyPrice'] + n2['SellPrice'])
ns2['Nifty-II Spread'] = n2['SellPrice']-n2['BuyPrice']
nm3['Nifty-III Mid'] = 0.5 * (n3['BuyPrice'] + n3['SellPrice'])
ns3['Nifty-III Spread'] = n3['SellPrice']-n3['BuyPrice']

if (option == 'Nifty-I Mid'):
    st.header('Nifty-I Mid')
    st.dataframe(nm1, use_container_width=True)
    st.header('Chart')
    chart = alt.Chart(nm1).mark_line().encode(
        x=alt.X('Time', axis=alt.Axis(labelOverlap="greedy", grid=False)),
        y=alt.Y('Nifty-I Mid', scale=alt.Scale(domain=[17400, 17800])))
    st.altair_chart(chart, use_container_width=True)

elif (option == 'Nifty-I Spread'):
    st.header('Nifty-I Spread')
    st.dataframe(ns1, use_container_width=True)
    st.header('Chart')
    chart = alt.Chart(ns1).mark_line().encode(
        x=alt.X('Time', axis=alt.Axis(labelOverlap="greedy", grid=False)),
        y=alt.Y('Nifty-I Spread'))
    st.altair_chart(chart, use_container_width=True)

elif (option == 'Nifty-II Mid'):
    st.header('Nifty-II Mid')
    st.dataframe(nm2, use_container_width=True)
    st.header('Chart')
    chart = alt.Chart(nm2).mark_line().encode(
        x=alt.X('Time', axis=alt.Axis(labelOverlap="greedy", grid=False)),
        y=alt.Y('Nifty-II Mid', scale=alt.Scale(domain=[17400, 17800])))
    st.altair_chart(chart, use_container_width=True)

elif (option == 'Nifty-II Spread'):
    st.header('Nifty-II Spread')
    st.dataframe(ns2, use_container_width=True)
    st.header('Chart')
    chart = alt.Chart(ns2).mark_line().encode(
        x=alt.X('Time', axis=alt.Axis(labelOverlap="greedy", grid=False)),
        y=alt.Y('Nifty-II Spread'))
    st.altair_chart(chart, use_container_width=True)

elif (option == 'Nifty-III Mid'):
    st.header('Nifty-III Mid')
    st.dataframe(nm3, use_container_width=True)
    st.header('Chart')
    chart = alt.Chart(nm3).mark_line().encode(
        x=alt.X('Time', axis=alt.Axis(labelOverlap="greedy", grid=False)),
        y=alt.Y('Nifty-III Mid', scale=alt.Scale(domain=[17400, 17800])))
    st.altair_chart(chart, use_container_width=True)

elif (option == 'Nifty-III Spread'):
    st.header('Nifty-III Spread')
    st.dataframe(ns3, use_container_width=True)
    st.header('Chart')
    chart = alt.Chart(ns3).mark_line().encode(
        x=alt.X('Time', axis=alt.Axis(labelOverlap="greedy", grid=False)),
        y=alt.Y('Nifty-III Spread'))
    st.altair_chart(chart, use_container_width=True)

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)