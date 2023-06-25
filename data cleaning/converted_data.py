
import streamlit as st
import geopandas as gpd
import pandas as pd

from geopy.geocoders import GoogleV3
import googlemaps

import folium

# Set up the OpenCage geocoder
geocoder = GoogleV3('AIzaSyAFGzeoMP9hk1FgPrVqCmiTmxPsxNO0X54')

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel(r"C:\Users\kavya\kavya\kavya work\ADES\data cleaning\cleaned.xlsx")

# Geocode the location data to obtain latitude and longitude coordinates
locations = df['Region'] + ', ' + df['Country'] + ', ' + df['Town'] + ', ' + df['Neighbourhood Street']
geocodes = locations.apply(geocoder.geocode)

# Extract the latitude and longitude coordinates from the geocoded data
lats = geocodes.apply(lambda x: x.latitude if x else None)
longs = geocodes.apply(lambda x: x.longitude if x else None)

# Create a new DataFrame with the geocoded data
geocoded_df = pd.concat([df, lats, longs], axis=1)
geocoded_df.columns = list(df.columns) + ['Latitude', 'Longitude']

# Convert the DataFrame to a GeoDataFrame
gdf = gpd.GeoDataFrame(geocoded_df, geometry=gpd.points_from_xy(geocoded_df['Longitude'], geocoded_df['Latitude']))

# Save the GeoDataFrame to a shapefile or GeoJSON file
gdf.to_file('filename.geojson', driver='GeoJSON')

# Save the GeoDataFrame to Shapefile format
gdf.to_file('filename.shp', driver='ESRI Shapefile')



# Save the GeoDataFrame to XML format
gdf.to_file('filename.xml', driver='GML')


#st.write(gdf)



#mapping on streamlit

# Create a map centered at the mean latitude and longitude
center_lat, center_long = gdf['Latitude'].mean(), gdf['Longitude'].mean()
m = folium.Map(location=[center_lat, center_long], zoom_start=10)

# Add the GeoDataFrame to the map as markers
for _, row in gdf.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['geometry']).add_to(m)




# Convert the Folium map to HTML
folium_map = folium.Map(location=[center_lat, center_long], zoom_start=10)
for _, row in gdf.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['geometry']).add_to(folium_map)
folium_map_html = folium_map._repr_html_()













