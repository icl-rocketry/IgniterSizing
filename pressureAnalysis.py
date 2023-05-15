import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("thanoscoldflow.csv",usecols=[0, 1, 2, 3, 4, 14])
print(df)

df.columns = ["P1", "P2", "P3", "P4", "P5", "Time"]

df.set_index("Time").plot()
plt.show()