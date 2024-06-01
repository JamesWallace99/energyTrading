import ESObot
import config
import numpy as np
import matplotlib.pyplot as plt

x = ESObot.esoBot()

csv_filepath = "test_random_input.csv"

# load assets into eso register
# x.initiate_grid_csv(csv_filepath)

# calculate the imbalance from forecasts
# print(x.imbalance_profile)
# x.get_imbalance_forecast(sim_length = 10, time_step= 1)

test_time_step = 0.25
test_sim_length = 240

# x.balance_grid(sim_length=test_sim_length, time_step=test_time_step, asset_csv_pathname= csv_filepath)
# x.plot_imbalance(sim_length=test_sim_length, time_step= test_time_step)


sim_runs = 100
average_resulting_imbalance = np.empty([int(np.ceil(test_sim_length / test_time_step))]) 

for i in range(sim_runs):
    x.balance_grid(sim_length=test_sim_length, time_step=test_time_step, asset_csv_pathname= csv_filepath)
    average_resulting_imbalance += x.imbalance_profile
    
    
average_resulting_imbalance = average_resulting_imbalance / 100 

print("Average imbalance from all sims: ", average_resulting_imbalance)

plt.plot(average_resulting_imbalance)
plt.show()