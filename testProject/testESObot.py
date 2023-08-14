from config import energyStorage, energyLoad, Solar
import random

# randomly generates assets given parameter range

class esoBot():
    
    def __init__(self, sim_runs: int, mode: str):
        self.sim_runs = sim_runs
        self.mode = mode
    
    def generate_storage_random(self, num_storage_assets: int, output_range: list, max_capacity_range:list, current_range: list):
        storage_assets = []
        for i in range(num_storage_assets):
            storage_assets.append(energyStorage(name = "storage" + str(i), maxOutput=random.randint(output_range[0], output_range[1]), state = 'static', maxCapacity=random.randint(max_capacity_range[0], max_capacity_range[1]), MaxCRate=1, currentCapacity=random.randint(current_range[0], current_range[1])))
            
        return(storage_assets)
    
    def generate_load_random(self, num_load_assets: int, max_load_range: list, load_time_limit_range: list):
        load_assets = []
        for i in range(num_load_assets):
            load_assets.append(energyLoad(name = "load" + str(i), maxLoad=random.randint(max_load_range[0], max_load_range[1]), loadTimeLimit=random.randint(load_time_limit_range[0], load_time_limit_range[1])))
    
    def generate_generators_random(self, num_generator_assets: int, power_range: list):
        generator_assets = []
        for i in range(num_generator_assets):
            generator_assets.append(Solar(name = "generator" + str(i), power = random.randint(power_range[0], power_range[-1])))
        pass 
    
    def initiate_grid():
        pass 
    
    def run_grid():
        pass
    
    
