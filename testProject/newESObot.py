from new_config import energyStorage, energyLoad, energyGenerator
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class esoBot():
    
    def __init__(self):
        self.storage_assets = []
        self.load_assets = []
        self.generator_assets = []
        self.imbalance_profile = []
        # if mode isn't random need to allow users to pass a custom list of generator, load and storage assets
    
    # these methods add the generation, load and storage assets into the bot instance
    def generate_storage(self, name: str, output: float, max_capacity: float, current_capacity: float):
        self.storage_assets.append(energyStorage(name = name, maxOutput=output, maxCapacity= max_capacity, currentCapacity= current_capacity))
        return()
    
    def generate_load(self, name: str, max_load: float):
        self.load_assets.append(energyLoad(name = name, maxLoad=max_load))
        return()
    
    def generate_generator(self, name: str, power: float):
        self.generator_assets.append(energyGenerator(name = name, max_power=power))
        return()
    
    def initiate_grid_csv(self, asset_csv_pathname):
        
        df = pd.read_csv(asset_csv_pathname)
        
        # get generator assets
        mask = df["type"] == "generator"
        gen_df = df[mask]
        y = 0
        for index, row in gen_df.iterrows():
            self.generate_generator(name = row["name"], power = row["gen_power_lim"])
        
        # get load assets
        mask = df["type"] == "load"
        load_df = df[mask]
        for index, row in load_df.iterrows():
            self.generate_load(name = row["name"], max_load = row["load_power_lim"])
        
        # get storage assets
        mask = df["type"] == "storage"
        stor_df = df[mask]
        for index, row in stor_df.iterrows():
            self.generate_storage(name = row["name"], output = row["storage_power_lim"], max_capacity= row["storage_max_cap"], current_capacity= row["storage_current_cap"])
        
        return(print("Assets initialised succesfully"))
    
    def get_imbalance_forecast(self, sim_length, time_step):
        
        net_gen = np.zeros(int(np.ceil((sim_length / time_step)))) # stores gen profile over time period
        net_load = np.zeros(int(np.ceil((sim_length / time_step)))) # stores demand profile over time period
        
        # iterate over gen and get profile
        
        for i in range(len(self.generator_assets)):
            net_gen += self.generator_assets[i].calculate_generation(sim_length, time_step)
            
        for i in range(len(self.load_assets)):
            net_load += self.load_assets[i].calculate_load(sim_length, time_step)
        
        net_imbalance = net_gen - net_load
        
        self.imbalance_profile = net_imbalance
            
        return(net_imbalance)
    
    def plot_imbalance(self, sim_length, time_step):
        
        times = np.linspace(0, sim_length, num = int(np.ceil((sim_length / time_step))))
        
        if len(self.imbalance_profile) > 0:
            plt.bar(times, self.imbalance_profile)
            plt.xlabel("Time Step (Hrs)")
            plt.ylabel("Net Imbalance (MW)")
            plt.show()
            return()
        
        else:
            imbalance = self.get_imbalance_forecast(sim_length, time_step)
            plt.bar(times, imbalance)
            plt.xlabel("Time Step (Hrs)")
            plt.ylabel("Net Imbalance (MW)")
            plt.show()
            return()
        
        
        
        
        # net_imbalance = net_gen - net_load
    
                
    
    # generators generate a random generation profile over set time period with a given time interval
    # load assets generate a random load profile over a set time period with a given time interval
    # storage assets have two methods - check capabiltiy and execute trade. These give asset capability and help balance grid
    # eso bot needs to calculate net imbalance in the system and then efficiently deploy storage assets to reduce imbalance
    
    # in future, storage assets will bid in with a price
    # in future, need to add generation flexibility, generators bid in with a price given ability to curtail
    
    