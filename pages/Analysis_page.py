# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:21:54 2023

@author: kavya
"""

import os.path as path
import streamlit as st

from os import listdir
from statistics import mean
import pydeck as pdk

import pandas as pd
import numpy as np


st.set_page_config(page_title="Analysis", 
                   page_icon = "bar_chart")

df = pd.read_excel(r"C:\Users\kavya\OneDrive\Desktop\ADES\data\farmer_data")



chart_name = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['b', 'g', 'h'])

st.line_chart()
