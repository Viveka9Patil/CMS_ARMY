import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static

# Set page configuration and add logo
st.set_page_config(
    page_title='CMS Platform',
    layout='wide',
    page_icon='ArmyLogo.png',
    initial_sidebar_state='expanded',
    menu_items={
        'Report a Bug': "mailto:contact@lvlalpha.com",
        'About': "The App is powered by lvlAlpha Pvt. Ltd."
    }
)

# Function to add logo
def add_logo(logo_url):
    logo_html = f'<img src="{logo_url}" width="150">'
    st.sidebar.markdown(logo_html, unsafe_allow_html=True)

add_logo(logo_url='ArmyLogo.png')

# Container for the Header
with st.container():
    t1, t2 = st.columns([0.9, 0.1])
    t1.title("Casualty Management Platform")
    t2.image('lvlAlpha_logo.png', width=150)

with st.container():
    c1, c2, c3, c4 = st.columns([0.25, 0.25, 0.25, 0.25])

    c1.metric(label='All Devices', value='240',
              help='Number of All Devices currently deployed and Working')
    c2.metric(label='Active Devices', value='200', delta='12',
              help='Number of Active Devices currently deployed and Working')
    c3.metric(label='Not Active Devices', value='40', delta='3',
              help='Number of Not Active Devices currently deployed and Working')
    c4.metric(label='Injuries', value='0',
              help='Indicates the amount of people injured currently')

st.title("Health Condition")

with st.container():
    selectCanvas = st.radio("Body Layer",
                            options=('ALL', 'STABLE', 'UNSTABLE', 'CRITICAL'), horizontal=True, label_visibility='hidden')

df = pd.DataFrame(
    np.random.randn(75, 2) / [200, 200] + [28.3839, 77.3332],
    columns=['lat', 'lon'])

# Generate Folium map using Streamlit
st.write("Folium Map:")
m = folium.Map(location=[28.3839, 77.3332], zoom_start=13)

# Add scatter plot to the Folium map based on body layer
for i in range(25):
    color = 'red' if selectCanvas == 'STABLE' or selectCanvas == 'ALL' else "transparent"
    folium.CircleMarker(
        location=[df['lat'][i], df['lon'][i]],
        radius=5,
        color=color,
        fill=True,
        fill_color=color
    ).add_to(m)

for i in range(26, 50):
    color = 'green' if selectCanvas == 'UNSTABLE' or selectCanvas == 'ALL' else "transparent"
    folium.CircleMarker(
        location=[df['lat'][i], df['lon'][i]],
        radius=5,
        color=color,
        fill=True,
        fill_color=color
    ).add_to(m)

for i in range(50, 75):
    color = 'orange' if selectCanvas == 'CRITICAL' or selectCanvas == 'ALL' else 'transparent'
    folium.CircleMarker(
        location=[df['lat'][i], df['lon'][i]],
        radius=5,
        color=color,
        fill=True,
        fill_color=color
    ).add_to(m)

# Render Folium map in Streamlit
folium_static(m)
