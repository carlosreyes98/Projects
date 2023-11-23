import pandas as pd
import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Naruverse", page_icon="🍥")

url = "https://narutodb.xyz/api/character?page=1&limit=1431"

response = requests.get(url).json()

df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)




st.title("Naruto Characters")
st.image(Image.open("Naruto_app/images/characters.png"), use_column_width= True, clamp=True)
st.warning("Choose the character you want to know more about")

character = st.selectbox("Choose the character", df["name"].unique())

st.write(df[df["name"] == character])



'''def show_character(character):
    df = df[df["name"] == character]
    
    return st.write(df)

show_character(character)'''
