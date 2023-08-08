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

class Wind(energyGenerator):
    
    # account for windspeed from historic data set
    # account for angle of wind turbine
    
    pass


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
    def __init__(self, maxCap, state, currentCharge = None):
        self.maxCap = maxCap # define th  max capacity of the storage device in MW
        self.state = state
        self.currentCharge = currentCharge if currentCharge is not None else 0 # define the available capacity of the storage device in MW

        
        
class esoBot():
    # first let botESO build new assets if load is higher than generation
    pass

# national grid esoBot should make an assumption on power demands based on forecast
# once in the market national grid esoBot should compare demand and supply and chose to activate storage when needed
# add asset state, update state to neutral or discharge depending on action currently being performed
# once serviced then update state
# then consider bidding strategy from storage bots into the market - their strategies should prefer max profit
# esoBot should constrain by grid servicing but also try to optimise on price

    


