import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
import io
from NLP_analysis import NLP_analysis_english, NLP_analysis_spanish
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
from spacy.lang.es.stop_words import STOP_WORDS

st.set_page_config(
    page_title="Word Party 📃",
    page_icon="📃",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/david-landeo/',
        'Report a bug': "https://www.linkedin.com/in/david-landeo/",
        'About': "This app allows you to get a wordcloud of your WhatsApp chat"
    }
)

hide_menu_style = """
                <style>
                footer {visibility: hidden; }
                </style>
                """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title('Word Party 📃')
st.markdown("Export any WhatsApp chat you desire and upload it below to visualize the most common words in a "
            "generated word cloud.")

if "image" not in st.session_state:
    st.session_state.image = False

if "language" not in st.session_state:
    st.session_state.language = "English"

if "n_words" not in st.session_state:
    st.session_state.n_words = 0


def show_image():
    st.session_state.image = True


# Upload the file to analyze
uploaded_file = st.file_uploader("Upload file to analyze", type=['txt'])