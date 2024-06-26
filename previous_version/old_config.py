import random

class energyGenerator():
    """
    A class to represent a generator asset on the grid.
    
    ...
    
    Attributes
    ----------
    name : str
        Name of the generator asset
    power : float
        Max power output of the generator asset (MW)
    location : List[float]
        List containing lat and long of generator asset
        
    Methods
    -------
    None

    """
    def __init__(self, name, power, location= None):
        self.name : str = name
        self.power : float = power
        self.location : list[float] = location # list of long-lat need to define data format
        
    def __str__(self):
        return f"Site Name: {self.name}, Power Output: {self.power}"

class Solar(energyGenerator):
    """
    A class to represent a solar generator asset on the grid.
    
    ...
    
    Attributes
    ----------
    name : str
        Name of the generator asset
    power : float
        Max power output of the generator asset (MW)
    location : List[float]
        List containing lat and long of generator asset
    panel_area : float
        Panel surface area used for power output calculation
        
    Methods
    -------
    current_output() -> float:
        Returns current output in MW

    """
    
    def __init__(self, name, power, location = None, panel_area = None):
        super().__init__(name, power, location)
        self.panel_area : float = panel_area # panel area
        
    def current_output(self) -> float:
        """
        Returns current output in MW

                Parameters:
                        None

                Returns:
                        float, uniform randomised value based on max output
    
        """
        # use time and location and compare to irradiance dataset to calculate irradiance
        # convert irradiance to solar farm output using heat-rate / efficiency
        
        return(round(random.uniform(0, self.power), 2))
    
    def __str__(self):
        return f"Name: {self.name}, Current Output: {self.current_output()} MW, Max Output: {self.power} MW"
    
    # account for the angle of incidence of the solar farm and combine with irradiance to calculate current output
    # constrain based on physical properties of the panels

class energyLoad():
    """
    A class to represent load assets on the grid.
    
    ...
    
    Attributes
    ----------
    name : str
        Name of the load asset
    maxLoad : float
        Max power demanded by the load asset (MW)
    loadTimeLimit : float
        Max Time in hrs that load power is demanded for
    location : List[float]
        List containing lat and long of load asset
        
    Methods
    -------
    current_load() -> float:
        Returns current load power demand in MW
        
    current_load_time() -> float:
        Returns time that current load is demanded for in hrs

    """
    def __init__(self, name, maxLoad, loadTimeLimit, location = None):
        self.name : str = name # name of load asset
        self.maxLoad : float = maxLoad # max load in MW
        self.loadTimeLimit : float = loadTimeLimit # limit in hrs of time demanded to deliver load
        self.location : list[float] = location # list of long-lat need to define data format
        
    def __str__(self):
        return f"Name: {self.name}, Max Load: {self.maxLoad} MW, Load Time Limit: {self.loadTimeLimit} hrs, Current Load: {self.current_load()} MW, Current Load Time: {self.current_load_time()} hrs"
    
    def current_load(self):
        """
        Returns current load power demand in MW

                Parameters:
                        None

                Returns:
                        float, uniform randomised value based on max load
    
        """
        return(random.uniform(0, self.maxLoad))
    
    def current_load_time(self):
        """
        Returns time that current load is demanded for in hrs

                Parameters:
                        None

                Returns:
                        float, uniform randomised value based on max load time limit
    
        """
        return(random.uniform(0, self.loadTimeLimit))
    
        
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
    def __init__(self, name: str, maxOutput: float, state: str, maxCapacity: float, currentCapacity: float):
        self.name : str = name # asset name
        self.maxOutput : float = maxOutput # Max Power output MW
        self.state : str = state # Charging, Discharging or Static
        self.maxCapacity : float = maxCapacity # MWh
        self.currentCapacity : float = currentCapacity if currentCapacity is not None else 0 # MWh
        
    def __str__(self):
        return f"Name: {self.name}, Max Output: {self.maxOutput} MW, Max Capacity: {self.maxCapacity} MWh, Current Capacity: {self.currentCapacity}"
        
    def check_capability(self, contract_type: str, power_required: float, service_time: float):
        """
        Checks if, and to what extent, the storage asset can provide a demanded service
        Assumes that asset is always able to meet max power output

                Parameters:
                        contract_type: str - Charge or Discharge
                        power_required: float - power needed to be provided to fulfill service MW
                        service_time: float - time that service is required for hrs

                Returns:
                        True / False if asset is able/not able to provide at least a partial service
                        Power delivered - this needs to change to energy
                        currentCapacity at end of service - currently only reported if asset provides service, change
                        
                        
        """
        
        # first check if asset can charge and discharge i.e. is it at max or min current capacity
        # check if max power is greater than demand - if so reduce and calcualte energy that can be provided
        # if asset can charge/discharge, max power isn't greater than demand, and has current cap greater than service_time*max_output it should operate at max power
        # if there isn't enough energy available it should bid in with a reduced power output
        
        if contract_type == 'charge':
            # first check if storage is at max capacity
            if self.currentCapacity == self.maxCapacity: # if no available capacity system cannot charge
                return(False, 'System fully charged already.')
            
            # now check to see if the demanded power from grid is less than asset max
            
            available_storage = self.maxCapacity - self.currentCapacity
            power_available = min(available_storage / service_time, self.maxOutput) # this looks wrong
            
            
            if power_available >= power_required:
                return(True, "full", power_required, self.currentCapacity + power_available*service_time)
            
            else:
                return(True, "partial", power_available, self.currentCapacity + power_available*service_time)
            
        if contract_type == 'discharge':
            # first, check if storage is at min capacity
            if self.currentCapacity == 0: # if no charge cannot deliver a discharge service
                return(False, "No charge in system")
            
            power_available = min(self.currentCapacity / service_time, self.maxOutput) # calc max power available from system
            
            if power_available >= power_required:
                return(True, "full", power_required, self.currentCapacity - power_available*service_time)
            
            else:
                return(True, "partial", power_available, self.currentCapacity - power_available*service_time)
        
        
                   
    
    
        
        

      
        


