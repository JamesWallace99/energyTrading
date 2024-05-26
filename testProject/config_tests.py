from config import energyGenerator
from config import energyLoad
from config import energyStorage

import numpy as np

x = energyGenerator(name = "test", max_power = 45, time_step = 0.25, sim_length= 14)
print(x.calculate_generation())

y = energyGenerator(name = "test_2", max_power = 9000, time_step = 0.6, sim_length= 9)
print(y.calculate_generation())

z = energyLoad(name = "test", maxLoad= 50, time_step= 0.3, sim_length= 40)
print(z.calculate_load())

# test fully charged asset discharging
# should work
print("Fully charged discharging")
a = energyStorage(name = "test", maxOutput= 50, maxCapacity= 100, currentCapacity= 100)
x = np.linspace(0.1, 1, 10)


for i in x:
    print("Power Required:", 10)
    print("Time step (hrs):", i)
    print("Energy required:", i * 10)
    print(a.report_capabiltiy(10, i))
    
# test fully discharged asset discharging
# should fail
print("Fully discharged discharging")
b = energyStorage(name = "test", maxOutput= 50, maxCapacity= 100, currentCapacity= 0)
x = np.linspace(0.1, 1, 10)


for i in x:
    print("Power Required:", 10)
    print("Time step (hrs):", i)
    print("Energy required:", i * 10)
    print(b.report_capabiltiy(10, i))
    
# test fully charged asset charging
# should fail
print("Fully charged charging")
c = energyStorage(name = "test", maxOutput= 50, maxCapacity= 100, currentCapacity= 100)
x = np.linspace(0.1, 1, 10)


for i in x:
    print("Power Required:", -10)
    print("Time step (hrs):", i)
    print("Energy required:", i * -10)
    print(c.report_capabiltiy(-10, i))



# test fully discharged asset charging
# should pass
print("Fully discharged charging")
d = energyStorage(name = "test", maxOutput= 50, maxCapacity= 100, currentCapacity= 0)
x = np.linspace(0.1, 1, 10) # timesteps 


for i in x:
    print("Power Required:", -10)
    print("Time step (hrs):", i)
    print("Energy required:", i * -10)
    print(d.report_capabiltiy(-10, i))
