from new_config import energyStorage, energyLoad, energyGenerator
import random
import pandas as pd


class esoBot():
    
    def __init__(self):
        self.storage_assets = []
        self.load_assets = []
        self.generator_assets = []
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
        for index, row in gen_df.iterrows():
                self.generator_assets.append(self.generate_generator(name = row["name"], power = row["gen_power_lim"]))
        
        # get load assets
        mask = df["type"] == "load"
        load_df = df[mask]
        for index, row in load_df.iterrows():
                self.load_assets.append(self.generate_load(name = row["name"], max_load = row["load_power_lim"]))
        
        # get storage assets
        mask = df["type"] == "storage"
        stor_df = df[mask]
        for index, row in stor_df.iterrows():
                self.storage_assets.append(self.generate_storage(name = row["name"], output = row["storage_power_lim"], max_capacity= row["storage_max_cap"], current_capacity= row["storage_current_cap"]))
        
        return(print("Assets initialised succesfully"))
    
                
    
    # generators generate a random generation profile over set time period with a given time interval
    # load assets generate a random load profile over a set time period with a given time interval
    # storage assets have two methods - check capabiltiy and execute trade. These give asset capability and help balance grid
    # eso bot needs to calculate net imbalance in the system and then efficiently deploy storage assets to reduce imbalance
    
    # in future, storage assets will bid in with a price
    # in future, need to add generation flexibility, generators bid in with a price given ability to curtail
    
    