from config import Solar
from config import energyLoad
from config import energyStorage

solar = Solar(name = 'solar1', power = 50, location = 'birmingham', panel_area=100)
load = energyLoad(maxLoad=50, loadTimeLimit= 0.5)
bat_one = energyStorage(maxOutput=500, state = 'static', maxCapacity=1000, MaxCRate=2, currentCapacity=500)

for i in range(10):
    storage_available = bat_one.maxCapacity - bat_one.currentCapacity
    imbalance = solar.current_output() - load.current_load() # what is the difference between supply and demand
    time_demand = load.current_load_time()
    
    print("\n Storage asset has {}MWh of energy available to discharge".format(bat_one.currentCapacity))
    print("Grid imbalance of {}MW detected, invoking balancing mechanism".format(imbalance))
    
    if imbalance > 0: # generation is greater than demand
        print('Generation greater than demand, attempting to charge batteries')
        state = bat_one.check_capability(contract_type='charge', power_required=imbalance, service_time=time_demand)
        
        if state[0] is not True:
            print("No storage available, grid overloaded")
            continue
        
        bat_one.state = 'charging' # activate the battery
        print(state)
        bat_one.currentCapacity = int(state[3]) # charge the battery up
        imbalance -= state[2] # update the grid state
        bat_one.state = 'static'
        
        if imbalance != 0:
            print("{}MW Curtailment required".format(imbalance))
            continue
    
    if imbalance < 0: # demand is greater than generation
        print('Demand greater than generation, attempting to discharge batteries')
        state = bat_one.check_capability(contract_type='discharge', power_required=abs(imbalance), service_time=time_demand)
        
        if state[0] is not True:
            print("No storage available, grid in deficit")
            continue
        
        bat_one.state = 'discharging' # activate the battery
        print(state)
        bat_one.currentCapacity = int(state[3]) # discharge the battery
        imbalance += state[2] # update the grid state
        bat_one.state = 'static'
        
        if imbalance != 0:
            print("{}MW Backup power required".format(imbalance))

        
