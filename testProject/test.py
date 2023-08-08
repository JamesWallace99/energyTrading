import random

# set up on Github and use Github issues and project to flesh out tasks to add

# incorporate variable demand and generation first in real time then also account for capacity sold in the day ahead market
# incorporate more realistic load patterns - use an example house following daily pattern

# incorporate more complex subclasses like factories and power stations
# account for energy capacity available and discharge time
# allow for multiple generators in grid
# allow for multiple storage devices in grid
# set energy pricing through market based on demand
# set storage and generator assets so they aim to maximise profit
# account for voltage discrepencies in the grid

class energyGenerator():
    def __init__(self, name, power, location):
        self.name = name
        self.power = power
        self.location = location # tuple of long-lat need to define data format
        
    # inheritence on time and weather for generator assets as we can make ouput dependent on this?
        
    def __str__(self):
        return f"Site Name: {self.name}, Power Output: {self.power}"

    
# def sub classes for wind and solar

class Solar(energyGenerator):
    
    def __init__(self, name, power, location, area):
        super().__init__(name, power, location)
        self.area = area # panel area
        # look up further determining factors on solar generator performance
        
    def current_output(self):
        """
        Return the current output of the solar asset
        """
        # use time and location and compare to irradiance dataset to calculate irradiance
        # convert irradiance to solar farm output using heat-rate / efficiency
        
        return(random.randint(0, self.power))
    
    # account for the angle of incidence of the solar farm and combine with irradiance to calculate current output
    # constrain based on physical properties of the panels and infrastructure of site
    
    pass

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
    
    
    
solar_one = Solar("sunny_meadows", 50, (500, 700), 500)
load_one = energyLoad(75, 0)
storage_one = energyStorage(50, "inactive")

# change order so system still tries to minise blackout by discharging the battery even if there isn't enough energy
# same for storing energy from the grid
# report the amount at which the grid exceeded / failed to provide power

for i in range(10):
    print(storage_one.currentCharge)
    generation = solar_one.current_output()
    load = load_one.current_load()
    storage_available = storage_one.maxCap - storage_one.currentCharge
    energy_available = storage_one.currentCharge
    if (generation - load) > storage_available: # if there is too much energy in the grid
        print("Overload on the grid! Too much power!")
        continue
    if (generation - load) < energy_available: # if there isn't enough energy in the grid
        print("Blackout on the grid! Not enough power!")
        continue
    if (generation - load) > 0: # charge up the battery
        storage_one.currentCharge += (generation - load)
        print("Charging the battery")
    if (generation - load) < 0: # discharge the battery
        storage_available -= (generation - load)
        print("Discharging the battery")
        
        
class esoBot():
    # first let botESO build new assets if load is higher than generation
    pass

# national grid esoBot should make an assumption on power demands based on forecast
# once in the market national grid esoBot should compare demand and supply and chose to activate storage when needed
# add asset state, update state to neutral or discharge depending on action currently being performed
# once serviced then update state
# then consider bidding strategy from storage bots into the market - their strategies should prefer max profit
# esoBot should constrain by grid servicing but also try to optimise on price

    


