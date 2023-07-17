import streamlit as st
import pandas as pd
import numpy as np
from Addlogo import add_logo
import plotly.express as px


st.set_page_config(page_title='CMS Platform',  layout='wide', page_icon='ArmyLogo.png',
                   initial_sidebar_state='expanded',
                   menu_items = {
                        'Report a Bug': "mailto:contact@lvlalpha.com",
                        'About' : "The App is powered by lvlAlpha Pvt. Ltd."
                   })

add_logo(logo_url = 'ArmyLogo.png')

# Container for the Header
with st.container():
    t1, t2 = st.columns([0.9, 0.1])
    
    t1.title("Casualty Management Platform")
    t2.image('lvlAlpha_logo.png', width = 150)

with st.container():
    c1, c2, c3 = st.columns([0.25, 0.25, 0.5])

    c1.metric(label = 'Active Devices', value = '200', delta = '12', 
              help = 'Number of Active Devices currently deployed and Working')
    c2.metric(label = 'Injuries' , value = '0',
              help = 'Indicates the amount of people injured currently')
    c3.header("Jawaan Health Overview")

col1, col2 = st.columns([0.5, 0.5])

with col1:
    st.header("Past record")

    tab1, tab2, tab3 = st.tabs(["VOC", "Temperature", "Humidity"])

    with tab1:
        st.subheader("Volatile Organic Compound Variation Log")

        vocDF = pd.read_csv("voc_data.csv")
        fig = px.line(vocDF, x = 'Days', y = 'Concentration', color = 'Compound', markers = True)
        fig.update_layout(title_text = 'VOC concentration in µg/m3')
        st.plotly_chart(fig, use_container_width = True)

    
    with tab2:
        st.subheader("Temperature Variation Log")

        tempDF = pd.read_csv("temperature.csv")
        fig = px.line(tempDF, x = 'Days', y = 'Avg temp (in degree celsius)', markers = True)
        fig.update_layout(title_text = 'Temperature in degreee Celsius')
        fig.update_yaxes(range = [20, 45])
        st.plotly_chart(fig, use_container_width = True)

    with tab3:
        st.subheader("Humidity Variation Log")

        hdf = pd.read_csv("humidity.csv")
        fig = px.line(hdf, x = 'Days', y = 'Humidity (in %)', markers = True)
        fig.update_layout(title_text = 'Humidity in Percentage')
        fig.update_yaxes(range = [0, 100])
        st.plotly_chart(fig, use_container_width = True)


with col2:

    df = pd.read_csv('mock_data.csv')
    #df = pd.DataFrame(
    #np.random.randn(10, 20),
    #columns=('col %d' % i for i in range(20)))

    #st.dataframe(df.style.highlight_max(axis=0))
    
    st.dataframe(df, use_container_width = True)

