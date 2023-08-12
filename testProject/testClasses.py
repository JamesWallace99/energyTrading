import random

class energyGenerator():
    def __init__(self, name, power, location):
        self.name = name
        self.power = power
        self.location = location # tuple of long-lat need to define data format
        
    def __str__(self):
        return f"Site Name: {self.name}, Power Output: {self.power}"

class Solar(energyGenerator):
    # subclass for solar generator
    def __init__(self, name, power, location, panel_area):
        super().__init__(name, power, location)
        self.panel_area = panel_area # panel area
        
    def current_output(self):
        """
        Return the current output of the solar asset
        """
        # use time and location and compare to irradiance dataset to calculate irradiance
        # convert irradiance to solar farm output using heat-rate / efficiency
        
        return(random.randint(0, self.power))
    
    # account for the angle of incidence of the solar farm and combine with irradiance to calculate current output
    # constrain based on physical properties of the panels


class energyLoad():
    def __init__(self, maxLoad, loadProvided):
        self.maxLoad = maxLoad
        self.loadProvided = loadProvided
    
    def current_load(self):
        """
        Return the current load demanded by the grid
        """
        return(random.randint(0, self.maxLoad))
        
class energyStorage():
    def __init__(self, maxOutput: float, state: str, maxCapacity: float, MaxCRate: float, currentCapacity: float):
        self.maxOutput = maxOutput # Max Power output MW
        self.state = state # Charging, Discharging or Static
        self.maxCapacity = maxCapacity # MWh
        self.MaxCRate = MaxCRate # int
        self.currentCapacity = currentCapacity if currentCapacity is not None else 0 # MWh
        self.systemTime = maxCapacity / maxOutput
        
    def check_capability(self, contract_type: str, power_required: float, service_time: float):
        
        # service time should be provided in hours
        # call this method to check if the asset is capable of delivering the service market requires
        # return False if storage asset cannot provide service
        # return True, power delivered and currentCapacity at end of service if asset capable of full/partial service
        # should also flag is complete or partial service provided
        
        if contract_type == 'charge':
            if self.currentCapacity == self.maxCapacity:
                return(False, 'System fully charged already.')
            
            available_energy = self.maxCapacity - self.currentCapacity
            power_available = min(available_energy / service_time, self.maxOutput)
            
        
        if contract_type == 'discharge':
            if self.currentCapacity == 0: # if no charge cannot deliver a discharge service
                return(False, "No charge in system")
            
            power_available = min(self.currentCapacity / service_time, self.maxOutput) # calc max power available from system
            
        if power_available == power_required:
            return(True, "full", power_available, self.currentCapacity - power_available*service_time)
        
        else:
            return(True, "partial", power_available, self.currentCapacity - power_available*service_time)
        
        
                   
    
    
        
        

      
        


