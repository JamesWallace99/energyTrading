from config import energyStorage, energyLoad, energyGenerator
import random

# randomly generates assets given parameter range

class esoBot():
    
    def __init__(self, sim_runs: int, mode: str):
        self.sim_runs = sim_runs
        self.mode = mode
    
    def generate_storage_random(self, num_assets: int, output_range: list, max_capacity_range:list, current_range: list):
        # generate the storage on the grid
        
        test = energyStorage(name = 'test', maxOutput=50, state = 'static', maxCapacity=100, MaxCRate=2, currentCapacity=0)
        
        storage_assets = []
        
        for i in range(num_assets):
            storage_assets.append(energyStorage(name = "storage" + str(i), maxOutput=random.randint(output_range[0], output_range[1]), state = 'static', maxCapacity=random.randint(max_capacity_range[0], max_capacity_range[1]), MaxCRate=1, currentCapacity=random.randint(current_range[0], current_range[1])))
            
        return(storage_assets)
        
    
    def generate_load_random():
        # start the load on the grid
        pass
    
    def generate_generators_random():
        # start the generators on the grid
        pass 
    
    def initiate_grid():
        pass 
    
    def run_grid():
        pass
    
    
