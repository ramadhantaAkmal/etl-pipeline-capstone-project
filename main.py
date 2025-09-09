import pandas as pd

data = pd.read_csv("data/population_data.csv",dtype='str', skiprows=4)

print(data.head)