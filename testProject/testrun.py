from testClasses import Solar
from testClasses import energyLoad
from testClasses import energyStorage

solar_one = Solar("sunny_meadows", 50, (500, 700), 500)
load_one = energyLoad(75, 0)
storage_one = energyStorage(50, "inactive")

for i in range(10):
    storage_available = storage_one.maxCap - storage_one.currentCharge
    deficit = solar_one.current_output() - load_one.current_load()
    
    print("\n Storage asset has an instantanous {}MW of capacity available to discharge".format(storage_one.currentCharge))
    print("Instantaneous grid excess of {}MW detected, invoking balancing mechanism".format(deficit))
    
    if deficit >= 0: # if generation is greater than load charge up the battery
        if (deficit + storage_one.currentCharge) > storage_available: # if the deficit will cause us to exceed battery capacity
            print("Require generation curtailment of {}MW".format(deficit - storage_available))
            storage_one.currentCharge = storage_one.maxCap
        else: # if there is enough storage to handle the excess
            storage_one.currentCharge += deficit # charge the battery
        
    elif deficit < 0: # if demand is greater than generation
        if storage_one.currentCharge > abs(deficit): # check if our available battery capacity is enough to meet deficit
            storage_one.currentCharge -= abs(deficit) # discharge battery
            continue
        else: #if the current charge within storage is not large enough to serve the deficit
            deficit += storage_one.currentCharge
            storage_one.currentCharge = 0
            print("Blackout on grid caused by {}MW deficit in generation and available storage.".format(deficit))
            

