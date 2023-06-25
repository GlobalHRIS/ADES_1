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
#from pages import 
from pandas.api.types import infer_dtype

@st.cache_data
def get_data_from_excel():
    data = pd.read_excel("farmers_data.xlsx",sheet_name="Farmer-Data",usecols="A:K", header=0)
    return data
    
df = get_data_from_excel() 
print(df)

st.write(df)

# --------SIDERBAR-----------
st.sidebar.header("Farmer-Info")

#names = st.sidebar.selectbox('name:', options=df["Farmers Name"].unique())
products = st.sidebar.selectbox('crop name:', options=df["Product Name"].unique())
quantity = st.sidebar.selectbox('Product quantity:', options=df["Product QTY"].unique())
farm_size = st.sidebar.multiselect('farm size of each farmer:', options=df["Farm Size"].unique())
#country = st.sidebar.multiselect('countr belong to:', options=df["Country"].unique())
city = st.sidebar.selectbox('cities:', options=df["Town/City"].unique())
contact = st.sidebar.selectbox('contact directly:', options=df["Contact Number"].unique())




st.write('you selected', products, quantity, farm_size, city, contact)

st.markdown("""---""")
st.dataframe(df)

st.button("Rerun")#otal_order = len(df)





