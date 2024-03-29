import requests
import pandas as pd
import streamlit as st
from PIL import Image
from io import BytesIO

# check API details bellow:
url = "https://anime-db.p.rapidapi.com/anime"
headers = {"X-RapidAPI-Key": "8af8022ddcmsh06e9119b8cc13f3p1a0e1fjsn8138c83b2c3b",
            "X-RapidAPI-Host": "anime-db.p.rapidapi.com"}
query = {"page": "1", "size": "10000"}
list_genders = ["Fantasy", "Drama", "Action", "Award Winning", "Slice of Life", "Suspense", "Horror", "Ecchi", "Avant Garde", "Erotica"
                "Comedy", "Hentai", "Boys Love", "Gourmet", "Girls Love", "Romance", "Adventure", "Mystery", "Supernatural", "Sci-Fi"]


# Streamlit APP:
picture = Image.open("Anime_recomendation/kimetsu.jpg")
st.image(picture, caption="WELCOME TO THE ANIME EXPLORER :)")

st.title("Fill your app preferences")

st.text("                                                                                                                              ")
st.text("                                                                                                                              ")
st.text("                                                                                                                              ")

genders = st.selectbox('Select the gender that you want to see: ', list_genders)

type = st.radio(" Movie or TV Serie?: ", ("Movie", "TV"), index=0)


if type == "TV":
    key = False

episodes = st.selectbox("How many episodes do you want to see: ", options= ["1-50", "51-100", "100-200", "200-1000"],disabled= key, placeholder= "Chose a range")

status = st.radio(" Status: ", ("Finished Airing", "Not yet aired"), index=0)


#search button:  
button = st.button("Search", type= "primary")   



if button:    
    #Calling API:
    response = requests.get(url, headers=headers, params=query)
    df = pd.DataFrame(response.json()["data"])
    
    df = df[df["type"] == type]
    
    df = df[df["status"] == status]
    
    df = df[df["genres"].apply(lambda x: genders in x)]
    
        
    if type == "TV":
        df = df[df["episodes"] <= int(str(episodes).split("-")[1])] 
        df = df[df["episodes"] >= int(str(episodes).split("-")[0])]
    
    df = df.sort_values(by="ranking", ascending=True).head(5)
        
    for i,y, z in zip(df["image"], df["title"], df["synopsis"]):
        
        response = requests.get(i)
        
        image_data = response.content

        st.header(y)
        st.image(Image.open(BytesIO(image_data)))
        st.text(z)
        
        st.text("                                                                                                                              ")
        st.text("                                                                                                                              ")
        st.text("                                                                                                                              ")

        
    st.balloons()
