import pandas as pd
import numpy as np
import datetime
from solarpy import solar_panel
from solarpy import irradiance_on_plane
from opencage.geocoder import OpenCageGeocode
import matplotlib.pyplot as plt

# this file reads in the solar voltaics reporting spreadsheets from the national deartment of stats
# these locations are converted into lat and long
# it also approximates the equivalent size of the solar panels by comparing their rated power output and calculated max irradiance values
# it saves to a new csv with country,constituency,installed_cap_mwh,eqv_panel_area_m2,lat,long

filepath = "/Users/jameswallace/Documents/energyTrading/testProject/Table_3_Feb_24-Table 1.csv"

test_df = pd.read_csv(filepath, skiprows=4).iloc[:,:3] # import solar installations in the UK and format
test_df.columns = ["country", "constituency","installed_cap_mwh"] # format column names
test_df["eqv_panel_area_m2"] = np.nan
test_df['lat'] = np.nan
test_df['long'] = np.nan

print(test_df.head())

# now we need to estimate the size of the solar installations so that we can estimate their output at different times of the day
# assume that installed capacity is max output
# find max irradiance at anytime of the day and then use this to calculate panel size
# need to find max irradiance by sweeping through time values
# will also need to do a calendar sweep

# initialise values
key = '87ada2f6b3d645458229d8fae2c45aa8'
geocoder = OpenCageGeocode(key)

months_days = {4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30}
times = [x for x in range(10, 14)]

vnorm = np.array([0, 0, -1])  # plane pointing zenith
h = 0  # sea-level
year = 2023



for index, row in test_df.iterrows():
    row_test = row

    query = str(row_test["constituency"] + " " + row_test["country"] + " " + "UK")

    results = geocoder.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    
    test_df.at[index, "lat"] = lat
    test_df.at[index, "long"] = lng


    # now find max modelled irradiance through a sweep of the year and times
    irradiance_vals = []
    dates = []

    for i in months_days:
        for j in range(1, months_days[i] + 1):
            for k in times:
                date = datetime.datetime(year, i, j, k)
                # print("solarpy irradiance estimate (W / m^2): ", irradiance_on_plane(vnorm, h, date, lat))
                irradiance_vals.append(irradiance_on_plane(vnorm, h, date, lat))
                dates.append(date)
                
    max_val = np.max(irradiance_vals)
    panel_area = row_test["installed_cap_mwh"]*10e6 / max_val / 0.2 # calculate panel area in m^2
    
    test_df.at[index, "eqv_panel_area_m2"] = panel_area
    

print(test_df.head())

test_df.to_csv('out.csv', index=False) 