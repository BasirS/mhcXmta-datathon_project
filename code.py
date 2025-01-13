# -*- coding: utf-8 -*-
"""MHC Datathon Project (Advanced).ipynb

# Import Libraries
import sqlite3
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
from geopy.distance import great_circle
import math
from tabulate import tabulate

# Import the csv files into files -> extract it

# Bus Data
file_path = '/content/MTA_Bus_Hourly_Ridership_Since_April2024.csv'
busdf = pd.read_csv(file_path)

# Preview the data to make sure it's correctly imported
print(busdf.head())
print()
print("Total Rows")
len(busdf)

# Subway Data
file_path = '/content/MTA_Subway_Hourly_Ridership_Since_April2024.csv'
subdf = pd.read_csv(file_path)

# Preview the data to make sure it's correctly imported
print(subdf.head())
print()
print("Total Rows")
len(subdf)

# Queries to extract information
# All the data is already Fair Fares -> filtered before downloaded as a csv file

# Connection
conn = sqlite3.connect(':memory:')

# Load the Subway PD DF to SQLite as a table
subdf.to_sql('subdf', conn, index=False, if_exists='replace')

# Load the Bus PD DF to SQLite as a table
busdf.to_sql('busdf', conn, index=False, if_exists='replace')

# Cursor Object
cursor = conn.cursor()

# Check that Queries Works
query_practice_1 = 'SELECT * FROM busdf LIMIT 10'

cursor.execute(query_practice_1)

result_df = pd.read_sql_query(query_practice_1, conn)
print(result_df)

query_practice_2 = 'SELECT * FROM subdf LIMIT 10'

cursor.execute(query_practice_2)

result_df = pd.read_sql_query(query_practice_2, conn)
print(result_df)

# Question #1: How are Fair Fares Passengers using the transportation system?
# A. Which subway lines are they using?
# B. Which bus routes are they using?

# Check the columns for subway data
column_names = subdf.columns
print(column_names)

# Check the columns for bus data
column_names = busdf.columns
print(column_names)

"""## Question 1: How are Fair Fares Passengers using the transportation system?"""

# Question_1_Query_A
# Problem unresolved: no subways line in the dataset -> Create a map that shows all the subway stations mapped (based on their open data visualization)
# A. Which subway lines are they using? - plotted on Kepler.gl by using the geographic coordinates (lat/lon) from the dataset and color-coded the points to differentiate subway lines or stations by ridership
pic_path = '/content/subway_yearly.png'
img = mpimg.imread(pic_path)
plt.imshow(img)
plt.axis('off')
plt.title('Mapped Subway Ridership (2022 - 2024)', fontsize = 16)
plt.show()

"""Following Maps are from MTA Open Data Built-in Visualization Tools"""

# Question_1_query_B
query = '''SELECT bus_route, COUNT(*) AS count
           FROM busdf
           GROUP BY bus_route
           ORDER BY count DESC
           LIMIT 10'''


cursor.execute(query)

result_df = pd.read_sql_query(query, conn)
print(result_df)
print(tabulate(result_df, headers = 'keys', tablefmt = 'pretty'))

# Question #2: Where are Fair Fares Passengers entering the system?
# A. By Borough?

#Subway
query = '''SELECT borough, COUNT(*) AS count, SUM(ridership) as ridership_sum
           FROM subdf
           GROUP BY borough
           ORDER BY count DESC
           LIMIT 10'''

cursor.execute(query)

result_df = pd.read_sql_query(query, conn)
print(tabulate(result_df, headers = 'keys', tablefmt = 'pretty'))

#Bus
# Problem: Region and Bus #s are together -> Data Manipulation needed

busdf['bus_prefix'] = busdf['bus_route'].str.extract(r'^([A-Z]+)')
busdf['bus_number'] = busdf['bus_route'].str.extract(r'(\d+)$')
busdf.head()

#busdf = busdf.drop('bus_route_letter', axis=1)

# Update sqlite after manipulating pandas df
cursor.execute('ALTER TABLE busdf ADD COLUMN bus_prefix TEXT')
cursor.execute('ALTER TABLE busdf ADD COLUMN bus_number TEXT') #Don't Run again if already added!
busdf.to_sql('busdf', conn, if_exists='replace', index=False)

query = '''SELECT DISTINCT bus_prefix
           FROM busdf'''

cursor.execute(query)

result_df = pd.read_sql_query(query, conn)
print(result_df)

# Query to find
query = '''SELECT bus_prefix, COUNT(*) AS count
           FROM busdf
           GROUP BY bus_prefix
           ORDER BY count DESC
           '''

cursor.execute(query)

result_df = pd.read_sql_query(query, conn)
print(result_df)

#plt.figure(figsize=(10,6))
#sns.lineplot(x='DateTime', y='Ridership', data= busdf)
#plt.title('MTA Bus Ridership Over Time')
#plt.xlabel('Date/Time')
#plt.ylabel('Ridership')
#plt.xticks(rotation=45)
#plt.show()

"""# Question 3:

4-year Colleges: Baruch, Hunter, CSI, Brooklyn, City, Lehman, John Jay, Queens

2-year Colleges: BMCC, QCC, BCC, KCC
"""

baruch_coord = (40.7420, -73.9876)
hunter_coord = (40.7647, -73.9633)
csi_coord = (40.5824, -74.1468)
brooklyn_coord = (40.6629, -73.9640)
city_coord = (40.8211, -73.9496)
lehman_coord = (40.8772, -73.8897)
john_jay_coord = (40.7498, -73.9901)
queens_coord = (40.7420, -73.8170)

bmcc_coord = (40.7174, -74.0123)
qcc_coord = (40.7571, -73.7563)
bcc_coord = (40.8565, -73.9127)
kcc_coord = (40.5785, -73.9356)

colleges = {
    "Baruch College": (40.7404, -73.9832),
    "Hunter College": (40.7678, -73.9645),
    "College of Staten Island (CSI)": (40.6022, -74.1504),
    "Brooklyn College": (40.6309, -73.9515),
    "City College of New York (CCNY)": (40.8200, -73.9493),
    "Lehman College": (40.8729, -73.8945),
    "John Jay College": (40.7707, -73.9892),
    "Queens College": (40.7367, -73.8203),
    "BMCC": (40.7174, -74.0123),
    "QCC": (40.7571, -73.7563),
    "BCC": (40.8565, -73.9127),
    "KCC": (40.5785, -73.9356)
}

subdf.head()

# Logic: extract number of data rows that are a certain distance from the college locations (based on lat and long)

# Haversine Formula: calculate the absolute distance between two locations based on latitude and longitude
def haversine_formula(lat1, lon1, lat2, lon2):
  R = 6371.0 # approximate radius of earth in km

  distance_lat = math.radians(lat2 - lat1)
  distance_lon = math.radians(lon2 - lon1)

  lat1 = math.radians(lat1)
  lat2 = math.radians(lat2)

  a = math.sin(distance_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(distance_lon/2)**2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  d = R * c #Distance in KM

  return d #Conver to Number

threshold_distance = 1

location_counts = {college: 0 for college in colleges}

coordinates = subdf[['latitude', 'longitude']].values.tolist()

for college, coord in colleges.items():
    for lat, lon in coordinates:
        distance = haversine_formula(coord[0], coord[1], lat, lon)
        if distance <= threshold_distance:
            location_counts[college] += 1

for college, count in location_counts.items():
    print(f"{college}: {count} locations")

colleges = list(location_counts.keys())
counts = list(location_counts.values())

# Bar Graph
plt.figure(figsize=(10,6))
plt.bar(colleges, counts, color='skyblue', edgecolor='black')
plt.title("Number of Locations per College", fontsize=16)
plt.xlabel("Colleges", fontsize=12)
plt.ylabel("Number of Locations", fontsize=12)
plt.xticks(rotation=90)
plt.show()

# Visualization
# Create a Base Map based on NYC
m = folium.Map(location=[40.75, -73.90], zoom_start=11)

# Add the Colleges to the Map
for college, coord in location_counts.items():
    folium.Marker(location=coord, popup=college).add_to(m)

# Add the Heatmap based on counts
heat_data = []

for college, count in location_counts.items():
    college_lat, college_lon = colleges[college]
    # If there are locations within the threshold, add them to the heatmap data
    for count in range(count):  # Add the location count times
        heat_data.append([college_lat, college_lon])

HeatMap(heat_data).add_to(m)

# Display the Map
m

# Visualization
# Create a Base Map based on NYC
m = folium.Map(location=[40.75, -73.90], zoom_start=11)

# Add the Colleges to the Map
for college, count in location_counts.items(): # Changed from location_counts.items() to colleges.items() to iterate through the correct dictionary
    folium.Marker(location=colleges[college], popup=college).add_to(m) # Changed coord to colleges[college] to get the coordinates for each college

# Add the Heatmap based on counts
heat_data = []

for college, count in location_counts.items():
    college_lat, college_lon = colleges[college]
    # If there are locations within the threshold, add them to the heatmap data
    for _ in range(count):  # Changed count to _  as the loop variable is not used
        heat_data.append([college_lat, college_lon])

HeatMap(heat_data).add_to(m)

# Display the Map
m

# Question #4: What does subway and bus ridership look like for neighborhoods that would benefit from the increased eligibility criteria for Fair Fares?
# These neighborhoods have been identified as Elmhurst/Jackson Heights,Flushing, Sunset Park, Brownsville, Morrisania and Highbridge.

# Flushing -> Buses: Q12, Q13, Q16, Q17, Q19, Q20, Q25, Q27, Q28, Q34, Q48, Q50, Q58, Q65, Q66
# Subway: 7

#Brownsville -> Buses: B6, B7, B8, B12, B14, B15, B20, B25, B35, B60, B83
# Subway: 3, L, C

#Elmhurst/Jackson Heights -> Q21, Q29, Q32, Q33, Q38, Q47, Q49, Q52SBS, Q53SBS

#Sunset park-> B9, B11, B70, B37, B16, B35, B63

subdf.head()

# Query to find the top subway stations with most Fair Fare Usage
query = '''SELECT station_complex, borough, COUNT(*) AS count, SUM(ridership) AS ridership_sum
           FROM subdf
           GROUP BY station_complex
           ORDER BY ridership_sum DESC
           LIMIT 20
           '''

cursor.execute(query)

result_df = pd.read_sql_query(query, conn)
print(result_df)

#Elmhurst/Jackson Heights, Flushing, Sunset Park, Brownsville, Morrisania and Highbridge
# 74-Broadway (7)/Jackson Hts-Roosevelt = Jackson Heights
# 161 St-Yankee Stadium = right between Morrisania and Highbridge
# Crowns Hts-Utica Av = Brownsville
# Flushing-Main St = Flushing
# Broadway Junction = near Brownsville
# 125 St = Leads to Bronx

query = '''SELECT station_complex, borough, COUNT(*) AS count, SUM(ridership) AS ridership_sum, SUM(ridership) / COUNT(*) AS avg_ridership
           FROM subdf
           WHERE NOT borough = 'Manhattan'
           GROUP BY station_complex
           ORDER BY ridership_sum DESC
           LIMIT 20
           '''

cursor.execute(query)

result_df = pd.read_sql_query(query, conn)
print(result_df)

print(tabulate(result_df, headers = 'keys', tablefmt = 'pretty'))

#Elmhurst/Jackson Heights, Flushing, Sunset Park, Brownsville, Morrisania and Highbridge
# 74-Broadway (7)/Jackson Hts-Roosevelt = Jackson Heights
# 161 St-Yankee Stadium = right between Morrisania and Highbridge
# 3 Av - 149 St = near Morrisania
# 125 St = Leads to Bronx

# Crowns Hts-Utica Av = Brownsville
# Broadway Junction = near Brownsville
# 8 Av = Sunset Park
# 36 St = Sunset Park

# Flushing-Main St = Flushing
# Forest Hills & Kew Gardens & Junction Blvd = lead to Elmhurst

busdf.head()

query = '''SELECT bus_route, COUNT(*) AS count, round(SUM(ridership),0) AS ridership_sum
           FROM busdf
           GROUP BY bus_route
           ORDER BY ridership_sum DESC
           LIMIT 20
           '''

cursor.execute(query)

result_df = pd.read_sql_query(query, conn)
print(result_df)

#Q25, Q27, Q44, Q58, Q65: Flushing
#B6, B8, B35: Brownsville & Sunset Park
#BX9, BX12, BX19: passes the two Bronx neighborhoods

subdf.head()
