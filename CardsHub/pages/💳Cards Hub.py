import streamlit as st
import streamlit_lottie as st_lottie
import sqlite3 as sql
import pandas as pd
import plotly.express as px
from PIL import Image
import requests
import json


connection = sql.connect("Cards.db")
cursor = connection.cursor()

# functions:
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

c1, c2,c3 = st.columns(3)
with c2:
    st_lottie(load_lottiefile("images/card_hand.json"), height = 111, quality = "high")
