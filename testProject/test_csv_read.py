import pandas as pd

df = pd.read_csv("test_random_input.csv")

print(df.head)
print(df.columns[0: 5])