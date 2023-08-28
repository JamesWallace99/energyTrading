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
    
    def generate_generator(self, name: str, init_power: float):
        self.generator_assets.append(Solar(name = name, power = init_power))
        return(self.generator_assets)
    
    def initiate_grid(self, mode: str, asset_csv_pathname):
        
        df = pd.read_csv(asset_csv_pathname) # csv containing asset details
        
        
        asset_types = ['generator', 'load', "storage"]
        
        for i in range(len(asset_types)):
            temp_df = df[df["type"] == asset_types[i]]
            
            for index, row in temp_df.iterrows():
                print('initiating {} {}'.format(row['num_assets'], asset_types[i]))
                
                for j in range(row["num_assets"]):
                    
                    if asset_types[i] == "generator":
                        if mode == 'random':
                            if type(row['name']) == str: # np.isnan(row['name']) is False
                                temp_name = row['name'] + "_" + str(j)
                            else:
                                temp_name = "generator_" + str(j)
            
                            temp_params = {"power": round(random.uniform(row["power_range_lower"], row["power_range_upper"]), 2)}
                        
                        self.generate_generator(name = temp_name, init_power = temp_params['power'])
                        
                        
                        if mode == 'defined':
                            pass
                            
                    if asset_types[i] == "load":
                        pass
                    
                    if asset_types[i] == "storage":
                        pass
            
            
            
            pass # call the initate asset function
                    
                    
        
        # write this next, should account for mode and include/generate random params in random mode
        # should create all the assets
        pass 
    
    def run_grid():
        # auto balance between all available assets
        pass
    
    
