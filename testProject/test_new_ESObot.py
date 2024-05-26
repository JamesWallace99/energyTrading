import newESObot
import new_config

x = newESObot.esoBot()

csv_filepath = "test_random_input.csv"

# load assets into eso register
x.initiate_grid_csv(csv_filepath)

# calculate the imbalance from forecasts
print(x.get_imbalance_forecast(sim_length = 10, time_step= 1))


