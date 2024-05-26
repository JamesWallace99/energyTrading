from testESObot import esoBot

test_bot = esoBot()

test_bot.initiate_grid(mode='random', asset_csv_pathname= "test_random_input.csv")

for i in range(len(test_bot.generator_assets)):
    print(test_bot.generator_assets[i])

for i in range(len(test_bot.load_assets)):
    print(test_bot.load_assets[i])
    
for i in range(len(test_bot.storage_assets)):
    print(test_bot.storage_assets[i])