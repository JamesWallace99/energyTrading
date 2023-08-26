from testESObot import esoBot
from config import energyLoad, energyGenerator, energyStorage

test_bot = esoBot()

# test generators generation
test_bot.generate_generators_random(num_assets=5, power_range=[50, 100])

for i in range(len(test_bot.generator_assets)):
    print(test_bot.generator_assets[i])
    
# test storage generation
    
test_bot.generate_storage_random(num_assets= 5, output_range= [50, 100], max_capacity_range= [100, 200], current_range= [0, 200])

for i in range(len(test_bot.storage_assets)):
    print(test_bot.storage_assets[i])


# test load generation

test_bot.generate_load_random(num_assets= 5, max_load_range= [10, 100], load_time_limit_range= [0.01, 1])

for i in range(len(test_bot.generator_assets)):
    print(test_bot.load_assets[i])

test_bot.initiate_grid(mode = "random", asset_csv_pathname="test")