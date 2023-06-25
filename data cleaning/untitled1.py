

import geopandas as gpd
import pandas as pd

from geopy.geocoders import GoogleV3
import googlemaps
# Set up the OpenCage geocoder
geocoder = GoogleV3('AIzaSyAFGzeoMP9hk1FgPrVqCmiTmxPsxNO0X54')

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel(r"C:\Users\kavya\kavya\kavya work\ADES\data cleaning\cleaned_data.xlsx")

# Geocode the location data to obtain latitude and longitude coordinates
locations = df['Region'] + ', ' + df['County/Division'] + ', ' + df['Town/City'] + ', ' + df['Neighbourhood/Street']
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
gdf.to_file('filename.shp', driver='ESRI Shapefile')


