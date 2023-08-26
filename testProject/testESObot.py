from config import energyStorage, energyLoad, Solar
import random
import pandas as pd

# randomly generates assets given parameter range

class esoBot():
    
    def __init__(self):
        self.storage_assets = []
        self.load_assets = []
        self.generator_assets = []
        # if mode isn't random need to allow users to pass a custom list of generator, load and storage assets
    
    def generate_storage_random(self, num_assets: int, output_range: list, max_capacity_range:list, current_range: list):
        for i in range(num_assets):
            self.storage_assets.append(energyStorage(name = "storage" + str(i), maxOutput=random.randint(output_range[0], output_range[1]), state = 'static', maxCapacity=random.randint(max_capacity_range[0], max_capacity_range[1]), MaxCRate=1, currentCapacity=random.randint(current_range[0], current_range[1])))
            
        return(self.storage_assets)
    
    def generate_load_random(self, num_assets: int, max_load_range: list, load_time_limit_range: list):
        for i in range(num_assets):
            self.load_assets.append(energyLoad(name = "load" + str(i), maxLoad=random.randint(max_load_range[0], max_load_range[1]), loadTimeLimit=random.uniform(load_time_limit_range[0], load_time_limit_range[1])))
    
    def generate_generators_random(self, num_assets: int, power_range: list):
        for i in range(num_assets):
            self.generator_assets.append(Solar(name = "generator" + str(i), power = random.randint(power_range[0], power_range[1])))
        return(self.generator_assets)
    
    def initiate_grid(self, mode: str, asset_csv_pathname):
        
        input_df = pd.read(asset_csv_pathname)
        
        if mode == "random":
            print("initialising random assets")
            # should only be one of each row - check if # of columns exceeds 3 then check for uniqueness on typing
            # move randomisation here and then generalise the generate_asset methods
            
            self.generate_storage_random()
            
        
        if mode == "defined":
            print("Initialsing assets")
        
        # write this next, should account for mode and include/generate random params in random mode
        # should create all the assets
        pass 
    
    def run_grid():
        # auto balance between all available assets
        pass
    
    
