import ESObot
import config

x = ESObot.esoBot()

csv_filepath = "test_random_input.csv"

# load assets into eso register
# x.initiate_grid_csv(csv_filepath)

# calculate the imbalance from forecasts
# print(x.imbalance_profile)
# x.get_imbalance_forecast(sim_length = 10, time_step= 1)

test_time_step = 0.25
test_sim_length = 240


x.balance_grid(sim_length=test_sim_length, time_step=test_time_step, asset_csv_pathname= csv_filepath)
x.plot_imbalance(sim_length=test_sim_length, time_step= test_time_step)