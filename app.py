import requests
import pandas as pd
import streamlit as st
from PIL import Image as img

url = "https://anime-db.p.rapidapi.com/anime"
headers = {"X-RapidAPI-Key": "8af8022ddcmsh06e9119b8cc13f3p1a0e1fjsn8138c83b2c3b",
            "X-RapidAPI-Host": "anime-db.p.rapidapi.com"}

list_genders = ["Fantasy", "Drama", "Action", "Award Winning", "Slice of Life", "Suspense", "Horror", "Ecchi", "Avant Garde", "Erotica"
                "Comedy", "Hentai", "Boys Love", "Gourmet", "Girls Love", "Romance", "Adventure", "Mystery", "Supernatural", "Sci-Fi"]


querystring = {"page":"1","size":"1000","genres": "Action","sortBy":"ranking","sortOrder":"asc"}

response = requests.get(url, headers=headers, params=querystring)

df = pd.DataFrame(response.json()["data"])

# Streamlit APP:
image = img.open("C:\\Users\\Carlos Reyes\\Desktop\\kimetsu.jpg")
st.image(image, caption="Kimetsu no Yaiba")

st.title("Your Anime Explorer")

st.text("Select the gender that you want to see: ")
genders = st.multiselect('Multiselect', list_genders, default=list_genders[0])










