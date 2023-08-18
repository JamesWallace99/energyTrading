from config import energyStorage, energyLoad, Solar
import random

# randomly generates assets given parameter range

class esoBot():
    
    def __init__(self, sim_runs: int, mode: str):
        self.sim_runs = sim_runs
        self.mode = mode
        if self.mode == "random":
            self.storage_assets = []
            self.load_assets = []
            self.generator_assets = []
        # if mode isn't random need to allow users to pass a custom list of generator, load and storage assets
    
    def generate_storage_random(self, num_storage_assets: int, output_range: list, max_capacity_range:list, current_range: list):
        for i in range(num_storage_assets):
            self.storage_assets.append(energyStorage(name = "storage" + str(i), maxOutput=random.randint(output_range[0], output_range[1]), state = 'static', maxCapacity=random.randint(max_capacity_range[0], max_capacity_range[1]), MaxCRate=1, currentCapacity=random.randint(current_range[0], current_range[1])))
            
        return(self.storage_assets)
    
    def generate_load_random(self, num_load_assets: int, max_load_range: list, load_time_limit_range: list):
        for i in range(num_load_assets):
            self.load_assets.append(energyLoad(name = "load" + str(i), maxLoad=random.randint(max_load_range[0], max_load_range[1]), loadTimeLimit=random.uniform(load_time_limit_range[0], load_time_limit_range[1])))
    
    def generate_generators_random(self, num_generator_assets: int, power_range: list):
        for i in range(num_generator_assets):
            self.generator_assets.append(Solar(name = "generator" + str(i), power = random.randint(power_range[0], power_range[1])))
        return(self.generator_assets)
    
    def initiate_grid():
        # write this next, should account for mode and include/generate random params in random mode
        # should create all the assets
        pass 
    
    def run_grid():
        # auto balance between all available assets
        pass
    
    
