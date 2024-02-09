import pandas as pd
import sqlite3 as sql
import streamlit as st
import streamlit_lottie as st_lottie
from PIL import Image
import json

#setting credit card page icon and title
st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# load css
local_css("CardsHub\style.css")

# DF
df = pd.DataFrame(columns= ["Issuer_Name", "Name", "Category", "Rewards_rate", "Welcome_Bonus", "Annual_Fee", 
                            "Recommended_Credit_Score", "Pros", "Cons", "Image_URL"])

def save_card():
    df.index[len(df)] = pd.Series(card_form)
    

def show_cards():
    st.dataframe(df)


def to_sql():
    conn = sql.connect('cards.db')
    df.to_sql('cards', conn, if_exists='replace', index=False)
    conn.close()

st.title("Fill card details on the form below:")

# card form
with st.form(key="card_form", clear_on_submit= True) as card_form:
    Issuer_Name = st.selectbox("Select the issuer", options=  ["Discover", "Chase", "Bank of America","Wells Fargo","Citi", "Capital One", "Credit One Bank", "American Express", "VISA", "Mastercard"])
    Name = st.text_area("Enter the card name")
    Category = st.selectbox("Choose the category", options=  ["Travel", "Cash Back", "0% APR","Student","Secured", "Business", "Balance Transfer", "Rewards"])
    Rewards_rate = st.text_area("Enter the rewards rate")
    Welcome_Bonus = st.number_input("Enter the welcome bonus in dollars", min_value= 0) 
    Annual_Fee = st.number_input("Enter the annual fee", min_value= 0)
    Recommended_Credit_Score = st.selectbox("Choose the recommended credit score range", options=["Bad (0-649)", "Fair (650-699)", "Good (700-749) ", "Excellent (750+)"])
    Pros = st.text_area("Enter 3 PROS of the card separated by line breaks")
    Cons =  st.text_area("Enter 3 CONS of the card separated by line breaks")
    Image_URL = st.text_input("Enter the URL of the card image")
    
    if st.form_submit_button("Submit"):
        save_card()
        st.success("Card details saved successfully")

if st.button("Show cards"):
    show_cards()