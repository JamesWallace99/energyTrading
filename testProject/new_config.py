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
    def __init__(self, name, max_power, location= None, gen_forecast = None):
        self.name : str = name
        self.max_power : float = max_power
        self.location : list[float] = location # list of long-lat need to define data format
        self.gen_forecast: list[float] = gen_forecast
        
        
    def __str__(self):
        return f"Site Name: {self.name}, Power Output: {self.max_power}"
    
    def calculate_generation(self, sim_length, time_step):
        """
        Calculates a random generation profile for the generation asset based on the sim time step
        """
        test = np.empty([int(np.ceil(sim_length / time_step))]) # initiate empty array
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
    def __init__(self, name, maxLoad, load_forecast = None, location = None):
        self.name : str = name # name of load asset
        self.maxLoad : float = maxLoad # max load in MW
        self.location : list[float] = location # list of long-lat need to define data format
        self.load_forecast : list[float] = load_forecast # array containing load forecast for asset in MW
        
    def __str__(self):
        return f"Name: {self.name}, Max Load: {self.maxLoad} MW, Load Time Limit: {self.loadTimeLimit} hrs, Current Load: {self.current_load()} MW, Current Load Time: {self.current_load_time()} hrs"
    
    
    def calculate_load(self, sim_length, time_step):
        """
        Calculates a random load profile for the load asset based on the sim time step in MW
        """
        test = np.empty([int(np.ceil(sim_length / time_step))]) # initiate empty array
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
    maxCapacity : float
        defines the max energy of the asset MWh
    currentCapacity: float
        the current energy stored in the asset MWh
    time_step: float
        Time in hours that power is demanded from the asset
        
    Methods
    -------
    report_capability() -> float:
        Returns asset's abiltiy to conduct trade and capacity of asset after trade.
        Input: grid power requirement
               Positive when power needs to be added to the grid
               Negative when power needs to be removed from the grid
        Output: List[can conduct trade: boolean, power provided to grid: float, updated asset capacity: float]

    """
    def __init__(self, name, maxOutput, maxCapacity, currentCapacity):
        self.name : str = name # asset name
        self.maxOutput : float = maxOutput # Max Power output MW
        self.maxCapacity : float = maxCapacity # MWh
        self.currentCapacity : float = currentCapacity if currentCapacity is not None else 0 # MWh
        
    def __str__(self):
        return f"Name: {self.name}, Max Output: {self.maxOutput} MW, Max Capacity: {self.maxCapacity} MWh, Current Capacity: {self.currentCapacity}"
    
    
    def report_capabiltiy(self, grid_power_req, time_step):
        
        '''
        Returns asset's abiltiy to conduct trade and state of asset after trade.
        Input: grid power requirement
                Positive when power needs to be added to the grid
                Negative when power needs to be removed from the grid
               time_step - time that power is required from asset
        Output: List[can conduct trade: boolean, power provided to grid: float, updated asset capacity: float]
        '''
        
        # first check if asset can charge and discharge i.e. is it at max or min current capacity
        # check if max power is greater than grid demand - if so reduce
        # if asset can charge/discharge, max power isn't greater than demand, and has current cap greater than service_time*max_output it should operate at max power
        # if there isn't enough energy available it should bid in with a reduced power output
        # output format [can_serve [bool], power_provided to grid, new capacity]
        # eventually needs to calculate a price at which the asset will bid into power market
        
        
        # set an internal state that matches current capacity as we are checking capabiltiy
        
        energy_available = self.currentCapacity
    

        
        
        # cover edge cases, asset unable to charge/discharge
        if grid_power_req < 0 and energy_available == self.maxCapacity:
            return([False, 0, energy_available]) # grid wants asset to charge but is at full cap
        
        if grid_power_req > 0 and energy_available == 0:
            return([False, 0, energy_available]) # grid wants asset to discharge but asset has no energy
        
        
        # now consider cases where asset is able to particpate
        
        # need to ensure asset is bidding in with enough energy to supply quoted power
        # if there isn't enough energy available to supply max output for time period need to find new power limit
        
        # temp power limits setting doesn't work when asset is charging
        
        # need to write cases for charging and discharging
        
        # if charging
        # (max capacity - storage capacity) is the energy to fill
        # need to compare this to the 
        
        if grid_power_req > 0: # asset discharging
            if self.maxOutput * time_step > energy_available:
                # can't sustain max power for the time period so need to bid in with new power limit
                temp_power_limit = energy_available / time_step
            else:
                temp_power_limit = self.maxOutput
        if grid_power_req < 0: # asset charging
            energy_to_fill = self.maxCapacity - energy_available
            if self.maxOutput * time_step > energy_to_fill:
                # can't sustain max power for the time period so need to bid in with new power limit
                temp_power_limit = -1* energy_to_fill / time_step
            else:
                temp_power_limit = -1* self.maxOutput
        
        
        # edge case
        # if the grid needs less power than the asset can provide, we need to supply less power
        if abs(grid_power_req) < abs(temp_power_limit):
            # we reduce power output of asset to match exact grid requirement
            if grid_power_req > 0: # if asset needs to discharge
                energy_available -= grid_power_req*time_step
                return([True, grid_power_req, energy_available])
            if grid_power_req < 0: # asset needs to charge from grid
                energy_available += -1* grid_power_req*time_step
                return([True, grid_power_req, energy_available])
            

        
        # in case where more power needs to provided to grid than asset can provide
        if abs(grid_power_req) > abs(temp_power_limit):
            if grid_power_req > 0: # if asset needs to discharge
                energy_available -= temp_power_limit*time_step
                return([True, temp_power_limit, energy_available])
            if grid_power_req < 0: # asset needs to charge from grid
                energy_available += -1* temp_power_limit*time_step
                return([True, temp_power_limit, energy_available])

    def execute_trade(self, grid_power_req, time_step):
        '''
        Executes on a market trade and updates assets currentCapacity
        Input: float power required by market.
                    Positive if power needs to be added
                    Negative if power needs to be removed
                time_step
        Output: boolean, true if trade succesful, false if trade not succesful
        '''
        temp = self.report_capabiltiy(grid_power_req, time_step)
        if temp[0]:
            self.currentCapacity += temp[2]
            return(True)
        else:
            return(False)

