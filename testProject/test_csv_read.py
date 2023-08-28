import pandas as pd
import random
import numpy as np


from testESObot import esoBot
from config import energyLoad, energyGenerator, energyStorage

test_bot = esoBot()


test_bot.initiate_grid(mode='random', asset_csv_pathname= "test_random_input.csv")

for i in range(len(test_bot.generator_assets)):
    print(test_bot.generator_assets[i])



'''
df = pd.read_csv("test_random_input.csv")

# print(df.columns)


# get all the entries for a certain type of asset
#print(df[df["type"] == "generator"]["power_range_lower"])

mode = 'random'
asset_types = ['generator', 'load', "storage"]

for i in range(len(asset_types)):
    temp_df = df[df["type"] == asset_types[i]]
    
    for index, row in temp_df.iterrows():
        print('initiating {} {}'.format(row['num_assets'], asset_types[i]))
        
        for j in range(row["num_assets"]):
            
            if asset_types[i] == "generator":
                if mode == 'random':
                    if type(row['name']) == str: # np.isnan(row['name']) is False
                        temp_name = row['name']
                    else:
                        temp_name = "generator_" + str(j)
    
                    temp_params = {"power": round(random.uniform(row["power_range_lower"], row["power_range_upper"]), 2)}
                
                print(temp_name, temp_params)
                
                if mode == 'defined':
                    pass
                    
            if asset_types[i] == "load":
                pass
            
            if asset_types[i] == "storage":
                pass
            
            
            
            pass # call the initate asset function

# for all the asset types we do need to check if the required information exists within the columns
# also need to check that those columns are not nonscence i.e. negative values


'''