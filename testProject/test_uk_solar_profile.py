import numpy as np
import pandas as pd
from solarpy import solar_panel
from solarpy import irradiance_on_plane
import datetime
import matplotlib.pyplot as plt
import random

test_df = pd.read_csv("out.csv")

print(test_df.head())

# now need to simualate solar profile over a certain time period with set granularity
# use 24 hr(s) with 0.5 hr settlement periods

test_time_step = 0.5 # set the time step to generate the solar profiles (in hours)
test_sim_length = 240 # set length of sim in hours
solar_gen_profile = np.empty([int(np.ceil(test_sim_length / test_time_step)) + 1]) # in MW # generate an empty array to store the generation profile

def return_times(start,end, delta):
    """Generates an array of timesteps

    Parameters
    ----------
    start : dateime
        start time for the sim
    end : _datetime
        end time for the sim
    delta : float
        timestep (hrs)
    """
    times = [start]
    
    while start < end:
        start += datetime.timedelta(hours = delta)
        times.append(start)
    return(times)

start_date_time = datetime.datetime(2024, 2, 19, 12)
end_date_time = start_date_time + datetime.timedelta(hours = test_sim_length)

times = return_times(start_date_time, end_date_time, test_time_step)

for index,row in test_df.iterrows(): # iterate over solar assets
    for i in range(len(times)): # iterate over each timestep in simulation
        panel = solar_panel(row['eqv_panel_area_m2'], 0.2, id_name='temp')
        panel.set_orientation(np.array([0, 0, -1]))
        panel.set_position(row['lat'], row['long'], 0)
        panel.set_datetime(times[i])
        
        solar_gen_profile[i] += panel.power() * 10e-6 * random.uniform(0, 1) # add to overall generation profile and reduce to MWh


    
plt.plot(times, solar_gen_profile)
plt.xlabel("Time")
plt.ylabel("Solar Power Output MW")


plt.show()
