import views.Zoologico as zooView
import streamlit as st


if __name__ == '__main__':
    st.set_page_config(
        page_title='San Diego´s Zoo',
        page_icon='logo.png',
        layout="wide",

    )

    st.title(':green[San Diego´s Zoo] :elephant:')
    zoologico = zooView.Zoologico("South Hills")
    zoologico.menu()

