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
    
    def generate_storage(self, name: str, output: float, max_capacity: float, current_capacity: float):
        self.storage_assets.append(energyStorage(name = name, maxOutput=output, state = 'static', maxCapacity= max_capacity, currentCapacity= current_capacity))
        return()
    
    def generate_load(self, name: str, max_load: float, load_time_limit: float):
        self.load_assets.append(energyLoad(name = name, maxLoad=max_load, loadTimeLimit= load_time_limit))
        return()
    
    def generate_generator(self, name: str, init_power: float):
        self.generator_assets.append(Solar(name = name, power = init_power))
        return()
    
    def initiate_grid(self, mode: str, asset_csv_pathname):
        
        df = pd.read_csv(asset_csv_pathname) # csv containing asset details
        
        
        asset_types = ['generator', 'load', "storage"]
        
        for i in range(len(asset_types)):
            temp_df = df[df["type"] == asset_types[i]]
            
            for index, row in temp_df.iterrows():
                print('initiating {} {}'.format(row['num_assets'], asset_types[i]))
                
                for j in range(row["num_assets"]):
                    
                    if mode == 'random':
                        if type(row['name']) == str:
                            temp_name = row['name'] + "_" + str(j)
                        else:
                            temp_name = asset_types[i] + "_" + str(j)
                    
                        if asset_types[i] == "generator":
                            temp_params = {"power": round(random.uniform(row["power_range_lower"], row["power_range_upper"]), 2)}
                            self.generate_generator(name = temp_name, init_power = temp_params['power'])
                            
                        if asset_types[i] == "load":
                            temp_params = {"max_load": round(random.uniform(row["max_load_range_lower"], row["max_load_range_upper"]), 2), "load_time_limit": round(random.uniform(row["load_time_limit_range_lower"], row["load_time_limit_range_upper"]), 2)}
                            self.generate_load(name = temp_name, max_load= temp_params['max_load'], load_time_limit= temp_params['load_time_limit'])
                        
                        if asset_types[i] == "storage":
                            temp_params = {"max_output": round(random.uniform(row['output_range_lower'], row['output_range_upper']), 2), "max_capacity": round(random.uniform(row['max_capacity_range_lower'], row['max_capacity_range_upper']),2 ), "current_capacity": round(random.uniform(row['current_range_lower'], row['current_range_upper']), 2)}
                            self.generate_storage(name = temp_name, output=temp_params["max_output"], max_capacity=temp_params["max_capacity"], current_capacity=temp_params["current_capacity"])
                    
                    if mode == 'defined':
                        pass
                
        pass 
    
    def run_grid():
        # auto balance between all available assets
        pass
    
    
