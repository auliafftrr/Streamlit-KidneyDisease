# import library yang dibutuhkan
import pickle
import streamlit as st
from web_functions import load_data
from PIL import Image

from Tabs import home, predict

#load model
model_file = pickle.load(open("model_dt.pkl", "rb"))

Tabs = {
    "Home": home,
    "Prediction": predict
}

# membuat sidebar
st.sidebar.title("Navigasi")

# membuat radio option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# load dataset
df, x, y = load_data()

# CSS untuk styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .stRadio label {
        font-size: 16px;
        margin-bottom: 10px;
    }
    .stTextInput label {
        font-size: 16px;
        margin-bottom: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# kondisi call app function
if page in ["Prediction"]:
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()
