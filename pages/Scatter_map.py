
"""
Created on Tue Feb 14 12:21:58 2023

@author: kavya
"""


import os.path as path
import streamlit as st

from os import listdir
from statistics import mean
import pydeck as pdk

import pandas as pd
import numpy as np

#from urllib.error import URLError

st.set_page_config(page_title="Maps", page_icon="🌍")

st.markdown("# Mapping")
st.sidebar.header("Mapping according to region")



#@st.cache_data
def from_data_file(filename):
    url = (r"C:\Users\kavya\OneDrive\Desktop\ADES\data\farmer_data.xlsx" )
    return pd.read_excel(url)


try:
    ALL_LAYERS = {
        "Product Name": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("Product Name"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Region": pdk.Layer(
            "ScatterplotLayer",
            data=from_data_file("Region.json"),
            get_position=["lon", "lat"],
            get_color=[200, 30, 0, 160],
            get_radius="[exits]",
            radius_scale=0.05,
        ),
        "County/Division": pdk.Layer(
            "TextLayer",
            data=from_data_file("County/Division.json"),
            get_position=["lon", "lat"],
            get_text="name",
            get_color=[0, 0, 0, 200],
            get_size=15,
            get_alignment_baseline="'bottom'",
        ),
        "Outbound Flow": pdk.Layer(
            "ArcLayer",
            data=from_data_file("bart_path_stats.json"),
            get_source_position=["lon", "lat"],
            get_target_position=["lon2", "lat2"],
            get_source_color=[200, 30, 0, 160],
            get_target_color=[200, 30, 0, 160],
            auto_highlight=True,
            width_scale=0.0001,
            get_width="outbound",
            width_min_pixels=3,
            width_max_pixels=30,
        ),
    }
    st.sidebar.markdown("### Map Layers")
    selected_layers = [
        layer
        for layer_name, layer in ALL_LAYERS.items()
        if st.sidebar.checkbox(layer_name, True)
    ]
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state={
                    "latitude": 37.76,
                    "longitude": -122.4,
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=selected_layers,
            )
        )
    else:st.error("Please choose at least one layer above.")
    

except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )'''
