import random
import numpy as np

class energyGenerator():
    """
    A class to represent a generator asset on the grid.
    
    ...
    
    Attributes
    ----------
    name : str
        Name of the generator asset
    max_power : float
        Max power output of the generator asset (MW)
    location : List[float]
        List containing lat and long of generator asset
    time_step: int
        Time inteveral for simulating generation profile
    gen_forecast: List[float]
        List containing generation forecast for asset
    sim_length: int
        Total length of sim
        
    Methods
    -------
    calculate_generation()
    Calculates a random generation profile in MW for the generation asset based on the sim time step and sim length
    Assume that value is average power gen in MW within interval

    """
    def __init__(self, name, max_power, time_step, sim_length, location= None, gen_forecast = None):
        self.name : str = name
        self.max_power : float = max_power
        self.location : list[float] = location # list of long-lat need to define data format
        self.time_step: float = time_step # time step for the simualtion in hrs
        self.sim_length: float = sim_length # total length of sim in hrs
        self.gen_forecast: list[float] = gen_forecast
        
        
    def __str__(self):
        return f"Site Name: {self.name}, Power Output: {self.max_power}"
    
    def calculate_generation(self):
        """
        Calculates a random generation profile for the generation asset based on the sim time step
        """
        test = np.empty([int(np.ceil(self.sim_length / self.time_step))]) # initiate empty array
        for i in range(len(test)):
            test[i] = round(random.uniform(0, self.max_power), 2)
        
        return(test)

    
class energyLoad():
    """
    A class to represent a load asset on the grid.
    
    ...
    
    Attributes
    ----------
    name : str
        Name of the load asset
    max_load : float
        Max power demanded by the load asset (MW)
    location : List[float]
        List containing lat and long of load asset
    time_step: int
        Time inteveral for simulating generation profile
    load_forecast: List[float]
        List containing generation forecast for asset
    sim_length: int
        Total length of sim
        
    Methods
    -------
    calculate_demand()
    Calculates a random demand profile in MW for the deamnd asset based on the sim time step and sim length
    Assume that value is average demand gen in MW within interval

    """
    def __init__(self, name, maxLoad, time_step, sim_length, load_forecast = None, location = None):
        self.name : str = name # name of load asset
        self.maxLoad : float = maxLoad # max load in MW
        self.location : list[float] = location # list of long-lat need to define data format
        self.time_step : float = time_step # sim time step in hrs
        self.sim_length : float = sim_length # total length of sim in hrs
        self.load_forecast : list[float] = load_forecast # array containing load forecast for asset in MW
        
    def __str__(self):
        return f"Name: {self.name}, Max Load: {self.maxLoad} MW, Load Time Limit: {self.loadTimeLimit} hrs, Current Load: {self.current_load()} MW, Current Load Time: {self.current_load_time()} hrs"
    
    
    def calculate_load(self):
        """
        Calculates a random load profile for the load asset based on the sim time step in MW
        """
        test = np.empty([int(np.ceil(self.sim_length / self.time_step))]) # initiate empty array
        for i in range(len(test)):
            test[i] = round(random.uniform(0, self.maxLoad), 2)

        return(test)
        

class energyStorage():
    """
    A class to represent storage assets on the grid.
    
    ...
    
    Attributes
    ----------
    name : str
        Name of the storage asset
    maxOutput : float
        Max power output (MW)
    state : str
        state of asset - 'Charging', 'Discharging' or 'Static'
    maxCapacity : float
        defines the max energy of the asset MWh
    currentCapacity: float
        the current energy stored in the asset MWh
        
    Methods
    -------
    check_capability() -> float:
        Returns current load power demand in MW

    """
    def __init__(self, name, maxOutput, maxCapacity, time_step, currentCapacity):
        self.name : str = name # asset name
        self.maxOutput : float = maxOutput # Max Power output MW
        self.maxCapacity : float = maxCapacity # MWh
        self.currentCapacity : float = currentCapacity if currentCapacity is not None else 0 # MWh
        self.time_step : float = time_step # sim time step in hrs
        
    def __str__(self):
        return f"Name: {self.name}, Max Output: {self.maxOutput} MW, Max Capacity: {self.maxCapacity} MWh, Current Capacity: {self.currentCapacity}"
    
    
    def report_capabiltiy(self, grid_power_req):
        
        # grid power req is positive when power needs to be added to grid
        # grid power req is negative wen power needs to be absorbed by the grid
        
        # first check if asset can charge and discharge i.e. is it at max or min current capacity
        # check if max power is greater than grid demand - if so reduce
        # if asset can charge/discharge, max power isn't greater than demand, and has current cap greater than service_time*max_output it should operate at max power
        # if there isn't enough energy available it should bid in with a reduced power output
        # output format [can_serve [bool], power_provided to grid, new capacity]
        
        
        # cover edge cases, asset unable to charge/discharge
        if grid_power_req < 0 and self.currentCapacity == self.maxCapacity:
            return([False, 0, self.currentCapacity])
        
        if grid_power_req > 0 and self.currentCapacity == 0:
            return([False, 0, self.currentCapacity])
        
        
        # now consider cases where asset is able to particpate
        
        # need to ensure asset is bidding in with enough energy to supply quoted power
        # if there isn't enough energy available to supply max output for time period need to find new power limit
        if self.maxOutput * self.time_step > self.currentCapacity:
            # can't sustain max power for the time period so need to bid in with new power limit
            temp_power_limit = self.currentCapacity / self.time_step
        else:
            temp_power_limit = self.maxOutput
        
        # edge case
        # if the grid needs less power than the asset can provide, we need to supply less power
        if abs(grid_power_req) < temp_power_limit:
            # we reduce power output of asset to match exact grid requirement
            if grid_power_req > 0: # if asset needs to discharge
                self.currentCapacity -= grid_power_req*self.time_step
                return([True, grid_power_req, self.currentCapacity])
            if grid_power_req < 0: # asset needs to charge from grid
                self.currentCapacity += grid_power_req*self.time_step
                return([True, -1*grid_power_req, self.currentCapacity])
            

        
        # in case where more power needs to provided to grid than asset can provide
        if abs(grid_power_req) > temp_power_limit:
            if grid_power_req > 0: # if asset needs to discharge
                self.currentCapacity -= temp_power_limit*self.time_step
                return([True, temp_power_limit, self.currentCapacity])
            if grid_power_req < 0: # asset needs to charge from grid
                self.currentCapacity += temp_power_limit*self.time_step
                return([True, -1*temp_power_limit, self.currentCapacity])


            
        
# test cases
'''
x = energyGenerator(name = "test", max_power = 45, time_step = 0.25, sim_length= 14)
print(x.calculate_generation())

y = energyGenerator(name = "test_2", max_power = 9000, time_step = 0.6, sim_length= 9)
print(y.calculate_generation())


z = energyLoad(name = "test", maxLoad= 50, time_step= 0.3, sim_length= 40)
print(y.calculate_generation())


a = energyStorage(name = "test", maxOutput= 50, maxCapacity= 100, time_step=0.25, currentCapacity= 100)
print(a.report_capabiltiy(40))

b = energyStorage(name = "test", maxOutput= 30, maxCapacity= 100, time_step=0.25, currentCapacity= 100)
print(b.report_capabiltiy(40))

c = energyStorage(name = "test", maxOutput= 30, maxCapacity= 100, time_step=0.25, currentCapacity= 50)
print(c.report_capabiltiy(-40))

'''