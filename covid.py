import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

import matplotlib.pyplot as plt
DATE_TIME = "date/time"
DATA_URL = pd.read_csv(
    "C:\\Users\\aksha\\Desktop\\covid19.csv"
)
DATA_URL_1 = pd.read_csv("C:\\Users\\aksha\\Desktop\\covid19_2.csv")
DATA_URL_2 = pd.read_csv("C:\\Users\\aksha\\Desktop\\datewise.csv")

st.title("COVID-19 Pune")
st.markdown("This application is a Streamlit dashboard that can be used "
            "to analyze Covid-19 Outbreak in Pune 💥")

st.dataframe(DATA_URL,width=1000,height=1000)

st.subheader("Ward Data As of: 15-May-20")
st.write(DATA_URL_1)
st.subheader("DATEWISE As of: 16-May-20")
st.write(DATA_URL_2)
st.subheader("WARD vs POSITIVE CASES")
fig = px.scatter(DATA_URL_1, x="Ward", y="Positive Cases", color="Ward", marginal_y="rug", marginal_x="histogram")
st.write(fig)
st.subheader("DATEWISE As of: 16-May-20")
fig = px.scatter(DATA_URL_2, x="Date", y="Confirmed cases")
st.write(fig)
df=DATA_URL_1['Deaths Cases']+DATA_URL_1['Recovered Cases']
st.header("Choose your ward")
select = st.selectbox('WARDS', ['Aundh - Baner','Kothrud - Bavdhan','Sinhagad Road','Warje - Karvenagar','Shivajinagar - Ghole Road','Kasaba - Vishrambaugwada',
                                'Dhankawadi - Sahakarnagar','Bhawani Peth','Bibwewadi','Dhole Patil Road','Yerwada - Kalas - Dhanori',
                                'Nagar Road - Wadgaon Sheri','Wanawadi - Ramtekdi','Kondhwa - Yewalerwadi','Hadapsar - Mundhawa','Outside'])
DATA_URL_3=pd.read_csv("C:\\Users\\aksha\\Desktop\\Aundh - Baner.csv")
if select =='Aundh - Baner':
    DATA_URL_3 = pd.read_csv("C:\\Users\\aksha\\Desktop\\Aundh - Baner.csv")
if select == 'Kothrud - Bavdhan':
    DATA_URL_3 = pd.read_csv("C:\\Users\\aksha\\Desktop\\Kothrud - Bavdhan.csv")
if select == 'Sinhagad Road':
    DATA_URL_3 = pd.read_csv("C:\\Users\\aksha\\Desktop\\Sinhagad Road.csv")
if select == 'Warje - Karvenagar':
    DATA_URL_3 = pd.read_csv("C:\\Users\\aksha\\Desktop\\Warje - Karvenagar.csv")

#fig = px.scatter(DATA_URL_3, x="Dates", y="Confirmed")
#st.write(fig)

#fig1 = plt.figure()
#plt.plot("Dates","Confirmed", data=DATA_URL_3, linestyle='-', marker='o')

#st.plotly_chart(fig1)
import plotly.graph_objects as go

x=DATA_URL_3['Dates']
y=DATA_URL_3['Confirmed']
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y,
                    mode='lines+markers',
                    name='lines+markers'))

st.plotly_chart(fig)