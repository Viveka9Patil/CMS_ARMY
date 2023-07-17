import streamlit as st
import pandas as pd
from Addlogo import add_logo


st.set_page_config(page_title='CMS Platform',  layout='wide', page_icon='ArmyLog.png', 
                   initial_sidebar_state='expanded',
                   menu_items = {
                        'Report a Bug': "mailto:contact@lvlalpha.com",
                        'About' : "The App is powered by lvlAlpha Pvt. Ltd."
                   })

add_logo(logo_url = 'ArmyLogo.png')

st.title("User Activity Logs")

df = pd.read_csv("user_log.csv")

st.table(df)