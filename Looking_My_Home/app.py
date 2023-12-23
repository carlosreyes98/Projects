import pandas as pd
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from datetime import date
from PIL import Image
import requests
import warnings
import json
import os
from urllib.request import urlopen

#setting the page config
st.set_page_config(page_title="Looking My Home ", page_icon=":house:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
# calling the api, 1 time per month, saving the data in a csv file and loading it and returning a dataframe
def get_data_and_loaddf():
    #getting the current date
    current_month_year = str(date.today()).split("-")[1] + "-" + str(date.today()).split("-")[0]
    # st.secrets call the secret api key from streamlit
    headers = {"accept": "application/json",
            "X-Api-Key": st.secrets["api_key"]}
    # list of urls to call
    list_calls = ["https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=1&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=2&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=3&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=4&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=1&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=2&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=3&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=4&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Apartment&bedrooms=1&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Apartment&bedrooms=2&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Apartment&bedrooms=3&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Apartment&bedrooms=4&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=1&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=2&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=3&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=4&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Apartment&bedrooms=1&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Apartment&bedrooms=2&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Apartment&bedrooms=3&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Condo&bedrooms=2&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Condo&bedrooms=3&status=Active&limit=500"]

    # checking if the csv file of the current month already exists
    if not os.path.exists(f"Looking_My_Home/rentcast_data_{current_month_year}.csv"):
        df = pd.DataFrame()

        for i in list_calls:
            # calling the api and concatinating in DataFrame
            response = requests.get(i, headers=headers).json()
            df = pd.concat([df, pd.DataFrame(response)], ignore_index=True)
                   
        #saving the dataframe to a csv file       
        df.to_csv(f"Looking_My_Home/rentcast_data_{current_month_year}.csv", index=False)
        
        # creating and cleaning the dataframe
        df = pd.read_csv(f"Looking_My_Home/rentcast_data_{current_month_year}.csv")
        df.dropna(how="all", inplace=True)
        df.drop_duplicates(inplace=True)
        return df
    
    else:
        df = pd.read_csv(f"Looking_My_Home/rentcast_data_{current_month_year}.csv")
        df.dropna(how="all", inplace=True)
        df.drop_duplicates(inplace=True)
        return df

# load lottie animation
def lottie_sidebar(path):
    with open(path, "r") as f:
        lottie_home = json.load(f)
    with st.sidebar:
	    st_lottie(lottie_home, height = 100, quality = "high")


lottie_sidebar("Looking_My_Home/home1.json")

def display_ga_map(dataframe):
    # Load GeoJSON data for Georgia
    with open("Looking_My_Home//GA.geojson") as geojson_file:
        geojson_data = json.load(geojson_file)
    # Create the choropleth map
    fig = px.choropleth_mapbox(
        dataframe,
        geojson=geojson_data,
        locations='state',
        mapbox_style="carto-positron",
        center={"lat": 32.6782, "lon": -83.2220},  # Georgia center
        zoom=6)
    st.plotly_chart(fig)


        
display_ga_map(get_data_and_loaddf())
    
    
        


