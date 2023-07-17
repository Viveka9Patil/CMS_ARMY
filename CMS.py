import streamlit as st
from Addlogo import add_logo

st.set_page_config(

    page_icon=('ArmyLogo.png'),
    
    page_title=('CMS Platform')

    
)
st.write("\n\n")
with st.container():
    t1,t2= st.columns([0.9, 0.1])
    t1.title("Casualty Management Platform")
    t2.image('lvlAlpha_logo.png', width = 150)


add_logo(logo_url = 'ArmyLogo.png')

st.sidebar.success=('Select a page.') 

