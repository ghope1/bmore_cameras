# authored by gavin h. on july 24th, 2022
# generates an *aesthetic* map of speed and red light cameras in baltimore
# data labeled 'bmore' obtained from data.baltimorecity.gov
# data labeled 'md' obtained from data.imap.maryland.gov
# takes my personal machine about a 45s to run to completion

import time
import matplotlib.pyplot as mpl
import geopandas as gpd

# projection centered around MD
ESPG = 'EPSG:6487'

# filepath for data files
FILEPATH_START = '../data/'

# loads speedcam data then converts to proper projection
startTime = time.time()
speedcams_df = gpd.read_file(FILEPATH_START+'bmore_speedcams.geojson')
speedcams_df = speedcams_df.to_crs(ESPG)
print("Took ", time.time() - startTime, "seconds to load speedcam data.")

# loads building data then converts to proper projection
startTime = time.time()
buildings_df = gpd.read_file(FILEPATH_START+'bmore_buildings.geojson')
buildings_df = buildings_df.to_crs(ESPG)
print("Took ", time.time() - startTime, "seconds to load building data.")

# loads red light camera data then converts to proper projection
startTime = time.time()
redlightcams_df = gpd.read_file(FILEPATH_START+'bmore_redlightcams.geojson')
redlightcams_df = redlightcams_df.to_crs(ESPG)
print("Took ", time.time() - startTime, "seconds to load red light data.")

# not sure if i want to do anything with the water data yet
# startTime = time.time()
# water_df = gpd.read_file(FILEPATH_START+'bmore_water.geojson')
# water_df = water_df.to_crs(ESPG)
# print("Took ", time.time() - startTime, "seconds to load water data.")

# loads county outline data then converts to proper projection
startTime = time.time()
counties_df = gpd.read_file(FILEPATH_START+'md_counties.geojson')
counties_df = counties_df.to_crs(ESPG)
print("Took ", time.time() - startTime, "seconds to load county data.")


# sets map size and resolution
fig, ax = mpl.subplots(figsize=(8, 8), dpi=400)

startTime = time.time()

# restricts axes limits to just baltimore
mpl.xlim(424500, 441000)
mpl.ylim(169500, 190000)
ax.set_facecolor('black')


# plots the data
counties_df.plot(color='darkgrey', edgecolor='black', linewidth=.2, ax=ax)
# water_df.plot(color="blue", ax=ax)
speedcams_df.plot(color='blue', markersize=2, alpha=0.9, ax=ax)
redlightcams_df.plot(color='red', markersize=2, alpha=0.9, ax=ax)
buildings_df.plot(color="black", ax=ax)

# remove axes ticks
ax.set_yticklabels([])
ax.set_xticklabels([])

print("Took ", time.time() - startTime, "seconds to generate map.")

mpl.savefig('bmore_cams.png', bbox_inches='tight')