from testClasses import energyStorage

storage = energyStorage(50, "static", 100, 2, 10)

print(storage)


print(storage.check_capability_discharge(100, 0.001))