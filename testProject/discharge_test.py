from testClasses import energyStorage

storage = energyStorage(50, "static", 100, 2, 90)

print(storage)


print(storage.check_capability('charge', 50, 0.5))

