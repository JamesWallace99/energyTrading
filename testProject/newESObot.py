from config import energyStorage, energyLoad, Solar
import random
import pandas as pd


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
    
    