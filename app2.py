# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:00:30 2023

@author: kavya
"""
from pathlib import Path
import streamlit as st
import pandas as pd
import openpyxl as oxl
from PIL import Image
import numpy as np
import plotly.express as px
import io



#@st.cache_data#(allow_output_mutation=True)
def get_data_from_excel():
    data = pd.read_excel(
        r"C:\Users\46058007\OneDrive - MMU\Attachments\ADES\ADES\famers_data1.xlsx",
        sheet_name="Farmer's Data",
        encoding= 'ISO-8859-1',
        usecols="A:P",
        #encoding='uf08'
        #converters={'Contact Number':int}
    )
    return data
df = get_data_from_excel() 
#df= df.withColumn("x_dbl", df["x"].cast(DoubleType()))

print(df)

st.write(df)

# --------SIDERBAR-----------
st.sidebar.header("Farmer-Info")

names = st.sidebar.selectbox('name:', options=df["Farmer's Name"].unique())
products = st.sidebar.selectbox('crop name:', options=df["Product Name"].unique())
quantity = st.sidebar.selectbox('Product quantity:', options=df["Product QTY"].unique())
farm_size = st.sidebar.selectbox('farm size of each farmer:', options=df["Farm Size"].unique())
#country = st.sidebar.multiselect('countr belong to:', options=df["Country"].unique())
#city = st.sidebar.selectbox('cities:', options=df["Town/City"].unique())
#contact = st.sidebar.selectbox('contact directly:', options=df["Contact Number"].unique())




#def local_css(file_name):
#    with open(r"C:\Users\kavya\kavya\kavya work\ADES\famers_data1.xlsx") as f:
#        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#def remote_css(url):
#    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

#def icon(icon_name):
#    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


#local_css("style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

#icon("search")
#selected = st.text_input("", "Search...")
#button_clicked = st.button("OK")

#st.write('you selected', names, products, quantity, farm_size)

st.markdown("""---""")
st.dataframe(df)

st.button("Rerun")#otal_order = len(df)




