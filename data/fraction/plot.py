import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv(f"solid1.csv", header=None)
# arr = df[0].values
# plt.plot(arr)
# plt.show()

df = pd.read_csv(f"../con/nom_con.csv", header=None)
arr = df[0].values
plt.plot(arr)
plt.show()
